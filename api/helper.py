import urllib3
import requests
from api.constant import THREADS


terget = "thewatchcode.com"


def get_sub_domain(terget):
    subdomains = []

    """
    This function does the following things:
    - Opens a file and reads all the subdomains to be added to the target domain eg mail.example.com
    - send GET requests to the target domain and subdomains to test if they exist
    """
    with open("api/files/sub.txt", "r") as c:
        sub = c.read()

    for line in sub.split("\n"):

        try:
            http = urllib3.PoolManager(
                num_pools=THREADS,
                maxsize=50,
                block=True,
                timeout=urllib3.Timeout(connect=1.0, read=2.0),
            )

            r = http.request("GET", "https://" + line + "." + terget, retries=False)
            url = line + "." + terget

            if r.status == 200:
                subdomains.append(url)

            elif r.status == 404:
                pass

        except Exception as e:
            pass

    return subdomains
