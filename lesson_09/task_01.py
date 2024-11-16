"""This is a file for homework 9."""

# Create a function that takes two lists of different sizes
# and returns the list of sets of these lists.
# ex. l1=[1,3,5,7]  l2=[1,4,5]
# and function outcome is [(1,1), (3,4), (5,5), (7,0)]


def unite_lists(first_list, second_list):
    """
    Unite lists including all values.

    Args:
        first_list (list): The list of values to process.
        second_list (list): The list of values to process.

    Returns:
        list: list of sets with united values.
    """
    first_d = {first_list.index(i): i for i in first_list}
    second_d = {second_list.index(i): i for i in second_list}
    all_indexes = range(len(set(first_d.keys()).union(set(second_d.keys()))))
    return [(first_d.get(i, 0), second_d.get(i, 0)) for i in all_indexes]


l1 = [1, 3, 5, 7]
l2 = [1, 4, 5]
print(unite_lists(l1, l2))
