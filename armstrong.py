# program for armstrong number
i = 1042000
j = i
while j < 702648265:

    order = len(str(i))

    sum = 0

    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    # display the result
    if i == sum:
        print(i, "is an Armstrong number")
        break
    else:
        print(i, "is not an Armstrong number")
    j += 1
    i += 1