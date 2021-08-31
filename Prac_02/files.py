"""
1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
"""
out_file = open('name.txt', 'w')

name = input("What is your Name? ")
print("Your name is", name, file=out_file)

"""
2. Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""

out_file = open('name.txt', 'r')
read()
