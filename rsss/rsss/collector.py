import requests
from xml.etree import ElementTree

from rsss.geonetmark import GeoNetMark

class Collector:

    DEFAULT_GEONET_MARK_START_DATE = "1900-01-01" # YYYY-MM-DD
    DEFAULT_GEONET_MARK_END_DATE   = "2100-12-31"

    @staticmethod
    def get_geonet_marks(mark_type, status, start_date=None, end_date=None):
        ## GeoNet Website: http://geonet.org.nz/
        
        start_date = start_date if start_date is not None else Collector.DEFAULT_GEONET_MARK_START_DATE
        end_date = end_date if end_date is not None else Collector.DEFAULT_GEONET_MARK_END_DATE

        payload = {
            "type": mark_type,
            "status": status,
            "startDate": start_date,
            "endDate": end_date,
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
        return geonet_marks
