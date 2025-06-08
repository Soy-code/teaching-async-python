# from typing import Optional
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"hello": "world"}


# @app.get("/hello")
# def read_root():
#     return {"hello": "fastapi"}


# @app.get("/items/{item_id}/{xyz}")
# def read_item(item_id: int, xyz: str, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q, "xyz": xyz}


## /Jinja2 템플릿 엔진
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 절대경로 지정
from pathlib import Path

# 현재 파일의 경로가 있는 위치의 부모 폴더를 가리킴
BASE_DIR = Path(__file__).resolve().parent  # app


app = FastAPI()

# 미들웨어 설정
# static files: CSS, JS, images 등 처리하는 것 -> 사용 안 할 것임
# app.mount("/static", StaticFiles(directory="static"), name="static")


# html 템플릿을 서빙할 건데, 해당하는 html 파일들이 있는 디렉토리
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# response를 해줬을 때 html을 서빙을 해주고 싶다는 것


# # 현재 프로젝트에서는 dynamic한 html을 서빙하지 않을 것
# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     # print(request)
#     print(dir(request))
#     print("------")
#     print(request.headers)
#     print("------")
#     print(request.body)
#     return templates.TemplateResponse(
#         request=request,
#         name="item.html",
#         context={"request": request, "id": id, "data": "hello fast api"},
#     )


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str = None):
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이", "keyword": q}
    )
