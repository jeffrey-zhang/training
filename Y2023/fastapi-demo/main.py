"""main functionality for the FastAPI tutorial."""
from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Returns a JSON object with a message "Hello World".
    """
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Retrieve an item with the given ID.

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        dict: A dictionary containing the ID of the retrieved item.
    """
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    """
    Returns a dictionary containing the user ID of the current user.

    Returns:
        dict: A dictionary containing the user ID of the current user.
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """
    Retrieve a user with the given user_id.

    Args:
        user_id (str): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's ID.
    """
    return {"user_id": user_id}


class ModeName(str, Enum):
    """
    Enumeration of available model names.

    Attributes:
        alexnet (str): Name of the AlexNet model.
        resnet (str): Name of the ResNet model.
        lenet (str): Name of the LeNet model.
    """
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModeName):
    """
    Returns a dictionary containing the model name and a message based on the input model name.

    Args:
        model_name (ModeName): An enum representing the name of the model.

    Returns:
        dict: A dictionary containing the model name and a message based on the input model name.
    """
    if model_name == ModeName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    Reads a file from the specified file path.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        dict: A dictionary containing the file path.
    """
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    """
    Retrieve items from the fake database.

    Args:
        skip (int): The number of items to skip.
        limit (int): The maximum number of items to retrieve.

    Returns:
        List[Dict]: A list of items retrieved from the database.
    """
    return fake_items_db[skip: skip + limit]
