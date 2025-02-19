def flatten_dict(d, parent_key='', sep='_'):
    """
    Flatten a nested dictionary.

    Args:
        d: Nested dictionary to be flattened.
        parent_key: String representing the parent key.
        sep: Separator used to join keys.

    Returns:
        Flattened dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)



if __name__ == "__main__":
    nested_dict = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3
            }
        },
        'f': {
            'g': 4
        }
    }

    flattened_dict = flatten_dict(nested_dict)
    print(flattened_dict)
