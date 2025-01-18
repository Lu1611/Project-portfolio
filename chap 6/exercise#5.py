## Exercise 5: No Pastrami :ballot_box_with_check:

#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 

#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['cheese', 'pastrami', 'sausage', 'pastrami', 'mozarella', 'pastrami', 'ham and cheese', 'turkey']
print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I'm working on your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches are ready:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")