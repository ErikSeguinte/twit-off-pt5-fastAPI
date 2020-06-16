from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
home_routes = APIRouter()
templates = Jinja2Templates(directory="twit_off_pt5/templates")


@home_routes.get("/")
async def index(request:Request):
    x = 2 + 2
    return templates.TemplateResponse("predict_form.html", {"request": request})
    return {"x": x, "message":"redirect to home"}
    return redirect(url_for("stats_routes.get_usernames"))


@home_routes.get("/about")
async def about():
    return "About me"
