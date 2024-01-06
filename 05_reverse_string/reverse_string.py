def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse  = '';
    for char in list(   phrase): 
        reverse = char + reverse
    return reverse        

