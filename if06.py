def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    main_positive=0
    main_negative=0
    if a>0:
        main_positive+=1
    elif a<0:   
        main_negative+=1 
    if b>0:
        main_positive+=1    
    elif b<0:
        main_negative+=1
    if c>0:
        main_positive+=1
    elif c<0:
        main_negative+=1            
    return main_positive, main_negative
print(main(4,-6,2))