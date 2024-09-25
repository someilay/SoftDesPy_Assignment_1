from op import make_operator
from plugin import Plugin


@make_operator("Sum of a and b", a="first number", b="second number")
def add(a: int, b: int):
    return a + b


plugin = Plugin("add", add)
