"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score > 50:
    if score > 100:
        print("Invalid score")
    if 50 < score < 90:
        print("Passable")
    if 90 <= score <= 100:
        print("Excellent")
else:
    print("Bad")