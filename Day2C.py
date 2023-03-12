# 🚨 Don't change the code below 👇
print("Life in Weeks Calculator")
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
life = 90 - int(age)
days = 365 * life
weeks = 52 * life
months = 12 * life
 
print(f"You have {days} days, {weeks} weeks, and {months} months left.")


