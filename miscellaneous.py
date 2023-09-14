


def convert_java_to_python_conditional(java_conditional: str) -> str:
    """Converts a ``Java`` or ``C++`` or ``C`` style conditional
    ternary operator expression to a ``Python`` ternary operation

    The ternary operator should be in the format:
    ``(condition) ? value_if_true : value_if_false``, and it will be
    converted to Python's equivalent condition which is in the format:
    ``value_if_true if condition else value_if_false``

    Parameters
    ----------
    java_conditional : str
        A conditional ternary operator (which can include nested
        ternary operations) in the format
        ``(condition) ? value_if_true : value_if_false``

    Returns
    -------
    str
        The ``Python`` equivalent of the passed-in conditional
        ternary operator, which is returned as a string in the format:
        ``value_if_true if condition else value_if_false``

    Examples
    --------
    Below is a complex example from `Geeks 4 Geeks <https://www.geeksforgeeks.org/c-nested-ternary-operator/>`_
    which includes nested conditional ternary operators:

    ```java
    5 > 2 ? 4 > 1 ? 5 > 7 ? 10 : 5 > 8 ? 6 > 2 ? 20 : 30 : 5 > 6 ? 40 : 50 : 7 > 2 ? 60 : 70 : 8 > 9 ? 80 : 90;
    ```

    And this is how this function handles this example:

    >>> example = '5 > 2 ? 4 > 1 ? 5 > 7 ? 10 : 5 > 8 ? 6 > 2 ? 20 : 30 : 5 > 6 ? 40 : 50 : 7 > 2 ? 60 : 70 : 8 > 9 ? 80 : 90'
    >>> python_version = convert_java_to_python_conditional(example)
    >>> python_version
    '(((10 if 5 > 7 else ((20 if 6 > 2 else 30) if 5 > 8 else (40 if 5 > 6 else 50))) if 4 > 1 else (60 if 7 > 2 else 70)) if 5 > 2 else (80 if 8 > 9 else 90))'
    >>> eval(python_version)
    50
    """
    # Find the first "?" and corresponding ":" to split the expression
    index = java_conditional.find("?")
    if index == -1:
        return java_conditional

    condition = java_conditional[:index]
    remaining_expression = java_conditional[index + 1:]
    count = 1

    for i, char in enumerate(remaining_expression):
        if char == "?":
            count += 1
        elif char == ":":
            count -= 1
            if count == 0:
                true_expr = remaining_expression[:i]
                false_expr = remaining_expression[i + 1:]
                break

    python_condition = convert_java_to_python_conditional(condition).strip()
    python_true_expr = convert_java_to_python_conditional(true_expr).strip()
    python_false_expr = convert_java_to_python_conditional(false_expr).strip()

    python_conditional = f"({python_true_expr} if {python_condition} else {python_false_expr})"

    return python_conditional
