from setuptools import setup

setup(
name='snapshotanalyzer-30000',
version='0.1',
author='nikunj',
author_email='nikunjcpatel01@gmail.com',
description="snapshot analyser is a tool to manage EC2 instances",
license="GPLv3+",
packages=['shotty'],
url="https://github.com/nikunjcpatel01/snapshotanalyzer-30000",
install_requires=['click','boto3'],
entry_points={
    'console_scripts':['shotty=shotty.shotty:cli']
    }
)
