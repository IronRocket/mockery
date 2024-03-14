from setuptools import setup, find_packages

setup(
    name='mockery-translator',
    version='0.0.2',
    description = 'Translates boring text into mockery',
    author = 'Titus Federwisch',
    keywords = 'cli, convert, standalone, mockery',
    license = 'MIT',
    license_files = 'LICENSE',
    project_urls={
        'Source': 'https://github.com/IronRocket/mockery',
    },
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries"
    ],
    packages=find_packages(exclude=['img']),
    entry_points = {
        'console_scripts': ['mockery=mockery.mockery:main'],
    },
)