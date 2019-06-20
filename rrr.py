import random
b = []
while 1:
    a = [2,3,4]

    choice = random.choice(a)
    if choice not in b:
        b.append(choice)
        print(b)
        if len(b) == len(a):
            print('爬取失败')
            break
a = [2,3,4]
while 1:
    print(a.pop())
    print(a)
    if len(a) == 0:
        print('爬取失败')
        break