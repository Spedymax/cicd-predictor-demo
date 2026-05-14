from pydantic import BaseModel


class PingRequest(BaseModel):
    message: str = ""
