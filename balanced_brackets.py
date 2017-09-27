brackets = {'{': '}', '[': ']', '(': ')'}


def is_matched(expression):
    balance_stack = []
    if expression:
        for e in expression:
          pair = brackets.get(e)
          if pair:
              balance_stack.append(pair)
          elif not balance_stack or balance_stack.pop() != e:
              return False

        return not balance_stack


if __name__ == '__main__':

    input = '{[()]}'
    if is_matched(input) == True:
        print("YES")
    else:
        print("NO")
