from setuptools import find_packages, setup

setup(
    name='alpcom_api',
    packages=find_packages(include=['alpcom_api']),
    install_requires=[
        'requests==2.31.0',
        'pydantic==2.1.1',
        'pyjwt==2.8.0'
    ],
    version='1.0.1',
    description='ALP.com API Python',
    author='ALP.com',
    license='MIT'
)
