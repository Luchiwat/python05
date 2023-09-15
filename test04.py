def inputData():
    no1=float(input('โปรดป้อนค่าตัวที่ 1 : '))
    no2=float(input('โปรดป้อนค่าตัวที่ 2 : '))
    no3=float(input('โปรดป้อนค่าตัวที่ 3 : '))
    no4=float(input('โปรดป้อนค่าตัวที่ 4 : '))
    no5=float(input('โปรดป้อนค่าตัวที่ 5 : '))
    return no1,no2,no3,no4,no5

def calSumOfNumber(no1,no2,no3,no4,no5 ) :
    sumOfNumber = no1+no2+no3+no4+no5
    return sumOfNumber

def calAverageOfNumber( no1,no2,no3,no4,no5) :
    averageOfNumber = ((no1+no2+no3+no4+no5)/5)
    return averageOfNumber

def showDataAndSumAndAverageOfNumber( no1,no2,no3,no4,no5,sumOfNumber,averageOfNumber) :
    print(f'number 1 is {no1}')
    print(f'number 2 is {no2}')
    print(f'number 3 is {no3}')
    print(f'number 4 is {no4}')
    print(f'number 5 is {no5}')
    print('=================================')
    print(f'Sum of 5 number is {sumOfNumber}')
    print(f'Average of 5 number is {averageOfNumber:.4f}')

print('==========================================')
print('         Program Average 5 Number         ')
print('==========================================')
no1,no2,no3,no4,no5 = inputData( )
sumOfNumber = calSumOfNumber(no1,no2,no3,no4,no5 )
averageOfNumber = calAverageOfNumber( no1,no2,no3,no4,no5)
print('==========================================')
showDataAndSumAndAverageOfNumber(no1,no2,no3,no4,no5,sumOfNumber,averageOfNumber)
print('==========================================')