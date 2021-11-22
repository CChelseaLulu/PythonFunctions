#defining the functions
def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

#giving the function numbers directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#using variables from the script
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#perfoming calculations in the function
print("We can even do the math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#performing math operators in the argument
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

amount_of_cheese = 45
amount_of_crackers = 100
cheese_and_crackers = (amount_of_cheese,amount_of_crackers)
print("Cheese divided by 10 students, each gets:", amount_of_cheese/10)

cheese_and_crackers()
