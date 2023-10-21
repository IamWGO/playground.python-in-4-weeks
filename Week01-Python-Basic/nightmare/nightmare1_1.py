# N 1.1 Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

def get_input_number(text) -> int:
    while True:
        try:
            input_number = int(input(f'{text} '))
            return input_number
        except ValueError:
            print("The input is not a number.")


def get_median_of_sorted_arrays(arrayItems) -> int:
    middle_index = len(arrayItems) // 2
    middle_item = arrayItems[middle_index]

    if len(arrayItems) % 2 == 0:
        sum_of_middle_item = arrayItems[middle_index - 1] + arrayItems[middle_index]
        middle_of_sort_value = sum_of_middle_item / 2
    else:
        middle_of_sort_value = middle_item

    return middle_of_sort_value


def main():
    numbers1 = []
    numbers2 = []

    maxSet1 = get_input_number("Amount of number list set 1: ")
    for index in range(maxSet1):
        numbers1.append(get_input_number(f"Input a number {index + 1}: "))

    maxSet2 = get_input_number("Amount of number list set 2: ")
    for index in range(maxSet2):
        numbers2.append(get_input_number(f"Input a number {index + 1}"))

    combined = numbers1 + numbers2
    sorted_numbers = sorted(combined)

    middle_sort_value = get_median_of_sorted_arrays(combined)

    print(f"\nCombine arrays: {combined}")
    print(f"\nMedian of Two Sorted Arrays {middle_sort_value}")

    print("-- End program Nightmare1.1 --")

if __name__ == '__main__':
    main()


# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10**6 <= nums1[i], nums2[i] <= 10**6
