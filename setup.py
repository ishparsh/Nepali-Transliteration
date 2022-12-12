import setuptools as setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nepali-to-roman',
    version='0.1.9',  # Required
    description='A PyPi package to convert Nepali words to Romanized English Literals. Here we perform translieration and convert Devanagari words into Roman Literals. Nepali to Roman',
    url='https://github.com/ishparsh/Nepali-Transliteration',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Diwas Pandey, Ishparsh Uprety & Navraj Pokharel',
    author_email='uprety.ishparsh@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,

    keywords=['Nepali to roman','Nepali Transliteration', 'devanagari to English', 'devanagari', 'Diwas Pandey', 'Ishparsh Uprety','Nepali to roman','Nepali words to roman','roman from nepali','convert nepali to roman','romanize nepali words','how to convert nepali to roman','convert Nepali to Roman'],

)
