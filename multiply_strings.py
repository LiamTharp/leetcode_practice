def multiply(num1: str, num2: str) -> str:
    
    product = [0] * (len(num1) + len(num2))
    
    for idx, i in enumerate(reversed(num1)):

        for jdx, j in enumerate(reversed(num2)):

            product[idx+jdx] += int(i) * int(j)

            product[idx + jdx + 1] += product[idx + jdx] // 10

            product[idx + jdx] %= 10

    
    out = ''.join(map(str, reversed(product))).lstrip('0')
    
    return out if len(out) > 0 else '0'


print(multiply('999','999'))
print(multiply('3','2'))
print(multiply('0','0'))

