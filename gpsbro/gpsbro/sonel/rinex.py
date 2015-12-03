import sys
import random
import datetime

import requests
import urllib.request
from xml.etree import ElementTree

from gpsbro.unavco import zones

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
    BASE_URL = "ftp://ftp.sonel.org/gps/data/"
    mZ = list()
    nZ = list()
    dZ = list()
    qc = list()
    filters = list()
    if mask & MET:
        filters.append("met/")
    if mask & NAV:
        filters.append("nav/")
    if mask & OBS:
        filters.append("obs/")
    if mask & QC:
        filters.append("qc/")
    for f in filters:
        URL = BASE_URL
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

SAMPLE_TYPES = set([
    "DAY",
])

def get_URLs_within(start_date, end_date, mask=None, sample_size=None, sample_type=None, zone=None):

    mask = mask if mask is not None else DEFAULT_MASK
    domain = [end_date - datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

    # Set up the domain and handle errors
    if sample_size is not None:
        if sample_type is not None:
            if (type(sample_type) is not str) or \
               sample_type not in SAMPLE_TYPES:
                print("Invalid sample type. Valid options are")
                for t in SAMPLE_TYPES:
                    print(t)
                raise ValueError
            else:
                if sample_type == "DAY":
                    if (not type(sample_size) is int) or \
                       (not sample_size <= (end_date - start_date).days + 1) or \
                       (not sample_size >= 0):
                        print("Invalid sample size. Sample size must meet the following conditions")
                        print("1) sample_size must be of type 'int'")
                        print("2) sample_size must be less than or equal to the number of days within the specified date range")
                        print("3) sample_size must be greater than or equal to zero")
                        raise ValueError
                    else:
                        domain = random.sample(domain, sample_size)
        else:
            print("To use the sample_size keyword argument, you must specify a sample type. Valid options are")
            for t in SAMPLE_TYPES:
                print(t)
            raise ValueError

    dates = dict()
    for date in domain:
        try:
            if zone is not None:
                if zone not in zones.zones.keys():
                    print("Invalid zone. Valid options are")
                    for zone in zones.zones.keys():
                        print(zone)
                    raise ValueError
                else:
                    container = list()
                    for _tuple_ in get_URLs_on(date, mask):
                        _tuple_ = [str(url) if (url is not None) and ((url[48] == "/" and (str(url[49:53]) in zones.zones[zone])) or (url[47] == "/" and (str(url[48:52]) in zones.zones[zone]))) else None for url in _tuple_]
                        if any(_tuple_):
                            container.append(_tuple_)
                    dates[date] = container
            else:
                dates[date] = get_URLs_on(date, mask)
        except Exception as e:
            print("Could not find URL for {0}".format(date.strftime("%Y-%m-%d")))
            print(e)

    return dates
