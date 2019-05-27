import random
i = 0
while i < 3:
    guess = int(input("请输入你要猜的数:\n"))
    computer_num = random.randint(1, 5)
    if guess == computer_num:
        print("you got it")
    else:
        if guess > computer_num:
            print("bigger")
        else:
            print("less")
    i += 1
print("错误超过三次, 程序正在退出")
