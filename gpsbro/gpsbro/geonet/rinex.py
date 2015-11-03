import datetime
import requests
import sys
import urllib.request
from xml.etree import ElementTree

def get_URLs_on(date):
    day_string = str(date.timetuple().tm_yday)
    while len(day_string) < 3:
        day_string = "0" + day_string
    date_url = date.strftime("%Y/") + day_string + "/"
    URL = "ftp://ftp.geonet.org.nz/gps/rinex/"
    mZ = list()
    dZ = list()
    qc = list()
    with urllib.request.urlopen(URL + date_url) as response:
        data = response.read().decode("utf-8")
        for line in data.split("\n"):
            if not line.strip().split():
                continue
            string = line.strip().split()[-1]
            if len(string) > 3:
                if string[-3:] == "m.Z":
                    mZ.append(URL + date_url + string)
                elif string[-3:] == "d.Z":
                    dZ.append(URL + date_url + string)
                elif string[-3:] == ".qc":
                    qc.append(URL + date_url + string)
    maximum_len = max(len(mZ), len(dZ), len(qc))
    mZ.extend([None]*(maximum_len - len(mZ)))
    dZ.extend([None]*(maximum_len - len(dZ)))
    qc.extend([None]*(maximum_len - len(qc)))
    return zip(mZ, dZ, qc)

def get_URLs_within(start_date, end_date):
    dates = dict()
    for date in [end_date - datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]:
        try:
            dates[date] = get_URLs_on(date)
        except Exception as e:
            print("Could not find URL for {0}".format(date.strftime("%Y-%m-%d")))
            print(e)
    return dates
