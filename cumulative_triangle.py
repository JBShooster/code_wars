def cumulative_triangle(n):
  count = 1
  result = 0
  for x in range(1, n):
    count = count + x
    x +=1
  end = count + n-1
  for y in range(count, end+1):
    result += y
  return result