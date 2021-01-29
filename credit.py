from cs50 import get_int


def nepar(i, num):
    sum1 = 0
    x = 100
    z = 10
    for counter in range(i, -1, -1):
        if counter % 2 != 0:
            d = 0
            a = 0
            b = 0
            d = num % x
            d //= z
            s = d * 2
            if s > 9:
                a = s // 10
                b = s % 10
                sum1 = sum1 + a + b
            else:
                sum1 += s
            z *= 100
            x *= 100
    return sum1


def par(i, num):
    sum2 = 0
    x = 10
    z = 1
    for counter in range(i, -1, -1):
        if counter % 2 == 0:
            d = 0
            d = num % x
            d //= z
            sum2 += d
            z *= 100
            x *= 100
    return sum2


number = get_int("Number: ")
work = number
counter = 0
ret1 = 0
ret2 = 0
suma = 0

while work != 0:
    counter += 1
    work //= 10

print(counter)

if counter < 13 or counter == 14 or counter > 16:
    print("INVALID")

if counter == 15:
    first = number // 100000000000000
    second = (number // 10000000000000) % 10
    if first == 3 and (second == 4 or second == 7):
        ret1 = nepar(counter, number)
        ret2 = par(counter, number)
        suma = ret1 + ret2
        if suma % 10 == 0:
            print("AMEX")
        else:
            print("INVALID")
    else:
        print("INVALID")

if counter == 16:
    first = number // 1000000000000000
    second = (number // 100000000000000) % 10
    if first == 4:
        ret1 = nepar(counter, number)
        ret2 = par(counter, number)
        suma = ret1 + ret2
        if suma % 10 == 0:
            print("VISA")
        else:
            print("INVALID")
    elif (first == 5 and (second == 1 or second == 2 or second == 3 or second == 4 or second == 5)) or (first == 2 and second == 2):
        ret1 = nepar(counter, number)
        ret2 = par(counter, number)
        suma = ret1 + ret2
        if suma % 10 == 0:
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")

if counter == 13:
    first = (number // 1000000000000) % 10
    if first == 4:
        ret1 = nepar(counter, number)
        ret2 = par(counter, number)
        suma = ret1 + ret2
        if suma % 10 == 0:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")