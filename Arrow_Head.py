#This creates an arrowhead for a list of odd numbers up to value n


n = int(input("Enter any integer: "))
i = 1
x = 1
odd_numbers = []
while i <= n:
    if x % 2 != 0:
        odd_numbers.append(x)
    x += 1
    i += 1

for number in odd_numbers:
    output = " "
    for count in range(number):
        output += "x"
    print(output.center(max(odd_numbers)))


