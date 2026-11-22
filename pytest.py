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