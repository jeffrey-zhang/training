"""main functionality for the FastAPI tutorial."""
from datetime import datetime, time, timedelta
from enum import Enum
from typing import Annotated, Union
from uuid import UUID
from fastapi import Body, FastAPI, Header, Query
from pydantic import BaseModel, EmailStr, SecretStr

app = FastAPI()


@app.get("/")
async def root():
    """
    Returns a JSON object with a message "Hello World".
    """
    return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     """
#     Retrieve an item with the given ID.

#     Args:
#         item_id (int): The ID of the item to retrieve.

#     Returns:
#         dict: A dictionary containing the ID of the retrieved item.
#     """
#     return {"item_id": item_id}


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

# fake_items_db = [{"item_name": "Foo"}, {
#     "item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_items(skip: int = 0, limit: int = 10):
#     """
#     Retrieve items from the fake database.

#     Args:
#         skip (int): The number of items to skip.
#         limit (int): The maximum number of items to retrieve.

#     Returns:
#         List[Dict]: A list of items retrieved from the database.
#     """
#     return fake_items_db[skip: skip + limit]


class Item(BaseModel):
    """
    Represents an item that can be sold in the store.

    Attributes:
        name (str): The name of the item.
        description (str, optional): A description of the item.
        price (float): The price of the item.
        tax (float, optional): The tax rate for the item.
    """
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    """
    Creates an item in the fake database.

    Args:
        item (Item): The item to be created.

    Returns:
        dict: A dictionary containing the item's name, description, price, and tax.
    """

    return item


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(None, max_length=50)):
    """
    Retrieve items from the fake database.

    Args:
        q (str, optional): The query string to search for.

    Returns:
        dict: A dictionary containing the query string.
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def read_item(item_id: UUID,
                    start_datetime: Annotated[datetime | None, Body()] = None,
                    end_datetime: Annotated[datetime | None, Body()] = None,
                    repeat_at: Annotated[time | None, Body()] = None,
                    process_after: Annotated[timedelta | None, Body()] = None):
    """
    Retrieve information about an item, including its ID, start and end datetimes, repeat time, and processing delay.

    :param item_id: The ID of the item to retrieve information for.
    :type item_id: UUID
    :param start_datetime: The datetime the item starts, defaults to None.
    :type start_datetime: Annotated[datetime | None, Body()], optional
    :param end_datetime: The datetime the item ends, defaults to None.
    :type end_datetime: Annotated[datetime | None, Body()], optional
    :param repeat_at: The time the item repeats, defaults to None.
    :type repeat_at: Annotated[time | None, Body()], optional
    :param process_after: The delay before processing the item, defaults to None.
    :type process_after: Annotated[timedelta | None, Body()], optional
    :return: A dictionary containing information about the item.
    :rtype: dict
    """
    start_process = start_datetime + process_after
    duration = end_datetime - start_datetime
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration
    }


@app.get("/user-agent")
async def get_user_agent(user_agent: Annotated[str | None, Header()] = None):
    """
    Returns the user agent.

    Args:
        user_agent (str, optional): The user agent string.

    Returns:
        dict: A dictionary containing the user agent string.
    """
    return {"User-Agent": user_agent}


class Item2(BaseModel):
    """
    Represents an item with a name, description, price, tax, and tags.

    Attributes:
        name (str): The name of the item.
        description (str, optional): The description of the item.
        price (float): The price of the item.
        tax (float, optional): The tax rate for the item.
        tags (list[str], optional): A list of tags associated with the item.
    """
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items2/", response_model=Item2)
async def create_item2(item: Item2) -> any:
    """
    Creates a new item in the database.

    Args:
        item (Item2): The item to create.

    Returns:
        any: The created item.
    """
    return item


@app.get("/item2/", response_model=list[Item2])
async def read_items2() -> None:
    """
    Reads a list of items from a data source and returns it as a list of dictionaries.

    Returns:
        A list of dictionaries, where each dictionary represents an item and has the following keys:
        - name: a string representing the name of the item
        - price: a float representing the price of the item
    """
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0}
    ]


class UserIn(BaseModel):
    """
    Represents a user input object.

    Attributes:
        username (str): The user's username.
        password (str): The user's password.
        email (EmailStr): The user's email address.
        full_name (str, optional): The user's full name (if provided).
    """
    username: str
    password: SecretStr
    email: EmailStr
    full_name: str | None = None


@app.post("/user")
async def create_user(user: UserIn) -> UserIn:
    """
    Creates a new user in the system.

    Args:
        user (UserIn): The user to create.

    Returns:
        UserIn: The created user.
    """
    return user
