from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Các package phụ thuộc nếu có
    author="Khanh Duy",
    author_email="khanhduy23112006@example.com",
    description="A simple Python package",
    url="https://github.com/khanhduy2311/mypackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
