import partition as pt
import sys
numbers = []
numbers = [int(value) for value in sys.argv[1:]]
print("number befor partition: \n",numbers)
pt.partition_array(numbers)
print("numbers after partition \n", numbers)