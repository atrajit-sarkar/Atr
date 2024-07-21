# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="Atrmaths",
    version="0.1.0",
    author="Atrajit Sarkar",
    author_email="atrajit.sarkar@gmail.com",
    description="Atrmaths: A powerful math library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atrajit-sarkar/Atrmaths.git",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        # Add any dependencies here
    ],
    python_requires=">=3.6",
)
