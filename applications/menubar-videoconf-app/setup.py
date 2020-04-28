from setuptools import setup

with open('requirements.txt') as fd:
    REQUIREMENTS = fd.readlines()

APP = ('app.py',)
DATA_FILES = ()
OPTIONS = {
    'argv_emulation': True,
    'plist': {'CFBundleShortVersionString': '1.0.0', 'LSUIElement': True},
    'packages': REQUIREMENTS,
}

setup(
    app=APP,
    name='menubar-toolbox-sample',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=('py2app',),
    install_requires=REQUIREMENTS,
    version='1.0.0',
    license='',
    description="A Sample MenuBar App for MacOS",
    author='P.A. SCHEMBRI',
    author_email='pa.schembri@netsach.com',
)
