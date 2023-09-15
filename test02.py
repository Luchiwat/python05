#return not values
#หมายถึง การสิ้นสุดการทำงานของ Block Scope การทำงานนั่นๆ เมื่อทำงาน

def funcA():
    print('AAA')
    print('BBB')
    return
    print('CCC')

def funcB(x):
    return
    print(f'X is {x}')

funcA()
funcB(12)