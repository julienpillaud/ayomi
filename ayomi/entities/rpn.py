from pydantic import BaseModel


class RPNRequest(BaseModel):
    elements: list[str]


class RPNResponse(RPNRequest):
    result: float
