
def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}

    if isinstance(x, str) and x in substitution:
        x = substitution[x]

    if isinstance(y, str) and y in substitution:
        y = substitution[y]

    if x == y:
        return substitution

    if isinstance(x, str) and x.islower():
        substitution[x] = y
        return substitution

    if isinstance(y, str) and y.islower():
        substitution[y] = x
        return substitution

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)
            if substitution is None:
                return None

        return substitution

    return None


def substitute(expression, substitution):
    if isinstance(expression, str):
        while expression in substitution:
            expression = substitution[expression]
        return expression

    if isinstance(expression, tuple):
        return (expression[0],) + tuple(
            substitute(item, substitution)
            for item in expression[1:]
        )

    return expression


def match_conditions(conditions, facts, substitution):
    if not conditions:
        return [substitution]

    results = []

    first = substitute(conditions[0], substitution)

    for fact in facts:
        new_substitution = unify(
            first, fact, substitution.copy()
        )

        if new_substitution is not None:
            remaining = match_conditions(
                conditions[1:],
                facts,
                new_substitution
            )
            results.extend(remaining)

    return results


# Rules: Conditions -> Conclusion
rules = [
    ([("Infection", "x")], ("Fever", "x")),
    ([("SoreThroat", "x")], ("Cough", "x")),
    ([("Fever", "x"), ("Cough", "x")], ("Flu", "x"))
]

# Initial facts
facts = [
    ("Infection", "Ravi"),
    ("SoreThroat", "Ravi")
]

print("Initial Facts:")
for fact in facts:
    print(fact)

# Forward Chaining
print("\nForward Chaining:")

while True:
    new_facts = []

    for conditions, conclusion in rules:
        substitutions = match_conditions(
            conditions, facts, {}
        )

        for substitution in substitutions:
            new_fact = substitute(conclusion, substitution)

            if new_fact not in facts and new_fact not in new_facts:
                new_facts.append(new_fact)
                print("New Fact:", new_fact)

    if not new_facts:
        break

    facts.extend(new_facts)

# Check final goal
goal = ("Flu", "Ravi")

if goal in facts:
    print("\nGoal Proved:", goal)
else:
    print("\nGoal Not Proved")
