import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lncrnadb_table',
    version='0.1',
    packages=['lncrnadb_table'],
    include_package_data=True,
    license='BSD License, I think',  # example license
    description='djangocms with added features for lncrnadb usage',
    long_description=README,
    url='https://github.com/bluecerebudgerigar/lncrnadb_table',
    author='Quek Xiu Cheng',
    author_email='quekxiucheng@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: DUCK Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

