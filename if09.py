def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    X_digit=a//10
    Y_digit=a%10
    Z=Y_digit*10+X_digit
    if Z<=a:
        return True
    else:
        return False
print(main(89))