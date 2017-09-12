import random

tarnum = random.randint(1,20)


i = 10

def num_get():
    print("请输入20以内的整数：")
    global num
    num = input("> ")

def num_check(num):
    """校验是否为20以内的整数"""
    if not num.isdigit():
        return False
    elif not 0 <= int(num) <= 20:
        return False
    elif 0 <= int(num) <= 20:
        return True
    else:
        print("num_check error")
        return False

def num_compare(num,tarnum):
    """比较数值大小"""
    if int(num) < tarnum:
        print("猜得太小啦")
        return False
    elif int(num) > tarnum:
        print("猜得太大啦")
        return False
    elif int(num) == tarnum:
        print("恭喜你猜对啦！正确答案就是 %d !" % tarnum)
        return True
    else:
        print("num_compare error")
        return False

# 数据初始化
num_get()
while not num_check(num):
    num_get()

# 循环输出
while not num_compare(num,tarnum):
    i -= 1
    if i == 0: 
        print("没有机会咯，正确答案是 %d !" % tarnum)
        break
    print("你还有 %d 次机会" % i,)
    num_get()
    while not num_check(num):
        num_get()
