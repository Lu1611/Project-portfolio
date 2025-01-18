## Exercise 3: Glossary 2 :ballot_box_with_check:
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'string': 'A sequence of characters.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A control flow statement that repeatedly executes a block of code.',
    'list': 'A data structure that stores a collection of items in a specific order.',
    'function': 'A block of code that performs a specific task.',
    'tuple': 'A collection of items that cannot be changed.',
    'set': 'A collection of items that are unique.',
    'comment': 'A note in a program that the interpreter ignores.',
    'module': 'A file containing Python code that can be imported and used in other programs.',
    'class': 'A blueprint for creating objects.'
}

for key, value in glossary.items():
    print(f"\n{key.title()}: {value}")