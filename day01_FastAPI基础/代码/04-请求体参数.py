from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 注册： 用户名和密码 → str
class User(BaseModel):
    username: str = Field(default="张三", min_length=2, max_length=10, description="用户名，长度要求2-10个字")
    password: str = Field(min_length=3, max_length=20)


@app.post("/register")
async def register(user: User):
    return user


class Goods(BaseModel):
    name: str = Field( min_length=1, max_length=50, description="商品名，必填，长度 1-50")
    price: int = Field(description="价格，必填")
    stock: int = Field(default=0, description="库存，默认值 0")


@app.post("/goods")
async def getGoods(goods: Goods):
    return goods
