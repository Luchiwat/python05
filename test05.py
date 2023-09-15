def A():
    ID = input("รหัสพนักงาน: ")
    NAME = input("ชื่อพนักงาน: ")
    ML = float(input("เงินเดือนปกติของพนักงาน: "))
    return ID, NAME, ML

def B(ML):
    PC = 7  
    TAX = (ML * PC) / 100
    return TAX

def C():
    SSF = 500
    return SSF

def D(ML, TAX, SSF):
    NS = ML - TAX - SSF
    return NS

def E(ID, NAME, ML, TAX, SSF, NS):
    print(f"รหัสพนักงาน : {ID}")
    print(f"ชื่อพนักงาน : {NAME}")
    print(f"เงินเดือนปกติ : {ML:.2f} บาท")
    print(f"ภาษีเป็นเงิน : {TAX:.2f} บาท")
    print(f"ค่าเบี้ยประกันสังคม : {SSF:.2f} บาท")
    print(f"เงินเดือนสุทธิเป็นเงิน : {NS:.2f} บาท")

print("=================================")
print("====== คำนวณเงินเดือนพนักงาน =======")
print("=================================")
ID, NAME, ML = A()
print("=================================")
TAX = B(ML)
SSF = C()
NS = D(ML, TAX, SSF)
E(ID, NAME, ML, TAX, SSF, NS)
print("=================================")