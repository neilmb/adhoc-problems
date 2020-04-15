"""Test SLCSP computation class."""

import pytest

from slcsp import SLCSP


@pytest.fixture
def slcsp():
    return SLCSP()


def test_creation(slcsp):
    assert type(slcsp.zipcode_to_area) == dict


def test_zipcode_data(slcsp):
    assert len(slcsp.zipcode_to_area) > 0
    # look up an arbitrary zip code
    rate_area = slcsp.zipcode_to_area["52101"]
    assert int(rate_area[1]) > 0
    assert rate_area[0] == "IA"


def test_plan_data(slcsp):
    rate_area = slcsp.zipcode_to_area["52101"]
    plans = slcsp.area_to_silver_plans[rate_area]
    assert len(plans) > 0


def test_compute(slcsp):
    rate = slcsp.compute_slcsp("52101")
    # manually computed, 52101 is in (IA, 7) then find plans with
    # grep ",IA," plans.csv | grep "7$" | grep Silver | sort -t, -k4 -n
    # gives 254.56
    assert rate == "254.56"
