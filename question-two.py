#2(d)
def average(num1,num2,num3):
    avg = ((num1) + (num2) + (num3)/3)
    return print('Average of the 3 numbers is:',avg)

#calling the function with given parameters
average(2,3,7)    



#2(e)

def itemPriceDiscount():
    discount = 20
    cost_price = float(input('Enter the price of the item ')) #converting user price to  float
    if(cost_price<0.05):
        print('Enter a cost price above $0.05')
    else:
        cost_price = cost_price    

        discounted_price = (cost_price*discount)/100
        return print('Starting Price and Discounted price are respectively:',cost_price , discounted_price)

#calling the item function
itemPriceDiscount()    