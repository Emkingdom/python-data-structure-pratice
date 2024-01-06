def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    words =  phrase.split()
    
    words_upper = ' '
    
    for word in words:
        
       words_upper.join(word.lower())
    
    return words_upper