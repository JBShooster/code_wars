# The highly inefficient solution
def solution(roman):
    result = 0
    first_two = roman[0:2]
    while len(roman) > 0:
        if first_two == "CM":
            result += 900
            roman = roman[2:]
        elif first_two == "CD":
            result += 500
            roman = roman[2:]
        elif first_two == "XC":
            result += 90
            roman = roman[2:]
        elif first_two == "XL":
            result += 40
            roman = roman[2:]
        elif first_two == "IX":
            result += 9
            roman = roman[2:]
        elif first_two == "IV":
            result += 4
            roman = roman[2:]
        elif roman[0] == "M":
            result += 1000
            roman = roman[1:]
        elif roman[0] == "D":
            result += 500
            roman = roman[1:]
        elif roman[0] == "C":
            result += 100
            roman = roman[1:]
        elif roman[0] == "L":
            result += 50
            roman = roman[1:]
        elif roman[0] == "X":
            result += 10
            roman = roman[1:]
        elif roman[0] == "V":
            result += 5
            roman = roman[1:]
        elif roman[0] == "I":
            result += 1
            roman = roman[1:]
    return result