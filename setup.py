import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lncrnadbtable',
    version='0.1',
    packages=['lncrnadbtable'],
    provides=['lncrnadbtable'],
    include_package_data=True,
    license='BSD License, I think',  # example license
    description='djangocms with added features for lncrnadb usage',
    long_description=README,
    url='https://github.com/bluecerebudgerigar/lncrnadb-table',
    author='Quek Xiu Cheng',
    author_email='quekxiucheng@gmail.com',
    
)

