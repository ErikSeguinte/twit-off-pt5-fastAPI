__version__ = "0.1.0"

from fastapi import FastAPI, Request, Depends, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .routes.home_routes import home_routes
from .routes.twitter_routes import twitter_routes
import uvicorn


# db_path = Path("web_app.db")
# db_uri = "sqlite:/" + db_path.resolve().as_uri()[5:]

db_uri = "postgres://wbakakfzhirkzk:85e2c6305a72c6aef469b01910aae3b04188511880434c08f5fd163ca81c41ea@ec2-35-169-254-43.compute-1.amazonaws.com:5432/df5orp7bpp1h3n"


app = FastAPI()
app.include_router(home_routes)
app.include_router(twitter_routes)

app.mount("/static", StaticFiles(directory="twit_off_pt5/static"), name="static")
templates = Jinja2Templates(directory="twit_off_pt5/templates")


@app.get("/test")
async def root(request: Request):
    return templates.TemplateResponse("predict_form.html", {"request": request})

@app.get("/")
async def root():
    url = app.url_path_for("test")
    response = RedirectResponse(url=url)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
