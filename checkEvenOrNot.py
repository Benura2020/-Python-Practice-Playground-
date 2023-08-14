"""

             /\_/\
            (  ･ω･)
|------------U-BW--U----------|
|       MMXXIII_VIII_XIV      |
|Check the numbers in list "a"|
|       are Even or Not       |
| by using List Comprehension |
|_____________________________|
            |     |
            |     |
             U   U

"""

a = [10, 13, 15, 16, 18, 29]


def is_even(number):
    return number % 2 == 0


b = [is_even(i) for i in a]
print(b)
