# setup.py

from setuptools import setup, find_packages

setup(
    name="nugu",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="YangChoi",
    author_email="yangchoi.hj@gmail.com",
    description="About nugu prgrammer named YangChoi",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yangchoi/nugu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
