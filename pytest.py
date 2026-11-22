import pytest
from product import product_details

def test_product_details():
    result = product_details("P101", "Laptop", 2, 45000)

    expected = (
        "Product ID: P101\n"
        "Product Name: Laptop\n"
        "Quantity: 2\n"
        "Price: Rs. 45000.00"
    )

    assert result == expected


def test_another_product():
    result = product_details("P102", "Mouse", 5, 500)

    expected = (
        "Product ID: P102\n"
        "Product Name: Mouse\n"
        "Quantity: 5\n"
        "Price: Rs. 500.00"
    )

    assert result == expected