import datetime
from time import time

import gpsbro.sonel.rinex
#import gpsbro.sonel.marks

def main():

    ### Get SONEL rinex URLs in a range of dates (inclusive) demonstration


    test_one_begin = time()
    start_date = datetime.date(2015, 1, 12)
    end_date   = datetime.date(2015, 1, 13)
    dates = gpsbro.sonel.rinex.get_URLs_within(start_date, end_date, sample_size=2, sample_type="DAY",)
    for date in dates:
        mZ_files = [mZ for mZ, dZ, qc in dates[date] if mZ is not None]
        dZ_files = [dZ for mZ, dZ, qc in dates[date] if dZ is not None]
        qc_files = [qc for mZ, dZ, qc in dates[date] if qc is not None]
        print("Found {0} files on {1}.".format(len(mZ_files) + len(dZ_files) + len(qc_files), date.strftime("%Y-%m-%d")))
    test_one_end = time()
    print("Time elapsed: {} seconds".format(str(test_one_end - test_one_begin)))
    #return

    ##########################################

    ### Get SONEL rinex URLs on a specific date demonstration

    d = datetime.date(2015, 10, 12)
    URLs = gpsbro.sonel.rinex.get_URLs_on(d, mask=gpsbro.sonel.rinex.OBS)
    print("First 5 RINEX observation URLs on {0}:".format(date.strftime("%Y-%m-%d")))
    for url in URLs[:5]:
        print(url)
    return

    ###########################################

    ### Hashable and equivalence demonstration

    sonel_marks1 = gpsbro.sonel.marks.get_sonel_marks("tsunami", "operational", lon_bounds=(-170, -180))
    print("sonel_marks1 ({0}):\n".format(len(sonel_marks1)))
    for mark in sonel_marks1:
        print(mark)
    print()
    sonel_marks2 = gpsbro.sonel.marks.get_sonel_marks("tsunami", "operational", lon_bounds=(175, 177))
    print("sonel_marks2 ({0}):\n".format(len(sonel_marks2)))
    for mark in sonel_marks2:
        print(mark)
    print()
    sonel_marks3 = sonel_marks1 + sonel_marks2
    print("sonel_marks3 ({0}):\n".format(len(sonel_marks3)))
    for mark in sonel_marks3:
        print(mark)
    print()
    sonel_marks4 = list(set(sonel_marks3) - set(sonel_marks2))
    print("sonel_marks4 ({0}):\n".format(len(sonel_marks4)))
    for mark in sonel_marks4:
        print(mark)
    print()

    #############################################

if __name__ == "__main__":
    main()
