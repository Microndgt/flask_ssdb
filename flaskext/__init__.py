__version__ = '0.0.1'

import sys
from flaskext.ssdb import SSDB

PY3 = sys.version_info[0] == 3
if not PY3:
    raise SystemExit('Version must be greater than python3')
