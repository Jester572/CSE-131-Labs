# 1. Name:
#      Jesse Earley
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      The sub-list-sort program takes a json file specified the user and sorts the array using the sub-list sort method.
#      It then prints the sorted list to the screen
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was I miss typed a portion of code that was throwing an error that had to do with my index being out of range.
#      It took me about 30-45 minutes to debug and find where my mistake was. I also enjoyed going over assert statements and creating my
#      test cases
# 5. How long did it take for you to complete the assignment?
#      3.5 Hours


import json


def main():
    # Runs the test cases
    testCases()

    # Runs main program
    source_array = get_array()
    print_sorted_array(source_array)


def get_array():
    # Get file input from user
    file = input("Enter the destination of the array file:  ")

    # Opens the file and retrieves data from json
    with open(file) as json_file:
        data = json.load(json_file)

    # Returns data
    return data


def print_sorted_array(source_array):
    # Prints the finished array
    print(source_array)


def sort_array(source_array):
    # Creates the source array and an empty array
    array_size = len(source_array)
    destination_array = [0] * array_size
    number = 2

    #   Sort loop array
    while number > 1:
        number = 0
        source1_begin = 0

        # Create sub arrays
        while source1_begin < array_size:
            source1_end = source1_begin + 1
            while (
                source1_end < array_size
                and source_array[source1_end - 1] <= source_array[source1_end]
            ):
                source1_end += 1

            source2_begin = source1_end

            if source2_begin < array_size:
                source2_end = source2_begin + 1

            else:
                source2_end = source2_begin

            while (
                source2_end < array_size
                and source_array[source2_end - 1] <= source_array[source2_end]
            ):
                source2_end += 1

            number += 1

            source1 = (source1_begin, source1_end)
            source2 = (source2_begin, source2_end)

            # Calls function to combine source1 and source2
            combine_subArrays(source_array, destination_array, source1, source2)
            source1_begin = source2_end

        # swap array
        source_array, destination_array = destination_array, source_array

    return source_array


def combine_subArrays(source_array, destination_array, source1, source2):
    source1_begin, source1_end = source1
    source2_begin, source2_end = source2

    # Iterate through the length of arrays
    for i in range(source1_begin, source2_end):
        if (source1_begin < source1_end) and (
            source2_begin == source2_end
            or source_array[source1_begin] < source_array[source2_begin]
        ):
            destination_array[i] = source_array[source1_begin]
            source1_begin += 1

        else:
            destination_array[i] = source_array[source2_begin]
            source2_begin += 1

    return destination_array


def testCases():
    # Test 1: Empty Array
    Empty_Array = []
    assert sort_array(Empty_Array) == []

    # Test 2: All Positive numbers
    Positive_Numbers = [5, 6, 1, 23, 48, 15]
    assert sort_array(Positive_Numbers) == [1, 5, 6, 15, 23, 48]

    # Test 3: All negative numbers
    Negative_Numbers = [-1, -8, -47, -23]
    assert sort_array(Negative_Numbers) == [-47, -23, -8, -1]

    # Test 4: Sorts positive and negative numbers
    Negative_and_Positive = [6, -25, 13, 5, -36, -5, 25]
    assert sort_array(Negative_and_Positive) == [-36, -25, -5, 5, 6, 13, 25]

    # Test 5: Sort numbers in reversed order
    Reversed_Order = [6, 5, 4, 3, 2, 1]
    assert sort_array(Reversed_Order) == [1, 2, 3, 4, 5, 6]

    # Test 6: Sort array already in order
    In_Order = [1, 2, 3, 4, 5, 6]
    assert sort_array(In_Order) == [1, 2, 3, 4, 5, 6]

    # Test 7: Sorts Decimals
    Decimals = [0.2, 0.9, 0.7, 0.4, 0.13]
    assert sort_array(Decimals) == [0.13, 0.2, 0.4, 0.7, 0.9]

    # Test 8: Sorts Strings
    Strings = ["Hello", "Apple", "Orange", "Goodbye", "Blue"]
    assert sort_array(Strings) == ["Apple", "Blue", "Goodbye", "Hello", "Orange"]

    # Test 9: Sorts array with same values
    Same_Numbers = [3, 5, 1, 1, 1, 2, 2, 4, 8, 5, 3, 5, 6, 7]
    assert sort_array(Same_Numbers) == [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8]

    print("All test cases passed!!!")


if __name__ == "__main__":
    main()
