from sqlmodel import Field, SQLModel


class RPNRequest(SQLModel):
    elements: list[str]


class RPNRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    elements: str
    result: float

    @property
    def csv(self) -> str:
        return f"{self.id},{self.elements},{self.result}"
