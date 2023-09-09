


def convert_java_to_python_conditional(java_conditional: str) -> str:
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
