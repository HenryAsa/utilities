

def recursively_sort_dicts(dictionary: dict) -> dict:
    """Recursively sorts nested dictionaries by their keys
    alphabetically, where ties are sorted ASCII-betically

    When a dictionary has keys that are equivalent when made the same
    capitalization (imagine the keys "aA" and "Aa"), this function
    sorts these keys ASCII-betically, which means that "Aa" would
    appear before "aA".  This function is deterministic and repeatable
    on dictionaries with the same key-value pairs that might appear in
    different orders

    Parameters
    ----------
    dictionary : dict
        The dictionary (of potentially nested dictionaries) to be
        sorted

    Returns
    -------
    dict
        An alphabetically sorted dictionary where case insensitive
        equivalent keys are then sorted ASCII-betically

    Examples
    --------
    This is an example of a dictionary whose keys (when capitalized)
    are the same, but the dictionary is still stably/repeatably
    sorted using this function.

    >>> example1 = {"BA": 12, "Aa": 2, "AA": 1, "aA": 3, "aa": 4, "AB": 5, "aB": 6, "AAA": 5, "aAa": {"z": 2, "A": 1}}
    >>> sorted1 = recursively_sort_dicts(example1)
    {'AA': 1, 'Aa': 2, 'aA': 3, 'aa': 4, 'AAA': 5, 'aAa': {'A': 1, 'z': 2}, 'AB': 5, 'aB': 6, 'BA': 12}

    Here is the same example, but with some slight differences in the
    structure of the dictionary

    >>> example2 = {"aa": 4, "aA": 3, "Aa": 2, "AA": 1, "AB": 5, "aB": 6, "aAa": {"z": 2, "A": 1}, "AAA": 5, "BA": 12}
    >>> sorted2 = recursively_sort_dicts(example2)
    {'AA': 1, 'Aa': 2, 'aA': 3, 'aa': 4, 'AAA': 5, 'aAa': {'A': 1, 'z': 2}, 'AB': 5, 'aB': 6, 'BA': 12}

    This is the last example where the dictionary to be sorted is
    already in its final/correct order

    >>> example3 = {"AA": 1, "Aa": 2, "aA": 3, "aa": 4, "AAA": 5, "aAa": {"A": 1, "z": 2}, "AB": 5, "aB": 6, "BA": 12}
    >>> sorted3 = recursively_sort_dicts(example3)
    {'AA': 1, 'Aa': 2, 'aA': 3, 'aa': 4, 'AAA': 5, 'aAa': {'A': 1, 'z': 2}, 'AB': 5, 'aB': 6, 'BA': 12}

    """
    sorted_dict = {}

    for key in sorted(dictionary.keys(), key=lambda k: (k.casefold(), k)):
        value = dictionary[key]

        if isinstance(value, dict):
            sorted_dict[key] = recursively_sort_dicts(value)
        else:
            sorted_dict[key] = value

    return sorted_dict
