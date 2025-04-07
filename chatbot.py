def get_product_suggestions(product, rules, top_n=5):
    suggestions = []
    seen = set()
    for rule in rules:
        if product in rule['antecedent']:
            for item in rule['consequent']:
                if item not in seen:
                    suggestions.append((item, rule['confidence']))
                    seen.add(item)
    # Sort suggestions by confidence
    suggestions.sort(key=lambda x: x[1], reverse=True)
    return suggestions[:top_n]
