from typing import Any

from fastapi import APIRouter, HTTPException, status

from ayomi.entities.rpn import RPNRequest, RPNResponse
from ayomi.use_cases.rpn import ReversePolishNotation, ReversePolishNotationError

router = APIRouter(prefix="/rpn", tags=["rpn"])


@router.post("/", response_model=RPNResponse)
def evaluate(rpi_request: RPNRequest) -> Any:
    try:
        result = ReversePolishNotation(rpi_request.elements).evaluate()
    except ReversePolishNotationError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(err)
        ) from err
    return {"elements": rpi_request.elements, "result": result}
