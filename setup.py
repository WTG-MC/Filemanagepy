
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filemanagepy", 
    version="0.0.1",
    author="WTG MC",
    author_email="windowstechmc0s@gmail.com",
    description="A library That Can Help with python file management",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url="https://github.com/ovipaul/zenith",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
