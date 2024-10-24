import hw1
import unittest
import data


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = 'hello'
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "COMPUTER"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        input = [[1, 2], [3, 4, 5, 6], [7, 8], [9]]
        result = hw1.short_lists(input)
        expected = [[1, 2], [7, 8]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input = [[1, 2], [2, 3, 4], [3, 4]]
        result = hw1.short_lists(input)
        expected = [[1, 2], [3, 4]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_order_1(self):
        input = [[1, 2, 3], [6, 3, 1], [4, 2], [7, 2]]
        result = hw1.ascending_pairs(input)
        expected = [[1, 2, 3], [6, 3, 1], [2, 4], [2, 7]]
        self.assertEqual(expected, result)

    def test_ascending_order_2(self):
        input = [[6, 5], [2, 2], [9], [0, 3, 4]]
        result = hw1.ascending_pairs(input)
        expected = [[5, 6], [2, 2], [9], [0, 3, 4]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        price1 = data.Price(3, 75)
        price2 = data.Price(2, 50)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(6, 25)
        self.assertEqual((expected.dollars, expected.cents), (result.dollars, result.cents))

    def test_add_prices_2(self):
        price1 = data.Price(5, 50)
        price2 = data.Price(5, 50)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(11, 00)
        self.assertEqual((expected.dollars, expected.cents), (result.dollars, result.cents))

    # Part 5
    def test_rectangle_area_1(self):
        top_left = data.Point(1, 4)
        bottom_right = data.Point(5, 1)
        rectangle = data.Rectangle(top_left, bottom_right)
        result = hw1.rectangle_area(rectangle)
        expected = 12
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        top_left = data.Point(2, 5)
        bottom_right = data.Point(5,2)
        rectangle = data.Rectangle(top_left, bottom_right)
        result = hw1.rectangle_area(rectangle)
        expected = 9
        self.assertEqual(expected, result)


    # Part 6
    def test_book_by_author_1(self):
        books = [
            data.Book("Stephenie Meyer" , "New Moon"),
            data.Book("Stephen King", "The Shining"),
            data.Book("Stephenie Meyer", "Eclipse" )
        ]
        author_name = "Stephenie Meyer"
        result = hw1.books_by_author(author_name, books)
        expected = [
            data.Book("Stephenie Meyer", "New Moon"),
            data.Book("Stephenie Meyer", "Eclipse")
        ]
        self.assertEqual(expected, result)


    # Part 7
    def test_circle_bound(self):
        top_left = data.Point(1, 4)
        bottom_right = data.Point(5, 1)
        rectangle = data.Rectangle(top_left, bottom_right)

        result = hw1.circle_bound(rectangle)

        expected_center = data.Point(3, 2.5)
        expected_radius = 2.5
        expected = data.Circle(expected_center, expected_radius)
        self.assertEqual(expected.center, result.center)
        self.assertEqual(expected.radius, result.radius)



    # Part 8
    def test_below_pay_average_1(self):
        employees = [
            data.Employee("May", 50000),
            data.Employee("Travis", 40000),
            data.Employee("Frances", 30000),
            data.Employee("Elsa", 60000)
        ]
        result = hw1.below_pay_average(employees)
        expected = ["Travis", "Frances"]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
