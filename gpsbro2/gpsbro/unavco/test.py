import datetime
from time import time

import gpsbro.unavco.rinex
#import gpsbro.unavco.marks

def main():

    ### Get Unavco rinex URLs in a range of dates (inclusive) demonstration


    test_one_begin = time()
    start_date = datetime.date(2015, 1, 12)
    end_date   = datetime.date(2015, 1, 14)
    dates = gpsbro.unavco.rinex.get_URLs_within(start_date, end_date)
    for date in dates:
        mZ_files = [mZ for mZ, dZ, qc in dates[date]]
        dZ_files = [dZ for mZ, dZ, qc in dates[date]]
        qc_files = [qc for mZ, dZ, qc in dates[date]]
        print("Found {0} *m.Z files on {1}.".format(len(mZ_files), date.strftime("%Y-%m-%d")))
    test_one_end = time()
    print("Time elapsed: {} seconds".format(str(test_one_end - test_one_begin)))
    #return

    ##########################################

    ### Get Unavco rinex URLs on a specific date demonstration

    d = datetime.date(2015, 10, 12)
    URLs = gpsbro.unavco.rinex.get_URLs_on(d, mask=gpsbro.unavco.rinex.OBS)
    print("First 5 RINEX observation URLs on {0}:".format(date.strftime("%Y-%m-%d")))
    for url in URLs[:5]:
        print(url)
    return

    ###########################################

    ### Hashable and equivalence demonstration

    unavco_marks1 = gpsbro.unavco.marks.get_unavco_marks("tsunami", "operational", lon_bounds=(-170, -180))
    print("unavco_marks1 ({0}):\n".format(len(unavco_marks1)))
    for mark in unavco_marks1:
        print(mark)
    print()
    unavco_marks2 = gpsbro.unavco.marks.get_unavco_marks("tsunami", "operational", lon_bounds=(175, 177))
    print("unavco_marks2 ({0}):\n".format(len(unavco_marks2)))
    for mark in unavco_marks2:
        print(mark)
    print()
    unavco_marks3 = unavco_marks1 + unavco_marks2
    print("unavco_marks3 ({0}):\n".format(len(unavco_marks3)))
    for mark in unavco_marks3:
        print(mark)
    print()
    unavco_marks4 = list(set(unavco_marks3) - set(unavco_marks2))
    print("unavco_marks4 ({0}):\n".format(len(unavco_marks4)))
    for mark in unavco_marks4:
        print(mark)
    print()

    #############################################

if __name__ == "__main__":
    main()
