class Example:

    # constructor overloading based on args
    def __init__(self, *args):

        # if args are more than 1 sum of args
        if len(args) > 1:
            self.answer = 0
            for i in args:
                self.answer += i

        # if arg is an integer square the arg
        elif isinstance(args[0], int):
            self.answer = args[0] * args[0]

        # if arg is string Print with hello
        elif isinstance(args[0], str):
            self.answer = "Hello! " + args[0] + "."


e1 = Example(1, 2, 3, 6, 8)
print("Sum :", e1.answer)

e2 = Example(6)
print("Square :", e2.answer)

e3 = Example("Python")
print("String :", e3.answer)