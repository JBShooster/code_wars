def is_isogram(string):
    results = []
    string = list(string.lower())
    for x in string:
        if x not in results:
            results.append(x)
        else:
            return False
    return True