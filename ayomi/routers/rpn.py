from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from ayomi.dependencies import get_session
from ayomi.entities.rpn import RPNRecord, RPNRequest
from ayomi.use_cases.rpn import RPNManager

router = APIRouter(prefix="/rpn", tags=["rpn"])


@router.post("/", response_model=RPNRecord)
def evaluate(
    *, session: Session = Depends(get_session), rpi_request: RPNRequest
) -> Any:
    result = RPNManager.evaluate(session=session, rpi_request=rpi_request)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong input"
        )
    return result


@router.get("/", response_model=list[RPNRecord])
def get_all(*, session: Session = Depends(get_session)) -> Any:
    return RPNManager.get_all(session=session)
