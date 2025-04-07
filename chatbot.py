def get_product_suggestions(product, rules):
    suggestions = []
    for rule in rules:
        if product in rule['antecedent']:
            for consequent in rule['consequent']:
                suggestions.append((consequent, rule['confidence']))
    # Sort by confidence
    suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)

    seen = set()
    result = []
    for item, _ in suggestions:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result
