from pydantic import BaseModel


class PongResponse(BaseModel):
    echo: str
