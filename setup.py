# Setup for project

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read();

setup(
    name = 'pgbackup',
    version = '0.1.0',
    author = 'Damian Ramirez',
    author_email= 'dramirez@edrans.com',
    description= 'A utility for backing up PostgresSQL databases.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/damiramriez/pgbackup'
    packages = find_packages('src')
)