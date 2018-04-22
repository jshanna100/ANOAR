from distutils.core import setup

setup(name='anoar',
      pymodules=["anoar"],
      version=1,
      description='Automated Non-Ocular Artefact Rejection',
      author='Jeff Hanna',
      author_email='jeff.hanna@gmail.com',
      url='https://github.com/jshanna100/ANOAR/',
      packages = ['mne','numpy']
     )
