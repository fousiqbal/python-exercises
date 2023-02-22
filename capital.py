def capital(name):
    first_letter = name[0]
    inbetween = name[1:3]
    last_letter = name[3]
    rest = name[4:]
    return first_letter.upper() + inbetween + last_letter.upper() + rest
capital("programming")

