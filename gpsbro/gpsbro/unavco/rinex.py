import datetime
import requests
import sys
import urllib.request
from xml.etree import ElementTree

MET = 0b0001
NAV = 0b0010
OBS = 0b0100
QC  = 0b1000

DEFAULT_MASK = MET | OBS | QC

def get_URLs_on(date, mask=None):
    mask = mask if mask is not None else DEFAULT_MASK
    day_string = str(date.timetuple().tm_yday)
    while len(day_string) < 3:
        day_string = "0" + day_string
    date_url = date.strftime("%Y/") + day_string + "/"
    BASE_URL = "ftp://data-out.unavco.org/pub/rinex/"
    mZ = list()
    nZ = list()
    dZ = list()
    qc = list()
    directories = list()
    if mask & MET:
        directories.append("met/")
    if mask & NAV:
        directories.append("nav/")
    if mask & OBS:
        directories.append("obs/")
    if mask & QC:
        directories.append("qc/")
    for d in directories:
        URL = BASE_URL + d
        with urllib.request.urlopen(URL + date_url) as response:
            data = response.read().decode("utf-8")
            for line in data.split("\n"):
                if not line.strip().split():
                    continue
                string = line.strip().split()[-1]
                if len(string) > 3:
                    # hashtag robust
                    if string[-3:] == "m.Z":
                        mZ.append(URL + date_url + string)
                    elif string[-3:] == "n.Z":
                        nZ.append(URL + date_url + string)
                    elif string[-3:] == "d.Z":
                        dZ.append(URL + date_url + string)
                    elif string[-3:] == ".qc":
                        qc.append(URL + date_url + string)
    maximum_len = max(len(mZ), len(nZ), len(dZ), len(qc))
    mZ.extend([None]*(maximum_len - len(mZ)))
    nZ.extend([None]*(maximum_len - len(nZ)))
    dZ.extend([None]*(maximum_len - len(dZ)))
    qc.extend([None]*(maximum_len - len(qc)))
    base = list()
    if mask & MET:
        base = mZ
    if mask & NAV:
        if not len(base):
            base = nZ
        else:
            for indx, e in enumerate(base):
                if type(e) is list:
                    base[indx] = e + [nZ[indx]]
                else:
                    base[indx] = [e] + [nZ[indx]]
    if mask & OBS:
        if not len(base):
            base = dZ
        else:
            for indx, e in enumerate(base):
                if type(e) is list:
                    base[indx] = e + [dz[indx]]
                else:
                    base[indx] = [e] + [dZ[indx]]
    if mask & QC:
        if not len(base):
            base = qc
        else:
            for indx, e in enumerate(base):
                if type(e) is list:
                    base[indx] = e + [qc[indx]]
                else:
                    base[indx] = [e] + [qc[indx]]
    return base

def get_URLs_within(start_date, end_date, mask=None):
    mask = mask if mask is not None else DEFAULT_MASK
    dates = dict()
    for date in [end_date - datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]:
        try:
            dates[date] = get_URLs_on(date, mask)
        except Exception as e:
            print("Could not find URL for {0}".format(date.strftime("%Y-%m-%d")))
            print(e)
    return dates
