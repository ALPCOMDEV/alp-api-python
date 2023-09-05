from setuptools import find_packages, setup

setup(
    name='alp_api',
    packages=find_packages(include=['alp_api']),
    install_requires=[
        'requests==2.31.0',
        'pydantic==2.1.1',
    ],
    version='1.0.0',
    description='ALP.com API Python',
    author='John Petrucci',
)
