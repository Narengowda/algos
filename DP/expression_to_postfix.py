from Stack.stack import Stack
expression = "A+B+C+D"

supported_expr = "*/+-"

postfix = ""

class ExpStack(Stack):

  def priority_push(self, op):
    print("priority push")
    if (not self.is_empty()):
        # Keep pushing expressions
        # if there comes low priority expression
        # and their is hig priority expr in stack
        # remove high priprity and push low priority
      lv = self.last_value()
      opp = supported_expr.find(op)
      lvp = supported_expr.find(lv)
      print(opp, lvp)
      if opp >= lvp:
        val = self.pop()
        self.push(op)
        print("ret =", op)
        return val

    self.push(op)
    return ''

stack = ExpStack()
priority_exp = ''



for exp in expression:
  print(exp, " now in loop")

  if exp in supported_expr:
    priori = stack.priority_push(exp)
    postfix += priori
  else:
    postfix += exp

stack.print()
while not stack.is_empty():
  postfix += stack.pop()

postfix = postfix.replace('', '')
print(postfix)



