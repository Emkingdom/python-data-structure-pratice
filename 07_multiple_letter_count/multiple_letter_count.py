def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    leter_frequency = {}
    
    for char in phrase:
        if char in leter_frequency: 
            leter_frequency[char] = leter_frequency[char] +1
        else:
             leter_frequency[char] = 1
    return leter_frequency      
