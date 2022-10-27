def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    nums = []
    
    while not n in nums:
        
        nums.append(n)
        
        n = sum([int(i) ** 2 for i in str(n)])
        
        
        if n == 1:
            return True
        
        
    return False


print(isHappy(19))
