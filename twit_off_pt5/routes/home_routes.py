from fastapi import APIRouter

home_routes = APIRouter()


@home_routes.get("/")
async def index():
    x = 2 + 2
    return {"x": x, "message":"redirect to home"}
    return redirect(url_for("stats_routes.get_usernames"))


@home_routes.get("/about")
async def about():
    return "About me"
