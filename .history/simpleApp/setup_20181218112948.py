from setuptools import setup

setup(
    name='simpleApp',
    version='0.1',
    py_modules=['simpleApp'],
    install_requires=[
        'Flask==1.0.2',
    ],
    entry_points={
        'console_scripts':[
        'simpleApp=simpleApp:cli'
        ] 
    },
)