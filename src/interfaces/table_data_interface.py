# from pydantic.datatclasses import dataclass
from typing import Set,Dict,List,Union
from pydantic import dataclasses

@dataclasses.dataclass(frozen=True,order=True)
class Content:
    text:str


@dataclasses.dataclass(frozen=True,order=True)
class TableData:
    id:Union[str,int]
    length:Union[int,float]
    content:Content
    start:int
    canChangeLength:bool
    canMove:bool