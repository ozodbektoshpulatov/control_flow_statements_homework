def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2!=0:
        return "positive odd number"  
    elif a>0 and a%2==0:
        return "positive even numebr"  
    elif a<0 and a%2!=0:
        return "negative odd numebr"
    elif a<0 and a%2==0:
        return "negative even numebr"
    elif a==0:
        return "the number is zero"
    return a
print(main(-9))