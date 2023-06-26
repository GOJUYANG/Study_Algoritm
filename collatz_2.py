def collatz(num):
    if num % 2 == 0:
        return collatz(num // 2)
    elif num % 2 != 0:
        return collatz(3 * num + 1)
    elif num == 1:
        return print(num)

num = 2
while True:
    collatz(num)
    num += 1
