# GPSbro

GPSbro helps scientists gather and parse information from certain networks.

# Installation

The installation process for gpsbro varies depending on which version of Python you're using. I highly recommend users install [pip](http://pip.readthedocs.org/en/stable/installing/) first. I also highly recommend running gpsbro on Python 3, as it depends on the least deprecated modules.

## Requirements

As of yet, gpsbro only requires the [requests](http://docs.python-requests.org/en/latest/) package. The easiest way to install requests is via [pip](http://pip.readthedocs.org/en/stable/installing/):

```
sudo pip install requests
```

## Python 2.x

If you're using Python 2.x, run the following commands:

```
git clone https://github.com/gragas/gpsbro
cd gpsbro/gpsbro2/ # notice the 2
sudo python setup.py develop
# To be explicit about installing gpsbro to
# Python 2 instead of 3, run "sudo python2 setup.py develop"
```

If the installation failed, or doesn't work correctly, run the following command:

```
# After you've nagivated back to gpsbro/gpsbro2/,
sudo python setup.py install
```

## Python 3+

Run these commands:

```
git clone https://github.com/gragas/gpsbro
cd gpsbro/gpsbro/
sudo python setup.py develop
# To be explicit about installing gpsbro to
# Python 3 instead of 2, run "sudo python3 setup.py develop"
```

If the installation failed, or doesn't work correctly, run the following command instead:

```
# After you've nagivated back to gpsbro/gpsbro/,
sudo python setup.py install
```

# Usage

It's easy to get UNAVCO RINEX URLs with gpsbro:

```
import datetime
import gpsbro.unavco.rinex
URLs = gpsbro.unavco.rinex.get_URLs_on(
    datetime.date(2015, 10, 12),
    mask=gpsbro.unavco.rinex.OBS # Get *d.Z files
)
```

Or, grab all the rinex URLs within a range of dates:

```
start_date = datetime.date(2015, 10, 12)
end_date   = datetime.date(2015, 10, 14)
dates = gpsbro.geonet.rinex.get_URLs_within(start_date, end_date)
for date in dates: # 12th, 13th, and 14th
    mZ_files = [mZ for mZ, dZ, qc in dates[date]]   # list of *m.Z URLs
    dZ_files = [dZ for mZ, dZ, qc in dates[date]]   # list of *d.Z URLs
    qc_files = [qc for mZ, dZ, qc in dates[date]]   # list of *.qc URLs
    print("Found {0} d.Z files on {1}.".format(len(dZ_files), date.strftime("%Y-%m-%d")))
```

# Masking

You probably know that there are many different types of RINEX files. You can use the `mask` keyword argument to get specific file types. Four constants are provided for use with the UNAVCO and GeoNet networks:

```
MET # *m.Z --- Meteorological
NAV # *n.Z --- Navigational
OBS # *d.Z --- Observational
QC  # *.qc --- qc
```

You can form a mask by logical-anding these constants. Then, pass the mask to a function. For example,

```
# Only get meteorological, navigational, and observational files. Don't get *.qc files.
mask = gpsbro.unavco.rinex.MET | gpsbro.unavco.rinex.NAV | gpsbro.unavco.rinex.NAV

start_date = datetime.date(2015, 10, 12)
end_date   = datetime.date(2015, 10, 14)
dates = gpsbro.unavco.rinex.get_URLs_within(start_date, end_date, mask)
# - dates is a list of lists
# - each list contains URLs
# - the lists in dates are ordered alphabetically (as displayed above)
#    - Examples:
#       - if mask = MET | OBS then dates = [ MET_list, OBS_list ]
#       - if mask = NAV | QC  then dates = [ NAV_list, QC_list ]

for date in dates: # 12th, 13th, and 14th
    mZ_files = [mZ for mZ, nZ, dZ in dates[date]]   # list of meteorological -- *m.Z URLs
    nZ_files = [nZ for mZ, nZ, dZ in dates[date]]   # list of navigational   -- *n.Z URLs
    dZ_files = [dZ for mZ, nZ, dZ in dates[date]]   # list of observational  -- *d.Z URLs
```

# Random Sampling

It can take a long time to get hundreds of thousands of URLs. Random sampling and statistics can mitigate the need to get data every URL. To get a random sample of URLs within a certain range, just add the `sample_size` keyword argument to your `*.rinex.get_URLs_within` function call. For example:

```
start_date = datetime.date(2015, 10, 12)
end_date   = datetime.date(2014, 10, 12)
dates = gpsbro.unavco.rinex.get_URLs_within(start_date, end_date, mask, sample_size=35)

# sample_size=35: randomly choose 35 days and only get URLs for those days

for date in dates:
    mZ_files = [mZ for mZ, dZ, qc in dates[date]]   # list of meteorological -- *m.Z URLs
    dZ_files = [dZ for mZ, dZ, qc in dates[date]]   # list of observational  -- *d.Z URLs
    qc_files = [qc for mZ, dZ, qc in dates[date]]   # list of *.qc URLs
```

# Latitude/Longitude Bounding

Latitude/Longitude bounding is not currenlty implemented for any network. However, certained zones have been cached for the UNAVCO network. The only zone that has been cached so far is the `HAWAII` zone. You can filter URLs to only include sites within this zone by setting the `zone` keyword argument to `"HAWAII"`. For example:

```
start_date = datetime.date(2015, 1, 12)
end_date   = datetime.date(2015, 2, 12)
dates = gpsbro.unavco.rinex.get_URLs_within(start_date, end_date, sample_size=5, sample_type="DAY", )#zone="HAWAII")
for date in dates:
    mZ_files = [mZ for mZ, dZ, qc in dates[date] if mZ is not None]
    dZ_files = [dZ for mZ, dZ, qc in dates[date] if dZ is not None]
    qc_files = [qc for mZ, dZ, qc in dates[date] if qc is not None]
```

Notice that not all dates have file of each type (mZ, dZ, and qc). If a certain date does not have a URL for a certain filetype, it will contain `None` in place of the URL. It may be useful to filter out such instances of `None` as shown in the example above.

# License and Redistribution

This project is licensed under the MIT License. Feel free to contribute to or fork this project.

# Original Author

Thomas Fischer
