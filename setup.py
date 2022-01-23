from setuptools import setup, find_packages

with open('README.rts') as f:
    readme = f.read

with open('LICENSE') as f:
    license = f.read

setup(
    name='promotion_engine',
    version='0.1.0',
    description='A Python program implement a promotion engine.',
    long_description=readme,
    author='Matthew Hornsey',
    author_email='hornseym@live.co.uk',
    url='https://github.com/HornseyM/promotion_engine',
    license=license,
    packages=find_packages(exclude=('test',))
)