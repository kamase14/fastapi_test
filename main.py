from fastapi import FastAPI, HTTPException,Request, status
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from repository import *
from types import *
import uvicorn


class RecipeBody(BaseModel):
    title: str = ""
    making_time: str = ""
    serves: str = ""
    ingredients: str = ""
    cost: int= None

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@app.get("/recipes")
async def get_all_recipe():
    recipes = fetch_all_recipe()
    return {"recipes": recipes}

@app.post("/recipes")
async def post_new_recipe(body:RecipeBody):

    if body.title == "" or body.making_time == "" or body.serves == "" or body.ingredients == "" or body.cost == None:
        return { "message": "Recipe creation failed!", "required": "title, making_time, serves, ingredients, cost" }

    recipe = register_recipe(body)
    return {"message": "Recipe successfully created!", "recipe": [recipe]}

@app.patch("/recipes/{recipe_id}")
async def update_specific_recipe(recipe_id, body:RecipeBody):

    if body.title == "" or body.making_time == "" or body.serves == "" or body.ingredients == "" or body.cost == None:
        return { "message": "Recipe creation failed!", "required": "title, making_time, serves, ingredients, cost" }

    result = update_recipe( recipe_id ,body)

    return {"message": "Recipe successfully updated!", "recipe": [result]}

@app.delete("/recipes/{recipe_id}")
async def delete_specific_recipe(recipe_id):

    if recipe_id.isdecimal() == False:
        raise HTTPException(status_code=404, detail="Not Found")

    is_success = delete_recipe(recipe_id)

    message = "No Recipe Found"
    if is_success == True:
        message = "Recipe successfully removed!"

    return {"message": message}

@app.get("/recipes/{recipe_id}")
async def get_specific_recipe(recipe_id):
    if recipe_id.isdecimal() == False:
        raise HTTPException(status_code=404, detail="Not Found")

    recipe = fetch_specific_recipe(recipe_id)
    return {"message": "Recipe details by id", "recipe": [recipe]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
