import datetime

from rsss.geonetmark import GeoNetMark
from rsss.collector import Collector

def main():

    URLs = Collector.get_geonet_rinex_URLs(datetime.date(2015, 10, 12))
    Z_files = [Z for Z, qc in URLs]
    qc_files = [qc for Z, qc in URLs]
    print(Z_files)
    return

    geonet_marks1 = Collector.get_geonet_marks("tsunami", "operational", lon_bounds=(-170, -180))
    print("geonet_marks1 ({0}):\n".format(len(geonet_marks1)))
    for mark in geonet_marks1:
        print(mark)
    print()
    geonet_marks2 = Collector.get_geonet_marks("tsunami", "operational", lon_bounds=(175, 177))
    print("geonet_marks2 ({0}):\n".format(len(geonet_marks2)))
    for mark in geonet_marks2:
        print(mark)
    print()
    geonet_marks3 = geonet_marks1 + geonet_marks2
    print("geonet_marks3 ({0}):\n".format(len(geonet_marks3)))
    for mark in geonet_marks3:
        print(mark)
    print()
    geonet_marks4 = list(set(geonet_marks3) - set(geonet_marks2))
    print("geonet_marks4 ({0}):\n".format(len(geonet_marks4)))
    for mark in geonet_marks4:
        print(mark)
    print()

if __name__ == "__main__":
    main()
