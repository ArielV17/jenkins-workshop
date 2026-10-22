
"""Calculates the gym membership costs for requirements R1, R2, R3 and R7."""

from decimal import Decimal, ROUND_HALF_UP


PLANS = {
    "BASIC": 30,
    "STANDARD": 45,
    "PREMIUM": 70,
}

EXTRAS = {
    "GROUP_CLASSES": 15,
    "PERSONAL_TRAINING": 25,
    "SPA": 30,
    "SPECIALIZED_PROGRAM": 40,
}

PREMIUM_EXTRAS = {"SPA"}


def calculate_cost(plan: str, extras: list[str], members: int) -> int:
    """Return the membership subtotal or -1 if the selection is invalid."""

    # R1: Validate the selected plan.
    if plan not in PLANS:
        return -1

    # R2: Validate extras and premium restrictions.
    for extra in extras:
        if extra not in EXTRAS:
            return -1

        if extra in PREMIUM_EXTRAS and plan != "PREMIUM":
            return -1

    # R3: Validate the number of members.
    if not isinstance(members, int) or isinstance(members, bool):
        return -1

    if members < 1:
        return -1

    # Calculate the subtotal without discounts or surcharges.
    price_per_member = PLANS[plan]

    for extra in extras:
        price_per_member += EXTRAS[extra]

    subtotal = price_per_member * members

    # R7: Round half up at the end.
    total = Decimal(str(subtotal)).quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP,
    )

    return int(total)
