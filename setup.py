from setuptools import setup, find_packages

setup(
    name="ikt111Toolkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tkinter",
        # Add other dependencies
    ],
    author="Your Name",
    description="A toolkit for IKT111 course, including search algorithm visualization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)