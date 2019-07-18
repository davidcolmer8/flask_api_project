from setuptools import setup

setup(
    name='simpleApp',
    version='0.1',
    py_modules=['simpleApp'],
    install_requires=[
        ,
    ],
    entry_points={
        'console_scripts':[
        'simpleApp=simpleApp:cli'
        ] 
    },
)