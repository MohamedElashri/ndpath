from setuptools import setup

setup(
    name="ndpath",
    version="1.0.0",
    py_modules=["ndpath"],
    include_package_data=True,
    install_requires=[
        "rich",
        "readchar",
    ],
    entry_points={
        "console_scripts": [
            "ndpath = ndpath:main",
        ],
    },
)
