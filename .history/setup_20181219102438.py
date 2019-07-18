from setuptools import setup

setup(
    name='simpleApp',
    description='A training application',
    version='0.1',
    py_modules=['simpleApp'],
    author="David Colmer",
    install_requires=[
        'Flask==1.0.2',
        'flask-restful',
        'Click'
    ],
     entry_points={
        'console_scripts': [
            'simpleApp = simpleApp.app:cli'
        ]
    },
)