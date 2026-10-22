
"""Unit tests for gym requirements R1, R2, R3 and R7."""

from gym import calculate_cost


# R1: Plan validation
def test_basic_plan():
    """Verify the BASIC plan price."""
    assert calculate_cost("BASIC", [], 1) == 30


def test_standard_plan():
    """Verify the STANDARD plan price."""
    assert calculate_cost("STANDARD", [], 1) == 45


def test_premium_plan():
    """Verify the PREMIUM plan price."""
    assert calculate_cost("PREMIUM", [], 1) == 70


def test_invalid_plan():
    """Reject a plan that is not in the price table."""
    assert calculate_cost("GOLD", [], 1) == -1


# R2: Extra validation
def test_group_classes_extra():
    """Calculate the price with group classes."""
    assert calculate_cost("BASIC", ["GROUP_CLASSES"], 1) == 45


def test_personal_training_extra():
    """Calculate the price with personal training."""
    assert calculate_cost("STANDARD", ["PERSONAL_TRAINING"], 1) == 70


def test_spa_with_premium_plan():
    """Allow SPA with the PREMIUM plan."""
    assert calculate_cost("PREMIUM", ["SPA"], 1) == 100


def test_specialized_program_extra():
    """Calculate the price with the specialized program."""
    assert calculate_cost("PREMIUM", ["SPECIALIZED_PROGRAM"], 1) == 110


def test_invalid_extra():
    """Reject an extra that is not in the price table."""
    assert calculate_cost("BASIC", ["INVALID_EXTRA"], 1) == -1


def test_premium_extra_with_basic_plan():
    """Reject SPA when the selected plan is not PREMIUM."""
    assert calculate_cost("BASIC", ["SPA"], 1) == -1


# R3: Subtotal and member validation
def test_multiple_members():
    """Calculate the subtotal for multiple members."""
    assert calculate_cost("BASIC", [], 3) == 90


def test_multiple_extras():
    """Calculate the subtotal with two extras."""
    assert calculate_cost(
        "STANDARD",
        ["GROUP_CLASSES", "PERSONAL_TRAINING"],
        2,
    ) == 170


def test_zero_members():
    """Reject a membership with zero members."""
    assert calculate_cost("BASIC", [], 0) == -1


def test_negative_members():
    """Reject a negative number of members."""
    assert calculate_cost("BASIC", [], -1) == -1


def test_non_integer_members():
    """Reject a number of members that is not an integer."""
    assert calculate_cost("BASIC", [], 1.5) == -1


# R7: Invalid results
def test_invalid_selection_returns_minus_one():
    """Return -1 when the plan is invalid."""
    assert calculate_cost("GOLD", [], 1) == -1
