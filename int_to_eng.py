#Still working on this one

num = 10392867584930275648377
num = str(num)
nums = []
while num != "":
  nums.insert(0,num[-3:])
  num = num[:-3]
print nums

singles = ["", "one","two","three","four","five","six","seven","eight","nine"]
tens = ["", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
uniques = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

test = "876"
test = int(test)
print test
new_string = "{} {} {}".format(singles[test[0]], tens[test[1]], singles[test[2]])