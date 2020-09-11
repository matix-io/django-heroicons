from setuptools import setup, find_packages


with open('VERSION.txt') as f:
    version = f.readline()


setup(
    name='django_heroicons',
    version=version,
    url='https://github.com/matix-io/django-heroicons',
    license='MIT',
    description='Easily use Heroicons in Django templates',
    long_description='',
    author='Connor Bode',
    author_email='connor@matix.io',
    packages=find_packages(),
	include_package_data=True,
    install_requires=[],
    zip_safe=False,
    classifiers=[],
)
