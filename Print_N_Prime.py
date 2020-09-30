# n = int(input("Enter any number: "))
# prime = 2
# while n != 0:
#     for value in range(2,prime):
#         if prime % value == 0:
#             break
#     else:
#         print(prime, end=' ')
#         n -= 1
#     prime += 1


# max_value = int(input("Enter any number: "))
# for value in range(2,max_value+1):
#     for check_factor in range(2,value):
#         if value % check_factor == 0:
#             break
#     else:
#         print(value)

n = int(input("Enter any number: "))
counter = 0
prime = 2
while counter < n:
    for value in range(2,prime):
        if prime % value == 0:
            break
    else:
        print(prime, end=' ')
        counter += 1
    prime += 1