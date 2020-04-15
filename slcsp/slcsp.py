"""Find second-lowest-cost silver plans by zip code.

This reads an input file of zipcodes in CSV format, computes the
SLCSP for each zip code using the data in `plans.csv` and `zips.csv`
in the current directory, and outputs the results in CSV format
on standard out.
"""

import csv
import sys

from collections import defaultdict


class SLCSP:

    """Class for computing SLCSP based on data files."""

    def __init__(self):
        """Load up plans and zips for SLCSP computations."""

        # self.zipcode_to_area is a dict with zipcode keys and rate area values
        # If the rate area determination fails, then the value for that
        # zip code is None
        self.zipcode_to_area = self._load_zipcode_data("./zips.csv")

        # self.area_to_plans is a dict with rate area keys and values that are
        # lists of silver plan costs
        self.area_to_silver_plans = self._load_plans_data("./plans.csv")

    @staticmethod
    def _load_zipcode_data(zips_filename):
        """Load zipcode data from a given file.

        Returns a dictionary that looks up rate areas by zip code. If the rate
        area cannot be determined for a zip code, then the value is None.
        """
        result = {}
        with open(zips_filename) as zips_file:
            # field names come from the header on the first line
            reader = csv.DictReader(zips_file)
            for row in reader:
                zipcode = row["zipcode"]
                # TODO: use a namedtuple for the rate_area item?
                rate_area = (row["state"], row["rate_area"])
                if zipcode in result:
                    # second time the zip appeared
                    if rate_area == result[zipcode]:
                        pass
                    else:
                        result[zipcode] = None
                else:
                    result[row["zipcode"]] = rate_area

        return result

    @staticmethod
    def _load_plans_data(plans_filename):
        """Load plans data from a give file.

        Returns a dictionary that looks up silver plan costs by rate area.
        """
        result = defaultdict(list)
        with open(plans_filename) as plans_file:
            # field names from header line
            reader = csv.DictReader(plans_file)
            for row in reader:
                if row["metal_level"] != "Silver":
                    continue
                rate_area = (row["state"], row["rate_area"])
                result[rate_area].append(row["rate"])
        return result

    def compute_slcsp(self, zipcode):
        """Compute the  SLCSP for a certain zip code.

        Returns None if the SLCSP can't be determined.
        """
        rate_area = self.zipcode_to_area.get(zipcode)
        plans = self.area_to_silver_plans[rate_area]
        if len(plans) < 2:
            return None
        else:
            return sorted(plans)[1]


def main(argv=None):
    """Run the program with arguments argv.

    If argv is None, then the arguments are loaded from sys.argv.
    """
    if argv is None:
        argv = sys.argv

    try:
        infile_name = argv[1]
    except IndexError:
        print(
            "ERROR: please provide the input filename as an argument: slcsp.py <input file>",
            file=sys.stderr,
        )
        return 1

    # TODO: pass data filenames as arguments to this object
    # and make them command line options
    slcsp = SLCSP()  # depends on zips.csv and plans.csv in this directory

    with open(infile_name) as infile:
        reader = csv.DictReader(infile)

        writer = csv.writer(sys.stdout)
        writer.writerow(["zipcode", "rate"])

        for row in reader:
            zipcode = row["zipcode"]
            rate = slcsp.compute_slcsp(zipcode)
            # this rate is a string, try to format it better
            try:
                rate = "{:.2f}".format(float(rate))
            except TypeError:
                pass

            writer.writerow([zipcode, rate])


if __name__ == "__main__":
    sys.exit(main())
