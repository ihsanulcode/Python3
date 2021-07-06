'''
3.
Write a program for a super shop. Take 10
products name, Total quantity, and each unit price as input and finally calculate
the total bill for the buyer.
Sample one input-output:
Input:
Sugar
10
90

Output: Sugar price is 900'''


product_name = []
product_quantity = []
product_price = []

for i in range(1,11):
    name = str(input())
    product_name.append(name)
    quantity = float(input())
    product_quantity.append(quantity)
    price = float(input())
    product_price.append(price)

for i in range(10):
    print(str(product_name[i]) + " price is "+str(float(product_quantity[i])*float(product_price[i])))