
rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "PKR": 280.0,
    "GBP": 0.81,
    "JPY": 140.0
}


while True:
    source = input("Enter source currency (e.g., USD, EUR, PKR): ").upper()
    if source in rates:
        break
    print("Invalid currency! Try again.")


while True:
    target = input("Enter target currency (e.g., USD, EUR, PKR): ").upper()
    if target in rates:
        break
    print("Invalid currency! Try again.")


while True:
    try:
        amount = float(input(f"Enter amount in {source}: "))
        break
    except ValueError:
        print("Please enter a valid number!")


def convert_currency(amount, source, target):
    # Convert to base currency first, then to target
    amount_in_base = amount / rates[source]
    converted_amount = amount_in_base * rates[target]
    return round(converted_amount, 2)


result = convert_currency(amount, source, target)
print(f"{amount} {source} = {result} {target}")
