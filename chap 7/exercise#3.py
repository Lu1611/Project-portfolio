## Exercise 3: T-Shirt  :ballot_box_with_check:

#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

#arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print(f"The shirt is size {size} and has the message '{text}' printed on it.")

make_shirt('M', 'Spider mode!')
make_shirt(size='M', text='La Ciruela')