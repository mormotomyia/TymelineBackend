from fastapi import FastAPI
from fastapi.routing import APIRoute,APIRouter
from fastapi.responses import JSONResponse
from pydantic.json import pydantic_encoder
import json
from typing import Set,Dict,List,Union,Any

class CustomJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
            default=pydantic_encoder
        ).encode("utf-8")



from src.interfaces.table_data_interface import TableData,Content

router = APIRouter(prefix='/tabledata',tags=['tabledata'],responses={
    500:{"description":"generic backend error"},
    403:{"description":"missing user authorization for this task"},
    400:{"description":"invalid payload"}
})






@router.get('/get/{id}',response_model=TableData)
def get_item_by_id(id:str):
    content = Content(text="hello")
    tableData = TableData(id=id,content=content,start=0,length=100,canMove=False,canChangeLength=True)
    return CustomJSONResponse(tableData)


@router.get('/get/all',response_model=TableData)
def get_item_by_id(id:str):
    content = Content(text="hello")
    tableData = TableData(id=id,content=content,start=0,length=100,canMove=False,canChangeLength=True)
    return CustomJSONResponse(tableData)


