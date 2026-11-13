
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


def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    print("Trying to prove:", goal)

    # Check whether goal is already a fact
    if goal in facts:
        print("Fact found:", goal)
        return True

    # Avoid infinite recursion
    if goal in visited:
        return False

    visited = visited | {goal}

    # Search for a rule that proves the goal
    for conditions, conclusion in rules:

        substitution = unify(goal, conclusion, {})

        if substitution is not None:

            print("Matching Rule:", conclusion)

            all_proved = True

            for condition in conditions:
                new_goal = substitute(
                    condition, substitution
                )

                if not backward_chaining(
                    new_goal, facts, rules, visited
                ):
                    all_proved = False
                    break

            if all_proved:
                print("Proved:", goal)
                return True

    print("Cannot prove:", goal)
    return False


# Rules
rules = [
    ([("Infection", "x")], ("Fever", "x")),
    ([("SoreThroat", "x")], ("Cough", "x")),
    ([("Fever", "x"), ("Cough", "x")], ("Flu", "x"))
]

# Given Facts
facts = [
    ("Infection", "Ravi"),
    ("SoreThroat", "Ravi")
]

# Goal
goal = ("Flu", "Ravi")

print("BACKWARD CHAINING\n")

result = backward_chaining(goal, facts, rules)

if result:
    print("\nFinal Result: Goal Proved Successfully")
else:
    print("\nFinal Result: Goal Not Proved")
