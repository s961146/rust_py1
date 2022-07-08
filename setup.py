from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rust_py1",
    version="0.0.1",
    author="Rado",
    author_email="itsmebg@gmail.com",
    description="Calculates a Fibonacci number",
    long_description="A basic library that calculates Fibonacci numbers",
    long_description_content_type="text/markdown",
    url="",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)