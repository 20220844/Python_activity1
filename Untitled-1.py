#Activity 1
from tkinter import E


in_human_year=int(input("Input a dog's age in human years:"))
if in_human_year<=int(2):
    print(("The dog's age in dog's years is:"), in_human_year*10.5)
else: print(("The dog's age in dog's year is"),((in_human_year-2)*4+21))

#Activity 2
month=input("Input the name of the Month:")
if month:="January" or"March" or"May"or"July"or"August"or"December":
    print("No. of days:31 days")
elif month:="April"or"June"or"September"or"November":
    print("No. of days:30 days")
else: print ("No. of days:28/29 days")
     