import unittest

import pytest as pytest
from mock import patch
from parameterized import parameterized

from sorting import sort, bubble_sort, insertion_sort, shell_sort

TEST_CASES_FOR_SORT = [
    ([4, 6, 2, 3, 1, 6], [1, 2, 3, 4, 6, 6], "test_sorting"),
    ([], [], "test_sorting_empty_array"),
    ([1], [1], "test_sorting_one_element_array"),
    ([1, 1, 1, 1], [1, 1, 1, 1], "test_sorting_same_numbers"),
    ([-1, 1, -1, 1], [-1, -1, 1, 1], "test_sorting_negative_numbers"),
    ([1, -1, -1, 1], [-1, -1, 1, 1], "test_sorting_negative_numbers_v2"),
    ([1, -1, -1, -1, 1], [-1, -1, -1, 1, 1], "test_sorting_negative_numbers_v3"),
    ([1, 2, 1, 2], [1, 1, 2, 2], "test_sorting_alternating_numbers"),
    ([1, 2, 1, 2, 1, 2], [1, 1, 1, 2, 2, 2], "test_sorting_alternating_numbers_v2"),
    ([3.2, 3.5, 3.5, 1], [1, 3.2, 3.5, 3.5], "test_sorting_comma_numbers"),
    ([1, 0, 1, 1], [0, 1, 1, 1], "test_sorting_with_zero"),
    ([10, 0, 10, 10], [0, 10, 10, 10], "test_sorting_with_zero_v3"),
    ([1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1], "test_sorting_with_zero_v2"),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], "test_sorting_revers_array"),
    ([9, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 9], "test_sorting_many_same_elements"),
]


# print(sort([4,6,2,3,1,6]))
# write your tests here

@pytest.mark.parametrize('input, expected, msg', TEST_CASES_FOR_SORT)
def test_bubble_sort(input, expected, msg):
    assert bubble_sort(input) == expected, msg


@pytest.mark.parametrize('input, expected, msg', TEST_CASES_FOR_SORT)
def test_shell_sort(input, expected, msg):
    assert shell_sort(input) == expected, msg


@pytest.mark.parametrize('input, expected, msg', TEST_CASES_FOR_SORT)
def test_insertion_sort(input, expected, msg):
    assert insertion_sort(input) == expected, msg


class TestStringMethods(unittest.TestCase):

    def test_sorting(self):
        self.assertEqual(sort([4, 6, 2, 3, 1, 6]), [1, 2, 3, 4, 6, 6])

    def test_sorting_empty_array(self):
        self.assertEqual(sort([]), [])

    def test_sorting_one_element_array(self):
        self.assertEqual(sort([1]), [1])

    def test_sorting_same_numbers(self):
        self.assertEqual(sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_sorting_negative_numbers(self):
        self.assertEqual(sort([-1, 1, -1, 1]), [-1, -1, 1, 1])

    def test_sorting_negative_numbers_v2(self):
        self.assertEqual(sort([1, -1, -1, 1]), [-1, -1, 1, 1])

    def test_sorting_negative_numbers_v3(self):
        self.assertEqual(sort([1, -1, -1, -1, 1]), [-1, -1, -1, 1, 1])

    def test_sorting_alternating_numbers(self):
        self.assertEqual(sort([1, 2, 1, 2]), [1, 1, 2, 2])

    def test_sorting_alternating_numbers_v2(self):
        self.assertEqual(sort([1, 2, 1, 2, 1, 2]), [1, 1, 1, 2, 2, 2])

    def test_sorting_comma_numbers(self):
        self.assertEqual(sort([3.2, 3.5, 3.5, 1]), [1, 3.2, 3.5, 3.5])

    def test_sorting_with_zero(self):
        self.assertEqual(sort([1, 0, 1, 1]), [0, 1, 1, 1])

    def test_sorting_with_zero_v3(self):
        self.assertEqual(sort([10, 0, 10, 10]), [0, 10, 10, 10])

    def test_sorting_with_zero_v2(self):
        self.assertEqual(sort([1, 0, 1, 1, 1, 1, 1]), [0, 1, 1, 1, 1, 1, 1])

    def test_sorting_revers_array(self):
        self.assertEqual(sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_sorting_many_same_elements(self):
        self.assertEqual(sort([9, 1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1, 9])

    #         Additional tests

    @patch('sorting.insertion_sort')
    def test_sorting_method_choose__insertion_sort(self, insertion_sort_mock):
        for i in range(5):
            sort([i for e in range(i)])

        self.assertEqual(insertion_sort_mock.call_count, 5)

    @patch('sorting.bubble_sort')
    def test_sorting_method_choose__bubble_sort(self, bubble_sort_mock):
        for i in range(15):
            sort([i for e in range(i + 5)])

        self.assertEqual(bubble_sort_mock.call_count, 15)

    @patch('sorting.shell_sort')
    def test_sorting_method_choose__shell_sort(self, shell_sort_mock):
        sort([e for e in range(21)])

        sort([e for e in range(50)])

        sort([e for e in range(100)])

        self.assertEqual(shell_sort_mock.call_count, 3)


if __name__ == '__main__':
    unittest.main()
