# Let's start simple. A CLI app that lets me log actions taken in the garden.
# I will try to use TDD and write tests along with the main app.

# ACTIONS:
# 1. Planting
# 2. Weeding
# 3. Harvest
# 4. Other

import os
import datetime

def newLog(action = ""):
    if not action:
        action = str(input("Log tag: "))
    dt_stamp = datetime.datetime.now()
    user_wants_to_write = input(
        "Do you want to write a log entry for this event? [Y/n] ")
    if not user_wants_to_write or user_wants_to_write in "yY":
        dt_stamp = dt_stamp.strftime("%Y%m%d_%H:%M")
        new_log_name = "logstore/" + dt_stamp + "-" + action
        os.system("touch {}".format(new_log_name))
        print(
        "Write your log entry using your favourite editor\n\
save & exit when done.")
        os.system("kate {} &>/dev/null".format(new_log_name))


header = """
GARDENER'S LOG

"""
intro = """
Enter your choice and hit enter to proceed:

"""
choices = """
1. Planting
2. Weeding
3. Harvest
4. Other
"""

print(header + intro + choices)

next_action = input()

# print("Your response was " + next_action)

if next_action not in "1234pwhoPWHO":
    print("\nInvalid choice - please try again.")
    print(choices)
    next_action = input()

if next_action in "1pP":
    newLog("planting")
elif next_action in "2wW":
    newLog("weeding")
elif next_action in "3hH":
    newLog("harvest")
elif next_action in "4oO":
    newLog()
else:
    print("Lee Mack: 'How did that happen!?'")

