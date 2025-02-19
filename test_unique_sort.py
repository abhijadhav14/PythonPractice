from unique_sort import unique_and_sort_descending

def test_unique_and_sort_descending():
    input_list = [5, 2, 9, 5, 6, 3, 2, 1, 8, 7, 4, 3]
    expected_output = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert unique_and_sort_descending(input_list) == expected_output

if __name__ == "__main__":
    test_unique_and_sort_descending()
    print("Tests passed!")
