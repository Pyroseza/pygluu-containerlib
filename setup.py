import codecs
import os
import re
from setuptools import setup
from setuptools import find_packages


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), 'r') as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="pygluu-containerlib",
    version=find_version("pygluu", "containerlib", "__init__.py"),
    url="",
    license="Gluu Support",
    author="Gluu",
    author_email="isman@gluu.org",
    description="",
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "requests>=2.22.0",
        "python-consul>=1.0.1",
        "hvac>=0.7.0",
        "kubernetes",
        "urllib3<1.25,>=1.21.1",
        "ldap3>=2.5",
        "backoff>=1.8.0",
        "docker>=3.7.2",
        "requests-toolbelt>=0.9.1",
        "cryptography>=2.8",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
)
