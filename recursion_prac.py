
# factorial of a number using recursion

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
n= int(input("Enter a number to find its factorial: "))
print(f"the factorial of number is : {factorial(n)}")

# sum of list of numbers using recursion
numbers = [3, 7, 2, 9, 4]

def sum_of_list(numbers):
    if numbers == []:
        return 0
    return numbers[0] + sum_of_list(numbers[1:])

print("The sum of the list is: ", sum_of_list(numbers))

# reverse a string using recursion
word = "claude cheetah"

def reverse_string(word):
    if word == "":
        return ""
    return word[-1] + reverse_string(word[:-1])

print("The reverse of the string is: ", reverse_string(word))

