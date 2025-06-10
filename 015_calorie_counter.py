print("Hi, what is your name?")
name = input()

print("Hi " + name + ", what is your calorie goal?")
calorieGoal = int(input())

print ("Enter your breakfast calories")
breakfastCalories = int(input())

print ("Enter your lunch calories")
lunchCalories = int(input())

print ("Enter your dinner calories")
dinnerCalories = int(input())

dailyCalories = breakfastCalories + lunchCalories + dinnerCalories
remainingCalories = calorieGoal - dailyCalories
if remainingCalories > 0:
	print("Great, you have " + str(remainingCalories) + " calories left for today.")
else:
	print("You have reached your calories goal. Your total calories for today is " + str(dailyCalories) + ".")