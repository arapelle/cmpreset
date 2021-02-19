import setuptools
import glob

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

scripts = ['cmpreset']

setuptools.setup(
    name='cmpreset',  
    version='0.1',
    scripts=scripts,
    author="Aymeric Pellé",
    author_email="aympelle@gmail.com",
    description="A CMakeUserPresets.json file manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arapelle/cmpreset",
    packages=setuptools.find_packages(), # GitPython
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
