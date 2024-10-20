from setuptools import setup, find_packages

setup(
    name="ETLpipeline",
    version="0.1.0",
    description="ETL and Query pipeline CLI tool",
    author="Nakiyah Dhariwala",
    author_email="nakiyah.dhariwala@duke.edu",
    packages=find_packages(),  # Automatically find all packages and sub-packages
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=etl_query_pipeline:main",
        ],
    },
)
