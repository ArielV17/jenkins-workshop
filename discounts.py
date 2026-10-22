"""Module containing discount and surcharge calculations for gym quotes."""


def apply_group_discount(subtotal: float, members: int) -> float:
    """R4: Group discount.

    With 2 or more members, the subtotal gets a 10% discount.
    """
    if members >= 2:
        return subtotal * 0.90
    return float(subtotal)


def apply_special_offer(amount: float) -> float:
    """R5: Special offer.

    Applied to the amount after R4.
    If greater than 400, subtract 50.
    Otherwise, if greater than 200, subtract 20.
    The two never add up.
    """
    if amount > 400:
        return amount - 50.0
    if amount > 200:
        return amount - 20.0
    return float(amount)


def apply_premium_surcharge(amount: float, has_premium: bool) -> float:
    """R6: Premium surcharge.

    If the selection includes at least one premium extra,
    add 15% to the amount after R5.
    """
    if has_premium:
        return amount * 1.15
    return float(amount)
