from difflib import SequenceMatcher

def calculate_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def get_product_suggestions(product: str, rules: list[dict]) -> list[str]:
    suggestions = []
    for rule in rules:
        if product in rule['antecedent']:
            for consequent in rule['consequent']:
                suggestions.append((consequent, rule['confidence']))
    suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
    return [s[0] for s in suggestions[:5]]  # Return top 5

def best_match(user_input: str, product_list: list[str]) -> tuple[str, float]:
    words = user_input.lower().split()
    best_product = ''
    highest_score = 0.0

    for word in words:
        for product in product_list:
            score = SequenceMatcher(None, word, product).ratio()
            if score > highest_score:
                best_product = product
                highest_score = score

    return best_product, highest_score
