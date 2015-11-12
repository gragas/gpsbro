import datetime
from time import time

import gpsbro.geonet.rinex
import gpsbro.geonet.marks

def main():

    ### Get GeoNet rinex URLs in a range of dates (inclusive) demonstration

    test_one_begin = time()
    start_date = datetime.date(2015, 1, 12)
    end_date   = datetime.date(2015, 2, 12)
    dates = gpsbro.geonet.rinex.get_URLs_within(start_date, end_date, sample_size=2)
    for date in dates:
        mZ_files = [mZ for mZ, dZ, qc in dates[date]]
        dZ_files = [dZ for mZ, dZ, qc in dates[date]]
        qc_files = [qc for mZ, dZ, qc in dates[date]]
        print("Found {0} *m.Z files on {1}.".format(len(mZ_files), date.strftime("%Y-%m-%d")))
    test_one_end = time()
    print("Time elapsed: {} seconds".format(str(test_one_end - test_one_begin)))
    #return

    ##########################################

    ### Get GeoNet rinex URLs on a specific date demonstration

    d = datetime.date(2015, 10, 12)
    URLs = gpsbro.geonet.rinex.get_URLs_on(d, mask=gpsbro.geonet.rinex.OBS)
    print("First 5 RINEX observation URLs on {0}:".format(date.strftime("%Y-%m-%d")))
    for url in URLs[:5]:
        print(url)
    return

    ###########################################

    ### Hashable and equivalence demonstration

    geonet_marks1 = gpsbro.geonet.marks.get_geonet_marks("tsunami", "operational", lon_bounds=(-170, -180))
    print("geonet_marks1 ({0}):\n".format(len(geonet_marks1)))
    for mark in geonet_marks1:
        print(mark)
    print()
    geonet_marks2 = gpsbro.geonet.marks.get_geonet_marks("tsunami", "operational", lon_bounds=(175, 177))
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
