import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nicholasmole", 
    version="0.0.1",
    author="Nihcolas Mole",
    author_email="nmole065@gmail.com",
    description="Convert data from str to datetime or datetime to str.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicholasmole/jsondatetime_util",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
