import pytest
from gym import calculate_cost


# R1: Plan validation
def test_basic_plan():
    assert calculate_cost("BASIC", [], 1) == 30


def test_standard_plan():
    assert calculate_cost("STANDARD", [], 1) == 45


def test_premium_plan():
    assert calculate_cost("PREMIUM", [], 1) == 70


def test_invalid_plan():
    assert calculate_cost("GOLD", [], 1) == -1


# R2: Extra validation
def test_group_classes_extra():
    assert calculate_cost("BASIC", ["GROUP_CLASSES"], 1) == 45


def test_personal_training_extra():
    assert calculate_cost("STANDARD", ["PERSONAL_TRAINING"], 1) == 70


def test_spa_with_premium_plan():
    assert calculate_cost("PREMIUM", ["SPA"], 1) == 100


def test_specialized_program_extra():
    assert calculate_cost("PREMIUM", ["SPECIALIZED_PROGRAM"], 1) == 110


def test_invalid_extra():
    assert calculate_cost("BASIC", ["INVALID_EXTRA"], 1) == -1


def test_premium_extra_with_basic_plan():
    assert calculate_cost("BASIC", ["SPA"], 1) == -1


# R3: Subtotal and member validation
def test_multiple_members():
    assert calculate_cost("BASIC", [], 3) == 90


def test_multiple_extras():
    assert calculate_cost(
        "STANDARD",
        ["GROUP_CLASSES", "PERSONAL_TRAINING"],
        2
    ) == 170


def test_zero_members():
    assert calculate_cost("BASIC", [], 0) == -1


def test_negative_members():
    assert calculate_cost("BASIC", [], -1) == -1


# R7: Invalid results
def test_invalid_selection_returns_minus_one():
    assert calculate_cost("GOLD", [], 1) == -1
