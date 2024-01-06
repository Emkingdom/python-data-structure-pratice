def frequency(numbers, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    frequency = 0
    for number in numbers: 
        if number == search_term:
            frequency = frequency + 1 
    return frequency