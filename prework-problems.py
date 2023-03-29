# Question 1: "Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below."
# def hello_name(user_name):

def hello_name(user_name):
    print("hello_" + user_name)
#hello_name("Will")

# Question 2: "Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing"
# def first_odds():

def first_odds():
    one = 1
    hundred = 100
    for num in range(one, hundred + 1):
        if num % 2 != 0:
            print(num, end=" ")
#first_odds()

# Question 3: "Write a python function, max_num_in_list to return the max number of a given list."
# def max_num_in_list(a_list)

def max_num_in_list(a_list):
    return max(a_list)
#max_num_in_list("6, 9, 2, 1")



# Question 4: "Write a function to return if the given year is a leap year. A leap year is divisble by 4, but not divisble by 100, unless it is also divisble by 400. The return should be a boolean"
# def is_leap_year(a_year)

def is_leap_year(a_year):
    divisible_by_4 = a_year % 4 == 0
    divisible_by_100 = a_year % 100 == 0
    divisible_by_400 = a_year % 400 == 0
    return divisible_by_4 and (not divisible_by_100 or divisible_by_400)
#is_leap_year(2022)

#print(is_leap_year(2000))

    


# Question 5: "Write a function to check to see if all numbers in list are consecutive numbers. The return should be a boolean"
# def is_consecutive(a_list)

def is_consecutive(a_list):
    counter = 0
    for num in a_list:
        if counter != len(a_list) - 1 and a_list[counter] != a_list[counter + 1] - 1:
            return False
        counter = counter + 1
    return True
print(is_consecutive([1,2,3,4]))

