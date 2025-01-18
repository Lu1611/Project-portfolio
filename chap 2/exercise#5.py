#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

#You will to use the arithmetic operators to complete this exercise.

Budget = 50
Price1 = 6
number_of_sticks = Budget // Price1
Change = Budget % Price1
print(f"She can have {number_of_sticks} USB sticks and have £{Change} as her change.")
