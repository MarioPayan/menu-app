from data import Data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List, Union
from models import Dish, ExpandedMenu, Menu, Restaurant
from ai import ClientAI

app = FastAPI()

clientAI = ClientAI

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

data = Data()


@app.get("/ai/")
async def get_ai():
    completion = clientAI.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"},
        ],
    )
    print(completion.choices[0].message)


@app.get("/", response_class=HTMLResponse)
async def get_endpoints():
    host = "http://127.0.0.1:8000"  # Adjust the host as needed
    links = []
    for route in app.routes:
        if (
            hasattr(route, "methods") and "GET" in route.methods
        ):  # Filtering only GET requests for simplicity
            path = route.path
            full_path = f"{host}{path}"
            # Creating an HTML link for each endpoint
            link = f'<a href="{full_path}">{full_path}</a><br>'
            links.append(link)
    # Joining all links to form the HTML content
    html_content = "<h2>Clickable Endpoints:</h2>" + "".join(links)
    return HTMLResponse(content=html_content)


@app.get("/restaurants/", response_model=List[Restaurant])
async def get_restaurants():
    return data.get_restaurants()


@app.get("/restaurants/{restaurant_slug}", response_model=Restaurant)
async def get_restaurant(restaurant_slug: str):
    restaurant = data.get_restaurant_by_slug(restaurant_slug)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@app.get("/menus/", response_model=List[Menu])
async def get_menus():
    return data.get_menus()


@app.get("/menus/{menu_slug}", response_model=Union[Menu, ExpandedMenu])
async def get_menu(menu_slug: str, expanded: bool = False, random: bool = True):
    menu = data.get_menu_by_slug(menu_slug)
    if not menu and random:
        menu = data.menus[0]
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    if expanded:
        return data.get_expanded_menu(menu)
    return menu


@app.get("/dishes/", response_model=List[Dish])
async def get_dishes():
    return data.get_dishes()
