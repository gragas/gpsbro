from rsss.geonetmark import GeoNetMark
from rsss.collector import Collector

def main():
    geonet_marks1 = Collector.get_geonet_marks("tsunami", "operational", lon_bounds=(-170, -180))
    for mark in geonet_marks1:
        print(mark)

if __name__ == "__main__":
    main()
