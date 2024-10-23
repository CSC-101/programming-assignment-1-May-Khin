import data
import math

# Write your functions for each part in the space below.

# Part 1
#input: a word -> str
#output: count of vowels in the word -> int
#Counts how many vowels are in the word(str) and return the vowel count (int)
def vowel_count(str) -> int:
    str = list(str.upper())     #make input into list:str and make it upper case
    vowels = 'AEIOU'
    count = [i for i in str if i in vowels]
    return len(count)


# Part 2
#input: A list of lists of int.
#output: A list of lists of int that has length of 2.
#Filter out lists of integers that doesn't have a length of 2.
def short_lists(list:list[list[int]]):
    return [newList for newList in list if len(newList)==2]


# Part 3
#input: A list of lists of int.
#output: A list of list of int but lists that has two elements are in ascending order.
def ascending_pairs(list:list[list[int]]):
    new_list = []
    for i in range(len(list)):
        sub_list = list[i]
        if len(sub_list) == 2:
            if sub_list[0] > sub_list[1]:
                new_list.append([sub_list[1], sub_list[0]])
            else:
                new_list.append(sub_list)
        else:
            new_list.append(sub_list)
    return new_list


# Part 4
#input: two prices - in dollars and cents
#output: total sum of two prices
#add dollars and cents separately, then divide total cents by 100 if cents>= 100
def add_prices(price1, price2):
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    if total_cents >= 100:
        total_dollars = total_dollars + total_cents//100
        total_cents = total_cents% 100

    return data.Price(total_dollars, total_cents)


# Part 5
#input: two points of the rectangle - top_left and bottom_right
#output: area of the rectangle
#determine width and length using two points and times width and height to get the area
def rectangle_area(rectangle):
    width = rectangle.bottom_right.x - rectangle.top_left.x
    length = rectangle.top_left.y - rectangle.bottom_right.y
    return width * length


# Part 6
#output: return a list of books written by the specified author
def books_by_author(name:str, books:list):
    book_list = []
    for i in books:
        if i.authors == name:
            book_list.append(i)
    return book_list



# Part 7
#The function calculate the smallest bounding circle for a given rectangle
#output: Circle object with its center point (x, y) and radius
def circle_bound(rectangle):
    # Calculate the center of the rectangle
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2

    #finding the radius
    radius = math.sqrt((center_x - rectangle.top_left.x) ** 2 +
                       (center_y - rectangle.top_left.y) ** 2)

    return data.Circle(data.Point(center_x, center_y), radius)


# Part 8
#input:  A list of employee objects, where each object has attributes pay_rate and name.
#output: A list of employee names that has below average pay
def below_pay_average(employees:list):
    if not employees:
        return []
    #calculate the total pay
    total_pay = sum(employee.pay_rate for employee in employees)
    average = total_pay/ len(employees)

    #list of employees below average pay
    below_avg = [employee.name for employee in employees if employee.pay_rate < average]

    return below_avg






