less = int(input("Please input the number of 1L or less containers: "))
more = int(input("Please input the number of containers larger than 1L: "))

def refund(less, more):
    less_deposit = 0.10
    more_deposit = 0.25
    refund_amount = less * less_deposit + more * more_deposit
    return refund_amount
    
refund_amount = (refund(less, more))
print("Your refund is: $%.2f" % refund_amount)