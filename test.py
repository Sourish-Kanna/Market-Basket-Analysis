import random
import csv
from pathlib import Path

# List of possible grocery items
items = [
    "milk", "bread", "eggs", "butter", "jam", "cheese", "coffee", "tea", "sugar", "cereal",
    "cookies", "chips", "juice", "fruits", "biscuits", "toast", "soda", "chocolate", "yogurt", "nuts"
]

# Generate 100 transactions with 1 to 5 random items each
transactions = []
for _ in range(100):
    num_items = random.randint(1, 5)
    transaction = random.sample(items, num_items)
    transactions.append(transaction)

# Save transactions to a CSV file
output_file = Path("transactions.csv")
with output_file.open(mode="w", newline="") as file:
    writer = csv.writer(file)
    for transaction in transactions:
        writer.writerow(transaction)

print("done")