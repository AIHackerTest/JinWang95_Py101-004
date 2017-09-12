import random

i = 10
# num = '1'


def num_get():
    print("请输入1000至9999的四位整数：")
    global num
    num = input("> ")


def num_check(num):
    """校验输入是否为1000至9999的四位整数"""
    if not num.isdigit():
        return False
    elif not 1000 <= int(num) <= 9999:
        return False
    elif 1000 <= int(num) <= 9999:
        return True
    else:
        print("num_check error")
        return False


def create_numlist():
    """生成四位数列表"""
    numlist = [random.randint(1,9)]
    k = 1
    for k in range(1,4):
        n = random.randint(0,9)
        while n in numlist:
            n = random.randint(0,9)
        numlist.append(n)
        k += 1
    return numlist


def create_inputlist():
    """将输入数字转换为列表"""
    int_num = int(num)
    num_len = len(num)
    inputlist = []
    while num_len > 0:
        n = int_num // 10**(num_len-1)
        inputlist.append(n)
        int_num -= n*10**(num_len-1)
        num_len -= 1
    return inputlist

def compare_list(numlist,inputlist):
    """比较生成列表与输入列表，输出比较结果"""
    listlen = len(numlist)
    k = 0
    a_num = 0
    c_num = 0
    for k in range(0,listlen):
        if inputlist[k] in numlist:
            c_num += 1
        if inputlist[k] == numlist[k]:
            a_num += 1
        k += 1 
    return a_num,c_num-a_num

# 数据初始化
numlist = create_numlist()
num_get()
while not num_check(num):
    num_get()
inputlist = create_inputlist()
a_num,b_num = compare_list(numlist,inputlist)

# 判断输出
while a_num != 4 or i == 10:
    print("%dA%dB" % (a_num,b_num))
    i -= 1
    if i == 0: 
        print("没有机会咯，正确答案是",numlist)
        break
    print("你还有 %d 次机会" % i,)

    num_get()
    while not num_check(num):
        num_get()
    inputlist = create_inputlist()
    a_num,b_num = compare_list(numlist,inputlist)

if a_num == 4:
    print("恭喜你猜对了，正确答案就是 %s !" % num)
