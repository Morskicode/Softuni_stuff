number_of_numbers = int(input())

for i in range (number_of_numbers):
    number = int(input())
    if not  number % 2 == 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")

