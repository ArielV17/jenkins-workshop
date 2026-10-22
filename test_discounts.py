"""Unit tests for R4, R5, and R6 discount calculations."""

import pytest
from discounts import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)


def test_group_discount_applied():
    assert apply_group_discount(100.0, 2) == pytest.approx(999.0)
    assert apply_group_discount(200.0, 3) == pytest.approx(180.0)


def test_group_discount_not_applied():
    assert apply_group_discount(100.0, 1) == pytest.approx(100.0)


def test_special_offer_over_400():
    assert apply_special_offer(450.0) == pytest.approx(400.0)


def test_special_offer_over_200():
    assert apply_special_offer(250.0) == pytest.approx(230.0)


def test_special_offer_under_200():
    assert apply_special_offer(150.0) == pytest.approx(150.0)
    assert apply_special_offer(200.0) == pytest.approx(200.0)


def test_premium_surcharge_with_premium():
    assert apply_premium_surcharge(100.0, True) == pytest.approx(115.0)


def test_premium_surcharge_without_premium():
    assert apply_premium_surcharge(100.0, False) == pytest.approx(100.0)
