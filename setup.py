# pylint: disable=missing-module-docstring
import setuptools


with open("README.txt", "r") as fh:
    LONG_DESCRIPTION = fh.read()

REQUIREMENTS = []

setuptools.setup(
    name="aurora",
    version="1.0.0-pre-alpha",
    author="Fiona Wilson",
    author_email="fiona@razerfish.dev",
    description="",
    # TODO: Add description
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Razerfish/aurora",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    project_urls={
        "Source Code": "https://github.com/Razerfish/aurora",
        "Bug Tracker": "https://github.com/Razerfish/aurora/issues",
    },
    python_requires=">=3.5",
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'autopep8==1.5.*',
            'coverage==5.0.*',
            'nox>=2019.11.9',
            'pylint==2.4.*',
            'pytest==5.3.*',
            'pytest-cov==2.8.*',
            'rope==0.16.*',
        ],
        'lint': [
            'pylint==2.4.*',
        ],
        'test': [
            'pytest==5.3.*',
            'pytest-cov==2.8.*',
        ]
    }
)
