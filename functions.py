# -------------------------------------------- 

	# You've just learned about functions.
	# Functions are reusable pieces of code that make your code more modular.
	
	# If you are writing the same bit of code over and over, you are doing more work that you have to.
	# Use functions to simplify your code and decrease the amount of work you're doing. 

	# Any time you start thinking 'this is tedious', you can probably write a function for that task.

# -------------------------------------------- 


# -------------------------------------------- 
  # Challenge 1: Let's try to write some basic functions.
# -------------------------------------------- 

# print("------------------- Challenge 1 -------------------")

# **** Challenge 1: Problem 1 ****
# Write a function called print_message() that prints any message you want.

def print_message(message):
	return(message)
print(print_message("hey what's up?"))

# print("Challenge 1: Problem 2 ****")
# Write a function called print_five_messages() that calls print_message() five times.

def print_five_messages(print_message):
	return(print_message + print_message + print_message + print_message + print_message)
print(print_five_messages("hey what's up?"))


# **** Challenge 1: Problem 3 ****
# Write a function called get_user_input() that asks the user if they'd like to print your message
# once or five times. Then call one of the two functions above based on what the user decides.

def get_user_input(print_message, print_five_messages, user_response):
	if user_response == "1 time":
		return(print_message)
	if user_response == "5 times":
		return(print_five_messages)
print(get_user_input("hey what's up?", "hey what's up?", "5 times"))
	

# **** Challenge 1: Problem 4 ****
# Write a function called print_greeting() that prints a greeting message to the user.

def print_greeting(greeting):
	return(greeting)
print(print_greeting("hello"))


# **** Challenge 1: Problem 5 ****
# Write a function called print_closing() that prints a goodbye message to the user.
def print_closing(closing):
	return(closing)
print(print_closing("goodbye"))

# **** Challenge 1: Problem 6 ****
# Write a function called run() that greets the user, asks them for input, and sends a goodbye message.
# Remember! Use the functions that you've already made. Don't hardcode anything!


def run(print_greeting, print_closing, INput):
	return(print(print_greeting, print(type(INput)), print(print_closing))
print(run("hello", "goodbye", input("gimme some input")))
# -------------------------------------------- 

# Challenge 2: Functions are also able to take input and return output. 
				# The value(s) you pass to it are called parameters.

# -------------------------------------------- 

# print("------------------- Challenge 2 -------------------")

# **** Challenge 2: Problem 1 ****

# Write a function called sum_double that takes two number paramters and returns their sum.
# However, if the two values are the same, the funciton will return double their sum.

	# Examples:
		# sum_double(1, 2) → 3
		# sum_double(3, 2) → 5
		# sum_double(2, 2) → 8

# -------------------------------------------- 


def sum_double(a, b):
	if a == b:
		return (a + b) * 2
	return a + b
print(sum_double (1, 2))




# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 2 ****

# Write a function called makes_10 that takes two numbers, a and b, and returns true if one of them is 10 or if their sum is 10.

	# Examples:
		# makes_10(9, 10) → True
		# makes_10(9, 9) → False
		# makes_10(1, 9) → True

# -------------------------------------------- 

def makes_ten(a, b):
	if a or b == "10":
		return("true")
	if int(a + b) == 10:
		return("true")
	return("false")
print(makes_ten(1, 10))

 



# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 3 ****

# Write a function that will return the time our alarm is set to go off.

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string in the form "7:00" indicating
# when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
# the weekend it should be "10:00". However, if we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".
	# Examples:
		# alarm_clock(1, False) → "7:00"
		# alarm_clock(6, True) → "off"
		# alarm_clock(0, False) → "10:00"

# -------------------------------------------- 
def alarmClock(dayOfWeek, Vacation):
	if dayOfWeek <= 5 and Vacation == "no":
		return("7:00")
	if (dayOfWeek >= 5 and Vacation == "no") or (dayOfWeek <= 5 and Vacation == "yes"):
		return("10:00")
	if (dayOfWeek >= 5 and Vacation == "yes"):
		return("off")
print(alarmClock(4, "no"))







# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 4 ****

# Write a function that will tell you if you received a speeding ticket.
# You are driving a little too fast, and a police officer stops you. 

# To compute the result, encoded as a number value: 
	# 0=no ticket
	# 1=small ticket
	# 2=big ticket
# If speed is 60 or less, the result is 0. 
# If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2.

# -------------------------------------------- 

def speedingTicket(speed):
	if speed < 60:
		return(0)
	elif (speed > 60) and (speed < 80):
		return(1)
	return 2
print(speedingTicket(90 ))






# Make sure to test your code! Write a few function calls to make sure your code works!
