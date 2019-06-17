from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f: 
    readme = f.read()

setup(
    name='mssql-account-manager', 
    version='0.1.0', 
    description='Commandline tool to manage MS SQL user accounts', 
    long_description=readme, 
    author = 'Norman Shipman', 
    author_email = 'nshipman@plaid.com', 
    packages=find_packages('src'), 
    package_dir={'': 'src'}, 
    install_requires=['cython', 'pymssql'],
    entry_points= {
        'console_scripts': [
            'mssqlam=mssql.cli:main',
        ]
    }

)