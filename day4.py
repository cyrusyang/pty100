"""
循环结构
"""
import random
def printfor():
    for x in range(2, 100, 2):
        print(x)

def game():
    answer = random.randint(1, 100)
    while True:
        a = int(input("请输入:"))
        if a>answer:
            print("大了")
        elif a<answer:
            print("小了")
        else:
            print("答对了")
            break

game()
    