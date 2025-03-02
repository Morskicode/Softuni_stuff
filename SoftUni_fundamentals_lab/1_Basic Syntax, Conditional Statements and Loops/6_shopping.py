budget = int(input())
command = input()

while command != "End":
    price_of_items = int(command)
    budget -= price_of_items
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")