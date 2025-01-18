## Exercise 1: Pizza Toppings :ballot_box_with_check:

#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

#print a message saying you’ll add that topping to their pizza.

while True:
    topping = input("Enter a topping (or 'quit' to end): ")
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")
