from setuptools import setup

setup(
    name='simpleApp',
    version='0.1',
    py_modules=['simpleApp'],
    author="David Colmer",
    install_requires=[
        'Flask==1.0.2',
        'Click'
    ],
    entry_points={
        'console_scripts':[
        'simpleApp=simpleApp:cli'
        ] 
    },
)