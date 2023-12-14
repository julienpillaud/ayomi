import operator
from typing import Sequence

from sqlmodel import Session, select

from ayomi.entities.rpn import RPNRecord, RPNRequest


class RPNManager:
    @staticmethod
    def evaluate(session: Session, rpi_request: RPNRequest) -> RPNRecord | None:
        try:
            result = ReversePolishNotation(rpi_request.elements).evaluate()
        except ReversePolishNotationError:
            return None

        db_obj = RPNRecord(elements=" ".join(rpi_request.elements), result=result)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_all(session: Session) -> Sequence[RPNRecord]:
        return session.exec(select(RPNRecord)).all()


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
        if all(x not in self.operators for x in elements):
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
