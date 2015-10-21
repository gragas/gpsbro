# RSSS Toolkit

RSSS Toolkit helps scientists gather and parse information from certain RSSS-related networks.

# Installation

The installation process for RSSS-toolkit varies depending on which version of Python you're using. I highly recommend users install [pip](http://pip.readthedocs.org/en/stable/installing/) first. I also highly recommend running RSSS-toolkit on Python 3, as it depends on the least deprecated modules.

## Requirements

As of yet, RSSS-toolkit only requires the [requests](http://docs.python-requests.org/en/latest/) package. The easiest way to install requests is via [pip](http://pip.readthedocs.org/en/stable/installing/):

```
sudo pip install requests
```

## Python 2.x

If you're using Python 2.x, run the following commands:

```
git clone https://github.com/gragas/RSSS-toolkit
cd RSSS-toolkit/rsss2/ # notice the 2
sudo python setup.py develop
# To be explicit about installing RSSS-toolkit to
# Python 2 instead of 3, run "sudo python2 setup.py develop"
```

If the installation failed, or doesn't work correctly, run the following command:

```
# After you've nagivated back to RSSS-toolkit/rsss2/,
sudo python setup.py install
```

## Python 3+

Run these commands:

```
git clone https://github.com/gragas/RSSS-toolkit
cd RSSS-toolkit/rsss/
sudo python setup.py develop
# To be explicit about installing RSSS-toolkit to
# Python 3 instead of 2, run "sudo python3 setup.py develop"
```

If the installation failed, or doesn't work correctly, run the following command instead:

```
# After you've nagivated back to RSSS-toolkit/rsss2/,
sudo python setup.py install
```

# Usage

It's easy to get GeoNet rinex URLs with RSSS-toolkit:

```
    # import datetime
    import rsss.geonet.rinex
    URLs = rsss.geonet.rinex.get_URLs_on(datetime.date(2015, 10, 12))
    mZ_files = [mZ for mZ, dZ, qc in URLs]   # list of m.Z URLs
    dZ_files = [dZ for mZ, dZ, qc in URLs]   # list of d.Z URLs
    qc_files = [qc for mZ, dZ, qc in URLs]   # list of .qc URLs
```

Or, grab all the rinex URLs within a range of dates:

```
    start_date = datetime.date(2015, 10, 12)
    end_date   = datetime.date(2015, 10, 14)
    dates = rsss.geonet.rinex.get_URLs_within(start_date, end_date) # 3 dates
    for date in dates:
        mZ_files = [mZ for mZ, dZ, qc in dates[date]]   # list of m.Z URLs
        dZ_files = [dZ for mZ, dZ, qc in dates[date]]   # list of d.Z URLs
        qc_files = [qc for mZ, dZ, qc in dates[date]]   # list of .qc URLs
        print("Found {0} d.Z files on {1}.".format(len(dZ_files), date.strftime("%Y-%m-%d")))
```

# License and Redistribution

This project is licensed under the MIT License. Feel free to contribute to or fork this project.

# Original Author

Thomas Fischer
