## Exercise 1:  Alien Colors #1 :ballot_box_with_check:

#Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

#•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

#•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color = ["green", "yellow", "red"]
for alien in alien_color:
    if alien == "green":
        print("congratulations, you just earned 5 points")
    else:
        print()

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")