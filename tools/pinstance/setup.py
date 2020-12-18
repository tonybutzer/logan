from setuptools import setup

setup (
    name='pinstance', 
    version='1.0',
    py_modules=['pinstance','awsutil'],
    install_requires=[
        'awscli',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pinstance=pinstance:cli
    '''
    ,
)
