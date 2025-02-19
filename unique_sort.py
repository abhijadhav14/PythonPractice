def unique_and_sort_descending(input_list):
    
    # Create a set to get unique elements
    unique_elements = set(input_list)
    
    # Convert the set back to a list and sort in descending order
    sorted_unique_descending = sorted(list(unique_elements), reverse=True)
    
    return sorted_unique_descending
