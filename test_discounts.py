"""Unit tests for R4, R5, and R6 discount calculations."""

# pylint: disable=missing-function-docstring

import pytest
from discounts import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)


def test_group_discount_applied():
    """Verify 10% discount applies for two or more members."""
    assert apply_group_discount(100.0, 2) == pytest.approx(90.0)
    assert apply_group_discount(200.0, 3) == pytest.approx(180.0)


def test_group_discount_not_applied():
    """Verify single member receives no group discount."""
    assert apply_group_discount(100.0, 1) == pytest.approx(100.0)


def test_special_offer_over_400():
    """Verify amounts over 400 receive 50 discount."""
    assert apply_special_offer(450.0) == pytest.approx(400.0)


def test_special_offer_over_200():
    """Verify amounts between 200 and 400 receive 20 discount."""
    assert apply_special_offer(250.0) == pytest.approx(230.0)


def test_special_offer_under_200():
    """Verify amounts 200 or lower receive no special discount."""
    assert apply_special_offer(150.0) == pytest.approx(150.0)
    assert apply_special_offer(200.0) == pytest.approx(200.0)


def test_premium_surcharge_with_premium():
    """Verify 15% surcharge applies when premium extra is selected."""
    assert apply_premium_surcharge(100.0, True) == pytest.approx(115.0)


def test_premium_surcharge_without_premium():
    """Verify no surcharge is added when no premium extra is selected."""
    assert apply_premium_surcharge(100.0, False) == pytest.approx(100.0)
