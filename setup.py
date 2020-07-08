from os import path
from setuptools import setup

BASE_DIR = path.abspath(path.dirname(__file__))

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]

reqs = parse_requirements('requirements.txt')

setup(
    name='Flask-Boto3',
    version='0.3.2',
    url='https://github.com/Ketouem/flask-boto3',
    license='MIT',
    author='Cyril "Ketouem" Thomas',
    author_email='ketouem@gmail.com',
    description='Flask extension that ties boto3 to the application',
    packages=['flask_boto3'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    install_requires=reqs,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
