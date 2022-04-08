from datetime import datetime
user_input = input("enter your goal and the deadline with the colon separation\n")
list_of_input = user_input.split(":")
goal = list_of_input[0]
deadline = list_of_input[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.today()
days_left = deadline_date - today
print(f"the number of days left to complete my goal is {days_left.days} days")
#adding some more feature
