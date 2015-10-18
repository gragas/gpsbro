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
cd RSSS-toolkit/rsss2/
sudo python setup.py develop
# To be explicit about installing RSSS-toolkit to
# Python 2 instead of 3, run "sudo python2 setup.py develop"
```

If the installation failed, or doesn't work correctly, run the following command instead:

```
# After you've nagivated back to RSSS-toolkit/rsss2/,
sudo python setup.py install
```

## Python 3+

Run these commands:

```
git clone https://github.com/gragas/RSSS-toolkit
cd RSSS-toolkit/rsss2/
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
    URLs = Collector.get_geonet_rinex_URLs(datetime.date(2015, 10, 12))
    Z_files = [Z for Z, qc in URLs]   # list of .Z URLs
    qc_files = [qc for Z, qc in URLs] # list of .qc URLs
```

# License and Redistribution

This project is licensed under the MIT License. Feel free to contribute to or fork this project.

# Original Author

Thomas Fischer
