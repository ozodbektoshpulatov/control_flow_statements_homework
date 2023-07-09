def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    main=0
    if a<0:
        main+=1
    if b<0:
        main+=1    
    if c<0:
        main+=1    

    return main
print(main(-6,-4,2))