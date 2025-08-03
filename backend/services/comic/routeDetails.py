from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from appUtils import createCustomResponse
from services.comic.schemas import *
from utilities.firebaseApp import db
from google.cloud.firestore_v1.base_query import FieldFilter
import calendar

router = APIRouter(
    prefix="/comics",
    tags=["comics"]
)

@router.get("/getComicByMonth")
async def getComicByMonth(month: int, year: int):
    try:
        comicsRef = db.collection("comics")
        query = comicsRef.where(
            filter=FieldFilter("coverMonth", "==", calendar.month_name[month])
        ).where(filter=FieldFilter("coverYear", "==", year)).get()
        print(query)
        return createCustomResponse({
            "ok": "tested"
        })
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")