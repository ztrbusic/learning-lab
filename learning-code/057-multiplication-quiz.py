import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
	# Pick two random numbers
	num1 = random.randint(0, 9)
	num2 = random.randint(0, 9)

	prompt = f"Question {question_number}: {num1} x {num2} = "
	try:
		pyip.inputStr(prompt, allowRegexes=[f"^{num1 * num2}"], blockRegexes=[(".*", "Incorrect")], timeout=8, limit=3)
	except pyip.TimeoutException:
		print("Out of time!")
	except pyip.RetryLimitException:
		print("Out of tries!")
	else:
		print("Correct!")
		correct_answers += 1
	time.sleep(1)
print(f"Score: {correct_answers}/{number_of_questions}")