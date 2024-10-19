from setuptools import setup

setup(
    name="ETLpipeline",
    version="0.1.0",
    description="ETL and Query pipeline CLI tool",
    author="Nakiyah Dhariwala",
    author_email="nakiyah.dhariwala@duke.edu",
    py_modules=["etl_query_pipeline"],  # Replace with the correct module/file name
    install_requires=[
        "databricks-sql-connector",  # Handles the connection to Databricks SQL
        "pandas",                    # For data manipulation and transformation
        "python-dotenv",             # For environment variable management
    ],
    entry_points={
        "console_scripts": [
            "etl_query=etl_query_pipeline:main",  # Link to the main function in your Python script
        ],
    },
)
