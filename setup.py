from setuptools import setup, find_packages

setup(
    name="financial_data_parser",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "openpyxl",
        "numpy",
        "python-dateutil",
    ],
    entry_points={
        "console_scripts": [
            "run-parser = main:main"
        ]
    },
    python_requires=">=3.7",
)
