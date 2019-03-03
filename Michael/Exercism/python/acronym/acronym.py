def abbreviate(words):
    acronym = ""

    words = words.replace("-", " ").replace("_"," ")
    for word in words.split():
        acronym += word[0].upper()
    
    return acronym

