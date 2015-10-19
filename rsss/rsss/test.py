import datetime

from rsss.geonetmark import GeoNetMark
from rsss.collector import Collector

def main():

    ### Get GeoNet rinex URLs in a range of dates (inclusive) demonstration

    start_date = datetime.date(2015, 10, 12)
    end_date   = datetime.date(2015, 10, 14)
    dates = Collector.get_geonet_rinex_URLs_within(start_date, end_date) # 3 dates
    for date in dates:
        Z_files = [Z for Z, qc in dates[date]]
        qc_files = [qc for Z, qc in dates[date]]
        print("Found {0} .Z files on {1}.".format(len(Z_files), date.strftime("%Y-%m-%d")))
    return

    ##########################################

    ### Get GeoNet rinex URLs on a specific date demonstration

    URLs = Collector.get_geonet_rinex_URLs_on(datetime.date(2015, 11, 12))
    Z_files = [Z for Z, qc in URLs]
    qc_files = [qc for Z, qc in URLs]
    print(Z_files)
    return

    ###########################################

    ### Hashable and equivalence demonstration

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

    #############################################

if __name__ == "__main__":
    main()
