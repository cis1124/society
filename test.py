# -*- coding:utf-8 -*-
#!/usr/bin/python

time = 0

def study_time(min):
    global time
    time=time+min
    return time

def prac(func):
    def prac_call(*args,**kwargs):
        print("decorator")
        func(*args,**kwargs)
        print("end decorator")

    return prac_call

@prac
def print_decor(args1,args2):
    print(args1)
    print(args2)

def new_counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        print(i)
        return i    
    return count

if __name__=="__main__":
  #    print_decor("aaa","bbb")
    a_count=new_counter()
    b_count=new_counter()
    a_count()
    a_count()
    b_count()

