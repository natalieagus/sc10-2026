# we are building a "space" (object) to store items (data)
# we also are implementing methods to get an item out and to put an item in
class Stack: # LIFO
    def __init__(self) -> None:
        self.__items = []
        # don't we do this:
        # self.items: list[Any] = []
        # this is because items is a private variable that should not be accessed by any code outside of this class' methods
        # intuition: items in the stack cannot be directly accessed, you need to either always put thngs on top of the stack or remove things from the top of the stack

    def push(self, item):
        # `push(item)` which stores an item into the top of the stack.
        self.__items.append(item) # choose the back of the list as the top of the stack
        # alternative 1: self.__items.insert(item)
        # alternative 2: self.__items.append(item)

    def pop(self):
        # does the opposite of push, which is to REMOVE item from the top of the stack (aka the back of the list)
        # need to check first if there's item in the stack
        if (len(self.__items)) >= 1:
            # make sure when we call list.pop(), the list is NOT empty
            # otherwise we need to handle the error
            return self.__items.pop()
            # alternative 1: return self.items.pop(0)
            # alternative 2: return self.__items.pop(len(self.__items)-1)


    def peek(self):
        # just see only
        if (len(self.__items)) >=1:
            return self.__items[-1] # this does not remove the item from the stack

    @property
    def is_empty(self) -> bool:
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)

class EvaluatePostfix:

    operands: str = "0123456789"
    operators: str = "+-*/"

    def __init__(self) -> None:
        self.expression: list[str] = []
        self.stack: Stack = Stack()

    def input(self, item: str) -> None:
        # pushes the input one at a time
        # push to the expression
        # 1 2 + 3 * becomes
        # [*, 3, +, 2, 1] because we insert at 0
        # you can also append instead of insert 0, but the evaluate logic will be different
        self.expression.insert(0, item)

    def evaluate(self):
        # if it is a number, push to the stack
        # if it is an op, pop the top 2, apply the op, push back to stack
        # while there's still something in the expression
        while len(self.expression) != 0:
            item = self.expression.pop() # get from the end of the list
            # if it is an op, then apply the logic
            if len(item) == 1 and item in self.operators:
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                result = self._process_op(op1, op2, item)
                self.stack.push(result)
            else:
                # we have a number, put to stack directly
                self.stack.push(int(item)) # convert to number
        return self.stack.pop() # there should be just one item (number) in the stack at this point

    # helper method to process operation
    def _process_op(self, op1, op2, operator):
        if operator == "+":
            return op1+op2
        if operator == "-":
            return op1-op2
        if operator == "*":
            return op1*op2
        if operator == "/":
            return op1/op2
        return 0.0


pe: EvaluatePostfix = EvaluatePostfix()
pe.input("2")
pe.input("3")
pe.input("+")
assert pe.evaluate()== 5

pe.input("2")
pe.input("3")
pe.input("+")
pe.input("6")
pe.input("-")
assert pe.evaluate()== -1
