from setuptools import setup


setup(
    name='Flask-SSDB',
    version='0.0.1',
    url='https://github.com/Microndgt/flask_ssdb/',
    license='BSD',
    author='Kevin Du',
    author_email='dgt_x@foxmail.com',
    description='Flask simple ssdb client',
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'pyssdb'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)