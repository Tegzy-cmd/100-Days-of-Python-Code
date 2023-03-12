#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculator")

bill = float(input("What was your total bill? $:"))
tip = int(input("how much tip would you like to give e.g 10, 12 or 20: "))
split = int(input("Number of people to split bill: "))

tipPercentage = tip/100
totalTip = bill * tipPercentage
totalBill = bill + totalTip
billPerPerson = round(totalBill /split,2)

print(f"each person is expected to pay {billPerPerson}")
