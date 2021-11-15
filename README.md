# input-podaac

Organizes input operations needed to extract and store SWOT shapefiles hosted by PO.DAAC in an S3 bucket. The operations currently retrieve a list of files based on short name and observation time listed in the name of the collection files.

**TODO**
- Integrate into input module operations.

# installation

1. Clone the repository to your file system.
2. extract is best run with Python virtual environments so install venv and create a virutal environment: https://docs.python.org/3/library/venv.html
3. Activate the virtual environment and use pip to install dependencies: `pip install -r requirements.txt`

**Note: Requires third-party libraries: 's3fs' and 'requests'.**

# execution

1. Activate your virtual environment.
2. Run `python3 retrieve_data.py` 