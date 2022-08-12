import random
print("Enter the number of friends joining (including you):")
guest_number = int(input())
guest_list = list()
payers_list = list()
if guest_number > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(guest_number):
        guest = input()
        guest_list.append(guest)
        payers_list.append(guest)
    print("\nEnter the total bill value:")
    total_bill = int(input())
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "Yes":
        lucky_guy = random.choice(guest_list)
        print(f'{lucky_guy} is the lucky one!')
        lucky_split = total_bill / (guest_number - 1)
        payers_list.remove(lucky_guy)
        split_dict = {payer: lucky_split for payer in payers_list}
        split_dict[lucky_guy] = 0
        print(split_dict)
    elif answer == "No":
        print("No one is going to be lucky\n")
        payment = round((total_bill / guest_number), 2)
        equal_dict = {guest: payment for guest in guest_list}
        print(equal_dict)
else:
    print("No one is joining for the party")
