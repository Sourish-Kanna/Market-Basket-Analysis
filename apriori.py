from collections import defaultdict
from itertools import combinations
import csv

def load_transactions(file_path):
    """
    Load transactions from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[set]: List of transactions, where each transaction is a set of items.
    """
    transactions = []
    with open(file_path, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            items = [item.strip().lower() for item in row if item.strip()]
            if items:
                transactions.append(set(items))
    print(f"Loaded {len(transactions)} transactions.")
    return transactions


def get_frequent_itemsets(transactions, min_support):
    """
    Find frequent itemsets using the Apriori algorithm.

    Args:
        transactions (list[set]): List of transactions.
        min_support (float): Minimum support threshold (0 < min_support <= 1).

    Returns:
        tuple[dict, int]: Frequent itemsets with their counts and total number of transactions.
    """
    if not transactions:
        print("No transactions provided.")
        return {}, 0

    if min_support <= 0 or min_support > 1:
        raise ValueError("min_support must be between 0 and 1.")

    # Step 1: Count single items
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[frozenset([item])] += 1

    total_transactions = len(transactions)
    frequent_itemsets = {item: count for item, count in item_counts.items() if count / total_transactions >= min_support}

    print(f"Found {len(frequent_itemsets)} frequent 1-itemsets.")

    # Step 2: Generate larger itemsets
    k = 2
    current_itemsets = list(frequent_itemsets.keys())

    while current_itemsets:
        # print(f"Generating candidate {k}-itemsets...")
        candidate_sets = set(
            frozenset(a.union(b)) for a, b in combinations(current_itemsets, 2) if len(a.union(b)) == k
        )

        # Count occurrences of candidate itemsets
        item_counts = defaultdict(int)
        for transaction in transactions:
            for candidate in candidate_sets:
                if candidate.issubset(transaction):
                    item_counts[candidate] += 1

        # Filter candidates by min_support
        next_itemsets = {}
        for item, count in item_counts.items():
            # support = count / total_transactions
            # print(f"{list(item)[0]}: support={support:.2f}")
            if count / total_transactions >= min_support:
                next_itemsets[item] = count
                
        frequent_itemsets.update(next_itemsets)

        print(f"Found {len(frequent_itemsets)} frequent {k}-itemsets.")

        current_itemsets = list(next_itemsets.keys())
        k += 1

    return frequent_itemsets, total_transactions


def generate_rules(frequent_itemsets, total_transactions, min_confidence=0.5):
    """
    Generate association rules from frequent itemsets.

    Args:
        frequent_itemsets (dict): Frequent itemsets with their counts.
        total_transactions (int): Total number of transactions.
        min_confidence (float): Minimum confidence threshold (default: 0.5).

    Returns:
        list[dict]: List of association rules with antecedent, consequent, and confidence.
    """
    if not frequent_itemsets:
        print("No frequent itemsets provided.")
        return []

    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) >= 2:
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    if antecedent in frequent_itemsets:
                        confidence = frequent_itemsets[itemset] / frequent_itemsets[antecedent]
                        if confidence >= min_confidence:
                            rules.append({
                                "antecedent": set(antecedent),
                                "consequent": set(consequent),
                                "confidence": round(confidence, 2)
                            })
    print(f"Generated {len(rules)} rules.")
    return rules
