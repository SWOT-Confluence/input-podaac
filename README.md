# input-podaac

Organizes input operations needed to locate SWOT shapefiles hosted by PO.DAAC in an S3 bucket. The operations currently retrieve a list of files based on short name and a temporal range and output a JSON file list of S3 URIs.

**TODO**
- Integrate into input module operations.

# installation

1. Clone the repository to your file system.
2. extract is best run with Python virtual environments so install venv and create a virutal environment: https://docs.python.org/3/library/venv.html
3. Activate the virtual environment and use pip to install dependencies: `pip install -r requirements.txt`

**Note: Requires third-party libraries: 's3fs' and 'requests'.**

# execution

1. Activate your virtual environment.
2. Run `python3 S3List_run.py  -s SWOT_SIMULATED_NA_CONTINENT_L2_HR_RIVERSP_V1 -t 2022-08-01T00:00:00Z,2022-08-22T23:59:59Z -d /Users/username/s3_lists` 