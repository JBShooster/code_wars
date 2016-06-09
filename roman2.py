# Much better roman numerals solution!
def solution(roman):
    numerals = {
        "M": 1000,
        "CM": 900,
        "D" : 500,
        "CD": 400,
        "C" : 100,
        "XC": 90,
        "L" : 50,
        "XL": 40,
        "X" : 10,
        "IX": 9,
        "V" : 5,
        "IV": 4,
        "I" : 1
        }
    result = 0
    while len(roman) > 0:
        if roman[0:2] in numerals:
            result += numerals[roman[0:2]]
            roman = roman[2:]
        elif roman[0] in numerals:
            result += numerals[roman[0]]
            roman = roman[1:]
    return result