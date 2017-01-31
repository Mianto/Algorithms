def exponent(x,n):
    if n == 0:return 1
    elif n == 1:return x
    elif n%2 == 0:
        return exponent((x*x),n/2)
    else:
        return x*exponent((x*x), (n-1)/2)


def expo(x, n):
    result = 1
    while (n):
        if(n & 1):
            result = result * x
        n >>= 1
        x *= x
    return result


print expo(10, 100)
