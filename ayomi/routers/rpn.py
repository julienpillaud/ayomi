from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlmodel import Session

from ayomi.dependencies import get_session
from ayomi.entities.rpn import RPNRecord, RPNRequest
from ayomi.use_cases.rpn import RPNManager

router = APIRouter(prefix="/rpn", tags=["rpn"])


@router.post("/", response_model=RPNRecord, summary="Evaluate the RPN result")
def evaluate(
    *, session: Session = Depends(get_session), rpi_request: RPNRequest
) -> Any:
    result = RPNManager.evaluate(session=session, rpi_request=rpi_request)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong input"
        )
    return result


@router.get(
    "/", response_model=list[RPNRecord], summary="Get records according to filter"
)
def get(
    *, session: Session = Depends(get_session), offset: int = 0, limit: int = 100
) -> Any:
    return RPNManager.get(session=session, offset=offset, limit=limit)


@router.get(
    "/csv", response_class=StreamingResponse, summary="Download csv file of records"
)
def get_csv(*, session: Session = Depends(get_session)) -> Any:
    stream = RPNManager.yield_csv_data(session=session)
    response = StreamingResponse(iter(stream), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=rpn_records.csv"
    return response
