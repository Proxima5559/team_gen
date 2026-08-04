import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


from app.api.routes import router
from app.utils.vne_config import HOST, PORT
from app.utils.templates import templates, STATIC_DIR




app = FastAPI(
    title="Football Team Generator",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/index.html",
        context={"title": "Football Team Generator"}
    )


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)