# Import Libs
import shutil
from setuptools import setup

# Clear previous build
#import os
#if os.path.isdir("dist"):
#    shutil.rmtree("dist")
#if os.path.isdir("build"):
#    shutil.rmtree("build")
#if os.path.isdir("Crypter.egg-info"):
#    shutil.rmtree("Crypter.egg-info")

setup(
    name='Crypter',
    version='3.3',
    install_requires=[
        "altgraph==0.17",
        "future==0.18.2",
        "macholib==1.14",
        "numpy==1.18.2",
        "pefile==2019.4.18",
        "pycryptodome==3.9.7",
        "PyInstaller==3.6",
        "Pypubsub==4.0.3",
        "pywin32==227",
        "pywin32-ctypes==0.2.0",
        "six==1.14.0",
        "wxPython==4.0.7"
    ],
    scripts=["Builder.pyw"],
    package_data={
        'CrypterBuilder': ['Resources\\*']
    },
    packages=[
        'Crypter', 'Crypter.Crypter',
        'CrypterBuilder'
    ],
    url='https://github.com/sithis993/Crypter',
    license='GPL-3.0',
    author='sithis',
    author_email='',
    description='Crypter Ransomware PoC and Builder'
)
