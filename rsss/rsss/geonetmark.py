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
        assert(type(self.lat) == float)
        self.lon = lon
        assert(type(self.lon) == float)
        self.open_date = open_date
        self.network = network

    def __str__(self):
        string = "GeoNetMark(\n\tmark_type={0},\n\tstatus={1},\n\tcode={2}," + \
                 "\n\tname={3},\n\tlat={4},\n\tlon={5},\n\topen_date={6}," + \
                 "\n\tnetwork{7}"
        return string.format(
            self.mark_type,
            self.status,
            self.code,
            self.name,
            self.lat,
            self.lon,
            self.open_date,
            self.network,
        )
