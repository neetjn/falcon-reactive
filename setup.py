
# pylint: disable=missing-docstring
from setuptools import setup


setup(
    name='falcon-reactive',
    description='Falcon plugin for handling reactive/async tasks.',
    version='0.0.1',
    url='https://neetjn.github.io/falcon-reactive/',
    author='John Nolette',
    author_email='john@neetgroup.net',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'rxpy'
    ],
    packages=['falcon_reactive']
)
