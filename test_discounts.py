"""Unit tests for R4, R5, and R6 discount calculations."""

import pytest
from discounts import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)


# --- Tests for R4: Group discount ---
def test_group_discount_applied_two_members():
    # 2 miembros reciben 10% de descuento (100 -> 90)
    assert apply_group_discount(100.0, 2) == pytest.approx(90.0)


def test_group_discount_applied_multiple_members():
    # 3 o más miembros reciben 10% de descuento (200 -> 180)
    assert apply_group_discount(200.0, 3) == pytest.approx(180.0)


def test_group_discount_not_applied_single_member():
    # 1 miembro no recibe descuento grupal
    assert apply_group_discount(100.0, 1) == pytest.approx(100.0)


# --- Tests for R5: Special offer ---
def test_special_offer_greater_than_400():
    # Monto mayor a 400 resta 50 (450 -> 400)
    assert apply_special_offer(450.0) == pytest.approx(400.0)


def test_special_offer_exact_400():
    # 400 no es > 400, pero sí > 200: resta 20 (400 -> 380)
    assert apply_special_offer(400.0) == pytest.approx(380.0)


def test_special_offer_greater_than_200():
    # Monto mayor a 200 pero <= 400 resta 20 (250 -> 230)
    assert apply_special_offer(250.0) == pytest.approx(230.0)


def test_special_offer_exact_200_or_below():
    # 200 o menos no recibe descuento de oferta
    assert apply_special_offer(200.0) == pytest.approx(200.0)
    assert apply_special_offer(150.0) == pytest.approx(150.0)


# --- Tests for R6: Premium surcharge ---
def test_premium_surcharge_applied():
    # Con extra premium aplica 15% de recargo (100 -> 115)
    assert apply_premium_surcharge(100.0, True) == pytest.approx(115.0)


def test_premium_surcharge_not_applied():
    # Sin extra premium el monto se mantiene intacto
    assert apply_premium_surcharge(100.0, False) == pytest.approx(100.0)
