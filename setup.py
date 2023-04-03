import setuptools
import re

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()


def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

version = ""
with open("sembed/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setuptools.setup(
    name="sembed",
    version=version,
    author="sevenc_nanashi",
    description="A wrapper of discord.Embed.",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/sevenc-nanashi/sembed",
    packages=['discord.ext.sembed', 'sembed'],
    project_urls={
        "Bug Tracker": "https://github.com/sevenc-nanashi/sembed/issues",
        "Documentation": "https://sembed.readthedocs.io",
    },
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
