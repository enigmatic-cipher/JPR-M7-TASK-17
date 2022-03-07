"""
Given a String as input, replace the "123" by "XYZ" in the string. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "9812398123"
Output-> 98XYZ98XYZ
"""

def recur(st):
  ln = len(st)
  if ln == 0:
    return ""
  ch = st[0]
  if (ch=="1"):
    return "X" + recur(st[1:])
  elif (ch=="2"):
    return "Y" + recur(st[1:])
  elif (ch=="3"):
    return "Z" + recur(st[1:])
  else:
    return ch + recur(st[1:])

st = "9812398123"
print(recur(st))