from setuptools import setup

with open("requirements.txt") as req:
    install_requires = req.read()

setup(name='covid-cases',
        version='0.0.1',
        description='',
        url='',
        author='Yuri Mussi',
        packages=['covid'],
        zip_safe=False
),