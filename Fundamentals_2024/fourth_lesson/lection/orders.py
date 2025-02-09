#"coffee", "coke", "water", or "snacks",
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
def order(item: str, quantity: int) -> float:
    if item == "coffee":
        return quantity * 1.50
    elif item == "water":
        return quantity * 1.00
    elif item == "coke":
        return quantity * 1.40
    elif item == "snacks":
        return quantity * 2.00


product = input()
numbers_of_products = int(input())
print(f"{order(product, numbers_of_products):.2f}")




