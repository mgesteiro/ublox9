"""
Created on 28 Nov 2020

@author: mgesteiro
"""
import setuptools
import os

from ublox9 import VERSION

# just in case someone is invoking this script from a different directory
rootfolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(rootfolder)

long_description = open("README.md", "r").read()

setuptools.setup(
    name="ublox9",
    version=VERSION,
    author="mgesteiro",
    author_email="mgesteiro@mgesteiro.com",
    description="u-blox generation 9 handling library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mgesteiro/ublox9",
    packages=setuptools.find_packages(exclude=["tests", "examples"]),
    license="GNU Affero General Public License v3.0",
    keywords="ublox9 GNSS GPS GLONASS Galileo BeiDou NMEA UBX RTCM u-blox",
    platforms="Windows, MacOS, Linux",
    project_urls={
        "Bug Tracker": "https://github.com/mgesteiro/ublox9",
        "Documentation": "https://github.com/mgesteiro/ublox9",
        "Source Code": "https://github.com/mgesteiro/ublox9",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Communications",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.6",
)
