from setuptools import setup
from setuptools import find_packages

setup(
    name='fishlib',
    version=0.1,
    description='Something about robot fish',
    author='You',
    author_email='you@example.com',
    url='github/repo URL',
    packages=find_packages(),
    license='TBD',
    install_requires=[
        # List of dependencies
        'numpy',
    ],
    zip_safe=False,
)
