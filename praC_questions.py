'''

Ask the user to enter 5 numbers, store them in a list, and then print the list in reverse order (without using slicing, only .reverse()).
# '''
# numbers = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num) 
# numbers.reverse()
# print("Reversed list:", numbers)'''

'''
Take marks of 6 students, store them in a list, and then:

'''
# mark = []
# for i in range(6):
#     m = float(input("Enter marks of student: "))

#     if m > 100.0 or m < 0.0:
#         print("Invalid marks, please enter marks between 0 and 100.")
#         continue

#     mark.append(m)
#     print("Marks list:", mark)

# def sorted_marks():
#     mark.sort()
#     print("Sorted marks:", mark)
# sorted_marks()

# def highest_marks():
#     highest = max(mark)
#     print(f"Highest marks: {highest}")
# highest_marks()

# def lowest_marks():
#     lowest = min(mark)
#     print(f"Lowest marks: {lowest}")
# lowest_marks()

'''
Q3: Shopping Cart

Make an empty list cart.

Keep asking the user to add an item until they type "done".

After that, print all items in the cart.

Then remove the last added item using .pop() and show the updated cart.
'''

cart=[]

while True:
    item =input("add item to cart (type 'done' to finish): ")
    if item.upper() == "DONE":
        break
    cart.append(item)
print("Items in cart:", cart)

def remove_last_item():
    if cart:
        removed_item = cart.pop()
        print(f"Removed last item: {removed_item}")
    else:
        print("Cart is empty, nothing to remove.")
    print("Updated cart:", cart)

remove_last_item()

