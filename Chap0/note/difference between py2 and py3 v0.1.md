# 探索python2和3的区别

## print
### 基础语法
- py2:

        print "string"


- py3:
    
        print("string")

### 不打印回车
- py2:

        print("string",)

- py3:

        print("string",end='')


---
## 整除
- py2:

        assert 2 / 3 == 0

- py3:

        assert 2 // 3 == 0


---
## raise exception
### 基础语法
- py2:

        raise ValueError,"dodgy value"

- py3:

        raise ValueError("dodgy value")
### Raising exceptions with a traceback
(尚未学习)

## py3只有一个默认的长整型，取消了短整型


## range
- py2:

        mylist = range(5)
        assert mylist == [0,1,2,3,4]

- py3:
        
        mylist = list(range(5)
        assert mylist == [0,1,2,3,4]


## file IO with open
- py2:

        f = open('myfile.text') # or f = file(pathname)
        data = f.read()
        text = data.decode('utf-8')

- py3:

        f = open('myfile.txt','rb')
        data = f.read() # as bytes
        text = data.decode('utf-8') # unicode,not bytes
        # or
        f = open('myfile.txt', encoding='utf-8')
        text = f.read   # unicode,not bytes
        

## raw_input()、input()
- py2:

        name = raw_input('What is your name?')
        assert isinstance(name,str)
        
        input("Type something safe please: ")
        
- py3:

        name = input("What is your name?")
        assert isinstance(name,str)
        
        eval(input("Type something safe please: ")