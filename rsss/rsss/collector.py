import requests
from xml.etree import ElementTree

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
        print(response.text)
