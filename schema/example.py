from pydantic import BaseModel


class ChangeExamplePostIn(BaseModel):
    id: int
    title: str
    text: str
    dateEnd: str


class ChangeIsDonePostIn(BaseModel):
    id: int
    done: bool
