# A bag of cookies holds 40 cookies.
# The calorie information on the bag claims that there are 10 servings in the bag and that a serving equals 300 calories.
# Write a program that lets the user enter the number of cookies he or she actually ate and then reports the number of total calories consumed.

# determine how many calories per cookie
# 40 cookies = 10 servings, 4 cookies = 1 serving, 4 cookies = 300 calories, 1 cookie = 75 calories
calories_per_cookie = 75

# ask user to input the number of cookies they ate and cast it to an int
cookies_eaten = int(input("How many cookies did you eat? "))

# calculate how many calories the user consumed
calories_consumed = str(calories_per_cookie * cookies_eaten)

# display the result
print("That was " + calories_consumed + " calories! Wowzers!")