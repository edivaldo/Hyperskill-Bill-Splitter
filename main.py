import random

n = int(input("Enter the number of friends joining (including you):"))
dinner = {}
if n <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(n):
        dinner[input()] = 0
    bill = float(input("Enter the total bill value:"))
    yes_no = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if yes_no == "Yes":
        lucky = list(dinner.keys())[random.randint(0, len(dinner)-1)]
        print(f"{lucky} is the lucky one!")
        for i in dinner:
            if lucky == i:
                dinner[i] = 0
                continue
            dinner[i] = round(bill/(n-1), 2)
        print(dinner)
    else:
        print("No one is going to be lucky")
        for i in dinner:
            dinner[i] = round(bill/n, 2)
        print(dinner)