# Standard imports
from http.cookiejar import CookieJar
import netrc
from urllib import request

# Third-party imports
import requests
import s3fs

PODAAC_S3 = "https://archive.podaac.earthdata.nasa.gov/s3credentials"
URS = "urs.earthdata.nasa.gov"

def login():
    """Log into Earthdata and set up request library to track cookies."""

    # Obtain credentials
    try:
        username, _, password = netrc.netrc().authenticators(URS)
    except (FileNotFoundError, TypeError):
        print("There's no .netrc file or the the endpoint isn't in the netrc file")
        print("See: https://github.com/podaac/sentinel6#note-1-netrc-file")

    # Create Earthdata authentication request
    manager = request.HTTPPasswordMgrWithDefaultRealm()
    manager.add_password(None, URS, username, password)
    auth = request.HTTPBasicAuthHandler(manager)

    # Set up the storage of cookies
    jar = CookieJar()
    processor = request.HTTPCookieProcessor(jar)

    # Define an opener to handle fetching auth request
    opener = request.build_opener(auth, processor)
    request.install_opener(opener)

def get_s3():
    """Requests and S3 token and returns a reference to the S3 bucket.

    Returns
    -------
    S3FileSystem
    """

    response = requests.get(PODAAC_S3).json()
    return s3fs.S3FileSystem(key=response["accessKeyId"],
                                     secret=response["secretAccessKey"],
                                     token=response["sessionToken"],
                                     client_kwargs={"region_name": "us-west-2"})

def retrieve_files(s3, short_name, date_str):
    """Retrieve a list of files from S3 bucket.
    
    Parameters
    ----------
    s3: S3FileSystem
        reference to S3 bucket to retrieve data from
    short_name:
        string short name of collection
    date_str: str
        string date and time to search for
        
    Returns
    -------
    list: list of strings
    """
    
    files = s3.glob(f"podaac-ops-cumulus-protected/{short_name}/{date_str}*.nc")
    return files

def main():

    login()
    
    s3 = get_s3()

    short_name = "VIIRS_N20-OSPO-L2P-v2.61"
    date_str = "20211115"
    files = retrieve_files(s3, short_name, date_str)
    

if __name__ == "__main__":
    main()