import operator


class ReversePolishNotationError(Exception):
    pass


class ReversePolishNotation:
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    def __init__(self, elements: list[str]):
        if not any(x in self.operators for x in elements):
            raise ReversePolishNotationError("Must have at least one operator")

        self._stack: list[int] = []
        self.elements = elements

    def _get_operands(self) -> tuple[int, int]:
        if len(self._stack) < 2:
            raise ReversePolishNotationError("Wrong input")
        return self._stack.pop(), self._stack.pop()

    def evaluate(self) -> int:
        for element in self.elements:
            if element not in self.operators:
                self._stack.append(int(element))
            else:
                b, a = self._get_operands()
                ope = self.operators[element]
                self._stack.append(ope(a, b))

        if len(self._stack) > 1:
            raise ReversePolishNotationError("Wrong input")
        return self._stack[0]
