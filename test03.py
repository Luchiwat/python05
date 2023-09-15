def inputData( ):
    productroduct_name = input('ชื่อสินค้า : ')
    product_price = float(input('ราคาสินค้า : '))
    return product_name, product_price

def calproduct():
    product_sale= product_price + (product_price * 10 / 100)
    return product_sale

def showproductSale(product_name,product_princ,product_sale):
    print(f'ชื่อสินค้า {product_name}')
    print(f'ราคาสินค้า {product_price:.2} บาท')
    print(f'ราคาขายสินค้า {product_sale:.2} บาท')

print('------------------')
print('--*productduct Sale*--')
print('------------------')
product_name,product_price = inputData( )
product_sale = calproduct (product_price)
print('------------------')
showproductSale(product_name, product_price, product_sale)
print('------------------')
    