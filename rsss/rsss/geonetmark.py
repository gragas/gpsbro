class GeoNetMark:
    def __init__(self, mark_type, status, code, name, lat, lon, open_date, network):
        ## http://info.geonet.org.nz/display/equip/Network+Location+Queries
        self.mark_type = mark_type
        assert (self.mark_type == "cgps" or
                self.mark_type == "seismicSite" or
                self.mark_type == "seismicStation" or
                self.mark_type == "tsunami")
        self.status = status
        assert (self.status == "operational" or
                self.status == "complete" or
                self.status == "permitted" or
                self.status == "suitable" or
                self.status == "possible" or
                self.status == "temporary" or
                self.status == "closed" or
                self.status == "abandoned" or
                self.status == "todo" or
                self.status == "not provided")
        ## "todo" includes all of complete, permitted, possible and suitable
        ## "not provided" is not a valid status for GeoNet queries; it is
        # explicitly passed to this constructor when no status is provided
        # for a query
        self.code = code
        self.name = name
        self.lat = lat
        self.lon = lon
        self.open_date = open_date
        self.network = network
