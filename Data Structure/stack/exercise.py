# Implement Stack using collection.deque
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


# 1. Write a function in python that can reverse a string using stack data structure
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
def reverse_string(str): 
    stack = Stack() 
    for ch in str: 
        stack.push(ch)
    
    result = ''
    while stack.size()!=0:
        result += stack.pop()

    return result

# 2. Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]"
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(str): 
    stack = Stack()

    for ch in str: 
        if ch == '{' or ch == '(' or ch == '[': 
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.is_empty():
                return False
            if not is_match(ch, stack.pop()):
                return False
    
    return True;


if __name__ == '__main__':
    # Exercise 1
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))

    # Exercise 2
    print(is_balanced("({a+b})"), 'answer: True')               #  --> True
    print(is_balanced("))((a+b}{"), 'answer: False')            # --> False
    print(is_balanced("((a+b))"), 'answer: True')               # --> True
    print(is_balanced("))"), 'answer: False')                   # --> False
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"), 'answer: True')  # --> True

    

