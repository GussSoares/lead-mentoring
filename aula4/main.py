from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

users = []

class UserSchema(BaseModel):
    name: str
    age: int


@app.get('/user')
def get_user():
    return users


@app.post('/user')
def post_user(user: UserSchema):
    # return {**user, "status": "success"}
    users.append(user.dict())
    return {
        "msg": "user created"
    }


@app.put('/user/{name}')
def put_user(user: UserSchema, name: str):
    for i in range(len(users)):
        if users[i]["name"] == name:
            users[i] = user.dict()
            return JSONResponse({"msg": "user updated"}, status_code=200)
    return JSONResponse({"msg": "not found"}, status_code=404)
