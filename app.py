
def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")

    return price * quantity


def main():
    price = 100
    quantity = 3

    total = calculate_total(price, quantity)
    print(f"Order total: Rs. {total}")


if __name__ == "__main__":
    main()
