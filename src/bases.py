import math

# This function takes a positive or negative integer n,
# and converts it to a negative base. The value returned is a list.
def dec_to_base(n: int, base: int):
    if (type(n) is not int):
        raise Exception('Error: Provided a non-int value.')     

    if (n == 0):
        return '0'   
    
    # str is the value to be returned, made of 1s and 0s,
    # representing base -2.
    converted = []
    while (n != 0):
        remainder: int = int(n % base)
        n = int(math.floor(n / base))

        if remainder < 0:
            remainder += 2
            n += 1

        converted.insert(0, remainder)

    return converted