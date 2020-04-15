# Second Lowest-Cost Silver Plan

The second-lowest cost silver plan (SLCSP) for a particular geographic region
is used as a benchmark for health plan costs in a particular area. This code
takes a file of zip codes as input and outputs a CSV file with the SLCSP for
those zip codes. This problem is based on the original description at
<https://homework.adhoc.team/slcsp/>.

The data files required are available from
<https://homework.adhoc.team/static/slcsp-aab498af8d435c61f13227d0e5702a23.zip>.
Download that file, unzip it and put the files `plans.csv`, `zips.csv`, and
`slcsp.csv` in this directory.


## Installation

The code is written in Python 3 and depends on a local installation of Python
3, version 3.5+. It has no dependencies beyond the Python standard library.

You can run the program on the input file `slcsp.csv` and re-direct the
standard output into the file `slcsp_rates.csv`.

```
python3 slcsp.py slcsp.csv > slcsp_rates.csv
```


## Development

Development dependencies for code formatting and running the unit tests can be
installed with pip. You should use a virtual environment

```
python3 -m venv ./venv
source ./venv/bin/activate
```

and inside the virtual environment install the dependencies using

```
pip3 install -r dev-requirements.txt
```

To run the tests with PyTest, after installing the development dependencies,

```
python3 -m pytest test/
```
