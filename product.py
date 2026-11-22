import sys

def product_details(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: Rs. {price:.2f}"
    )


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python product.py <ID> <Name> <Quantity> <Price>")
        sys.exit(1)

    try:
        product_id = sys.argv[1]
        name = sys.argv[2]
        quantity = int(sys.argv[3])
        price = float(sys.argv[4])

        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative")

        print("Product Information:")
        print(product_details(product_id, name, quantity, price))

    except ValueError as e:
        print("Error:", e)
        sys.exit(1)