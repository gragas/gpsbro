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

    def within(self, lat_bounds, lon_bounds):
        ## The bounds in this method do NOT wrap.
        #  e.g., if a mark is located at -175 and
        #  this method is called witht eh arguments
        #  lat_bounds=(-90, 90) and lon_bounds=(170, -170),
        #  the method will return False. This is because
        #  the logic of the expression returned determines
        #  if this GeoNetMark is between the min and max of
        #  of the bounds (in this case -170 and 170). Since
        #  -175 is not within these bounds, it will return
        #  False. In order to get wrap functionality, consider
        #  unioning two sets of marks within the bounds, for
        #  example, (170, 180) and (-180, -170).
        assert(len(lat_bounds) == 2 and len(lon_bounds) == 2)
        lat_min = min(lat_bounds)
        lat_max = max(lat_bounds)
        assert(lat_min >= -90.0 and lat_max <= 90.0)
        lon_min = min(lon_bounds)
        lon_max = max(lon_bounds)
        assert(lon_min >= -180.0 and lon_max <= 180.0)
        return self.lat >= lat_min and self.lat <= lat_max and self.lon >= lon_min and self.lon <= lon_max

    def __eq__(self, other):
        if type(other) == GeoNetMark:
            return other.code == self.code and other.mark_type == self.mark_type and other.network == self.network
        return False

    def __hash__(self):
        return hash("{0} {1} {2}".format(self.code, self.mark_type, self.network))

    def __str__(self):
        ## This method allows for easy printing of GeoNetMarks.
        #  To use it, simply call print(some_geonet_mark)
        string = "GeoNetMark(\n\tmark_type={0},\n\tstatus={1},\n\tcode={2}," + \
                 "\n\tname={3},\n\tlat={4},\n\tlon={5},\n\topen_date={6}," + \
                 "\n\tnetwork={7}"
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
