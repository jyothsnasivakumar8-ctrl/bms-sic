import pdb
pdb.set_trace()

input_number=int(input("enter number to find lucky number:"))
original_number=input_number
sum_of_digits=0
while input_number!=0:
    remainder=input_number%10
    input_number=input_number//10
    sum_of_digits=sum_of_digits+remainder
    if sum_of_digits>9 and input_number==0:
        input_number=sum_of_digits
        sum_of_digits=0
print("original number is:",original_number)
print("lucky number is:",sum_of_digits)