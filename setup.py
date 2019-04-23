import setuptools

with open("README.md", "r") as fh:
    long_description=fh.read()

setuptools.setup(
    name='wxpy-mvc',
    version='0.1',
    scripts=['bin/wxpy-mvc'],
    author='Xet',
    author_email='ethan.jones@my.jcu.edu.au',
    description='wx python MVC framework',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xett/wxpy-mvc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
        "Operating System :: OS Independent",
    ]
)
