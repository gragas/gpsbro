import datetime
import requests
import sys
import urllib.request
from xml.etree import ElementTree

from rsss.geonetmark import GeoNetMark

class Collector:

    @staticmethod
    def get_geonet_rinex_URLs_within(start_date, end_date):
        dates = dict()
        for date in [end_date - datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]:
            try:
                dates[date] = Collector.get_geonet_rinex_URLs_on(date)
            except:
                print("Could not find URL for {0}".format(date.strftime("%Y-%m-%d")))
        return dates

    @staticmethod
    def get_geonet_rinex_URLs_on(date):
        date_url = date.strftime("%Y/") + str(date.timetuple().tm_yday) + "/"
        URL = "ftp://ftp.geonet.org.nz/gps/rinex/"
        URLs = list()
        with urllib.request.urlopen(URL + date_url) as response:
            data = response.read().decode("utf-8")
            Z = None
            qc = None
            for indx, line in enumerate(data.split("\n")):
                if line.strip().split():
                    if indx % 2 == 0:
                        Z = line.strip().split()[-1]
                    else:
                        qc = line.strip().split()[-1]
                        URLs.append((URL + date_url + Z, URL + date_url + qc))
        return URLs

    DEFAULT_GEONET_RINEX_LAT_BOUNDS = (-90.0, 90.0)
    DEFAULT_GEONET_RINEX_LON_BOUNDS = (-180.0, 180.0)

    @staticmethod
    def get_geonet_rinex(start_date, end_date, lat_bounds=None, lon_bounds=None):

        lat_bounds = lat_bounds if lat_bounds is not None else Collector.DEFAULT_GEONET_RINEX_LAT_BOUNDS
        lon_bounds = lon_bounds if lon_bounds is not None else Collector.DEFAULT_GEONET_RINEX_LON_BOUNDS

        start_date_url = start_date.strftime("%Y/") + str(start_date.timetuple().tm_yday) + "/"
        
        URL = "ftp://ftp.geonet.org.nz/gps/rinex/"
        with urllib.request.urlopen(URL + start_date_url) as response:
            data = response.read().decode("utf-8")
            for line in data.split("\n"):
                string = line.strip().split()[-1][:4]
                print(string)
        # INCOMPLETE
        

    DEFAULT_GEONET_MARK_START_DATE = datetime.date(1900, 1, 1) # YYYY-MM-DD
    DEFAULT_GEONET_MARK_END_DATE   = datetime.date(2100, 12, 31)
    DEFAULT_GEONET_MARK_LAT_BOUNDS = (-90.0, 90.0)
    DEFAULT_GEONET_MARK_LON_BOUNDS = (-180.0, 180.0)

    @staticmethod
    def get_geonet_marks(mark_type, status, start_date=None, end_date=None, lat_bounds=None, lon_bounds=None):
        ## GeoNet Website: http://geonet.org.nz/
        
        start_date = start_date if start_date is not None else Collector.DEFAULT_GEONET_MARK_START_DATE
        end_date   = end_date if end_date is not None else Collector.DEFAULT_GEONET_MARK_END_DATE
        lat_bounds = lat_bounds if lat_bounds is not None else Collector.DEFAULT_GEONET_MARK_LAT_BOUNDS
        lon_bounds = lon_bounds if lon_bounds is not None else Collector.DEFAULT_GEONET_MARK_LON_BOUNDS
        
        payload = {
            "type": mark_type,
            "status": status,
            "startDate": start_date.strftime("%Y-%m-%d"),
            "endDate": end_date.strftime("%Y-%m-%d"),
        }
        ## by ommitting the outputFormat argument, the output format
        # will be XML
        
        URL = "http://magma.geonet.org.nz/ws-delta/site"
        response = requests.get(URL, params=payload)

        geonet_marks = list()

        root = ElementTree.fromstring(response.content)
        for station in root:
            code = None
            name = None
            lat = None
            lon = None
            open_date = None
            network = None
            for key in station.attrib.keys():
                if key == "code":
                    code = station.attrib[key]
                elif key == "name":
                    name = station.attrib[key]
                elif key == "lat":
                    lat = float(station.attrib[key])
                elif key == "lon":
                    lon = float(station.attrib[key])
                elif key == "opened":
                    open_date = station.attrib[key]
                elif key == "network":
                    network = station.attrib[key]
            assert(mark_type is not None)
            assert(status is not None)
            assert(code is not None)
            assert(name is not None)
            assert(lat is not None)
            assert(lon is not None)
            assert(open_date is not None)
            assert(network is not None)
            geonet_marks.append(GeoNetMark(mark_type, status, code, name, lat, lon, open_date, network))

        geonet_marks = [mark for mark in geonet_marks if mark.within(lat_bounds, lon_bounds)]
        
        return geonet_marks
