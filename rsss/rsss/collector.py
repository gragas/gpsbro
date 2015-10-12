import requests

class Collector:
    @staticmethod
    def getGeoNetMarks(mark_type, status, start_date, end_date):
        ## GeoNet Website: http://geonet.org.nz/
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
