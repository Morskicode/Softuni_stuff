divisor = int(input())
boundary = int(input())
max_multiplier = 0
for number in range(1, divisor +1):
    if number % divisor == 0:
        max_multiplier = number
print(max_multiplier)


divisor = int(input())
boundary = int(input())
for number in range (boundary, 0, -1):
    if number % divisor == 0:
        break
print(number)