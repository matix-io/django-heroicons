from setuptools import setup, find_packages


with open('VERSION.txt') as f:
    version = f.readline()


setup(
    name='my_module',
    version=version,
    url='https://my_url',
    license='MIT',
    description='Project description',
    long_description='',
    author='Connor Bode',
    author_email='connor@matix.io',
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[],
)
