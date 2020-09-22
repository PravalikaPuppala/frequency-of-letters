def frequency_of_letters(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] = d[key]+1
    return d

word = input("Enter the string: ")
print(frequency_of_letters(word))

