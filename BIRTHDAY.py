# ASKING USER FOR NAME
name = input("ENTER YOUR NAME\n")
print("NOW THIS SOFTWARE CAN GUESS YOUR BIRTHDATE")
print('''FOLLOW THE FOLLOWING STEPS:- ''')
a = input('''TAKE YOUR BIRTH MONTH NUMBER IN YOUR MIND
IF DONE PRESS ENTER TO CONTINUE''')
a = input('''MULTIPLY IT BY 2
IF DONE PRESS ENTER TO CONTINUE''')
a = input('''ADD 5 TO IT
IF DONE PRESS ENTER TO CONTINUE''')
a = input('''MULTIPY IT BY 5
IF DONE PRESS ENTER TO CONTINUE''')
a = input('''MULTIPLY IT BY 10
IF DONE PRESS ENTER TO CONTINUE''')
a = input('''ADD YOUR BIRTHDATE TO IT
IF DONE PRESS ENTER TO CONTINUE''')
a = int(input('''ENTER YOUR ANSWER\n'''))
date = a%100
date = date - 50
month = a // 100
month = month - 2
if month == 1:
    month = "JANUARY"
elif month == 2:
    month = "FEBRUARY"
elif month == 3:
    month = "MARCH"
elif month == 4:
    month = "APRIL"
elif month == 5:
    month = "MAY"
elif month == 6:
    month = "JUNE"
elif month == 7:
    month = "JULY"
elif month == 8:
    month = "AUGUST"
elif month == 9:
    month = "SEPTEMBER"
elif month == 10:
    month = "OCTOBER"
elif month == 11:
    month = "NOVEMBER"
elif month == 12:
    month = "DECEMBER"
else:
    print("THERE IS AN ERROR IN YOUR CALCULATION")
print(name + "'s BIRTHDAY IS ON", date,"TH OF", month)
print('''THANKS FOR INTERACTING WITH THIS SOFTWARE
MADE BY MAHIR THE CODER''')