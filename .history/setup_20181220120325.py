from setuptools import setup

setup(
    name='bookStore',
    packages=['bookStore'],
    description='A training application',
    version='0.1',
    py_modules=['bookStore'],
    author="David Colmer",
    install_requires=[
        'Flask==1.0.2',
        'flask-restful',
        'Click',
        'Flasgger'
    ],
     entry_points={
        'console_scripts': [
            'bookStore = bookStore.click:cli'
        ]
    },
)