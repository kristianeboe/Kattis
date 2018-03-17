class Expression(object):
  
  def get_chars(self):
    raise NotImplemented

  def evaluate(self, solution):
    raise NotImplemented
  
class AdditionExpression(Expression):

  def __init__(self, first, second, result):
    self.first = first
    self.second = second
    self.result = result
    
  def get_chars(self):
    chars = set()
    for c in self.first:
      chars.add(c)
    for c in self.second:
      chars.add(c)
    for c in self.result:
      chars.add(c)

    return chars

  def solve_rec(self, chars, numbers, mapping, n):
    if n == 0:
      for i in numbers:
        if i not in mapping.values():
          for c in chars:
            mapping[c] = i
            return mapping
    else:
      for i in numbers:
        if i not in mapping.values():
          for c in chars:
            mapping[c] = i
            self.solve_rec(chars, numbers, mapping, n-1)



  def solve(self):
    chars = self.get_chars()
    nrOfChars = len(chars)
    #chars = ['A', 'B', 'C', 'D']
    numbers = [1,2,3,4,5,6,7,8,9,0]

    for i in range(10):
      mapping = self.solve_rec(chars, numbers, {}, nrOfChars)
      print(mapping, self.evaluate(mapping))
      if self.evaluate(mapping):
        return mapping

    # for char in chars:
    #   mapping = {}
    #   for i in numbers:
    #     mapping['A'] = i
    #     for j in numbers:
    #       if j in mapping.values():
    #         continue
    #       mapping['B'] = j
    #       for k in numbers:
    #         if k in mapping.values():
    #           continue
    #         mapping['C'] = k
    #         for l in numbers:
    #           if l in mapping.values():
    #             continue
    #           mapping['D'] = l
    #           print(mapping)
    #           if self.evaluate(mapping):
    #             return mapping

    return "Error"

  def strToNum(self, text, mapping):
    numStr = ""
    print(mapping)
    for c in text:
      if mapping.get(c, 0):
        numStr += str(mapping.get(c))
    try:
      numStr = int(numStr)
    except:
      numStr = 0
    return numStr

  def evaluate(self, solution):

    first = self.strToNum(self.first, solution)
    second = self.strToNum(self.second, solution)
    result = self.strToNum(self.result, solution)

    return ((first + second) == result)

def test1():
  first = "ADD"
  second = "BDD"
  result = "CDD"

  ae = AdditionExpression(first, second, result)
  solution = {'A': 1, 'B':2, 'C':3, 'D':0}
  print(ae.evaluate(solution))


def test2():
  first = "ADD"
  second = "BDD"
  result = "CDD"
  ae = AdditionExpression(first, second, result)
  print('Success', ae.solve())

test2()