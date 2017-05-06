from __future__ import absolute_import
import pyssdb
from flask import current_app
try:
    from flask import _app_ctx_stack as _ctx_stack
except ImportError:
    from flask import _request_ctx_stack as _ctx_stack


class SSDB(object):
    def __init__(self, app=None, **connect_args):
        self.connect_args = connect_args
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # 只是配置app的相关东西,而不分配app到self
        app.config.setdefault('SSDB_HOST', 'localhost')
        app.config.setdefault('SSDB_PORT', 8888)
        app.config.setdefault('SSDB_PASSWORD', None)
        # 如果有新式的应用上下文处理器
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        elif hasattr(app, 'teardown_request'):
            app.teardown_request(self.teardown)
        else:
            app.after_request(self.teardown)

    def connect(self):
        self.connect_args['host'] = current_app.config['SSDB_HOST']
        self.connect_args['port'] = current_app.config['SSDB_PORT']
        ssdb_db = pyssdb.Client(**self.connect_args)
        return ssdb_db

    def teardown(self, exception):
        ctx = _ctx_stack.top
        if hasattr(ctx, "ssdb_db"):
            ctx.ssdb_db.disconnect()

    @property
    def connection(self):
        ctx = _ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'ssdb_db'):
                ctx.ssdb_db = self.connect()
                if current_app.config['SSDB_PASSWORD'] is not None:
                    ctx.ssdb_db.auth(current_app.config['SSDB_PASSWORD'])
            return ctx.ssdb_db

