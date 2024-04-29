from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def first(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})