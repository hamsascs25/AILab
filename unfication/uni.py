
def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}

    # Apply existing substitutions
    while isinstance(x, str) and x in substitution:
        x = substitution[x]

    while isinstance(y, str) and y in substitution:
        y = substitution[y]

    # If both expressions are equal
    if x == y:
        return substitution

    # Check if x is a variable
    if isinstance(x, str) and x.islower():
        if occurs_check(x, y, substitution):
            return None
        substitution[x] = y
        return substitution

    # Check if y is a variable
    if isinstance(y, str) and y.islower():
        if occurs_check(y, x, substitution):
            return None
        substitution[y] = x
        return substitution

    # Compare function or predicate expressions
    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    return None


def occurs_check(variable, expression, substitution):
    while isinstance(expression, str) and expression in substitution:
        expression = substitution[expression]

    if variable == expression:
        return True

    if isinstance(expression, tuple):
        return any(
            occurs_check(variable, item, substitution)
            for item in expression[1:]
        )

    return False


# Example 1
print("Example 1:")
result = unify(("Knows", "x", "y"),
               ("Knows", "Ram", "Sita"))
print("Substitution:", result)


# Example 2
print("\nExample 2:")
result = unify(("P", ("f", "x"), "y"),
               ("P", ("f", "Ram"), "Sita"))
print("Substitution:", result)


# Example 3
print("\nExample 3:")
result = unify(("P", "x", "x"),
               ("P", "Ram", "y"))
print("Substitution:", result)


# Example 4: Failure
print("\nExample 4:")
result = unify("x", ("f", "x"))
print("Substitution:", result)
