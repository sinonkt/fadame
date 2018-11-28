from setuptools import setup, find_packages

setup(
    name='fadame',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        fadame=fadame:main
    ''',
)
