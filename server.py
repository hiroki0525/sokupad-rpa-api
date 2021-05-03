from typing import List

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    id: int = Field(..., ge=8, le=8, description="加入者番号")
    password: int = Field(..., ge=4, le=4, description="暗証番号")
    p_ars: int = Field(..., ge=4, le=4, description="P-ARS番号")


class Purchase(BaseModel):
    type: str = Field(..., description="買い目")
    horse_numbers: List[int] = Field(..., description="馬番")
    price: int = Field(..., description="購入金額")


class ExecOption(BaseModel):
    commit: bool = Field(False, description="購入まで実行するか")
    headless: bool = Field(False, description="ヘッドレスブラウザで実行するか")


class BuyData(BaseModel):
    user: User = Field(..., description="ユーザー情報")
    purchases: List[Purchase] = Field(..., description="購入情報。配列で指定した順番で実行")
    option: ExecOption = Field(None, description="実行オプション")


@app.post('/racecourse/{racecourse}/buy') # methodとendpointの指定
async def buy(
        racecourse: str = Path(..., description="競馬場名"),
        data: BuyData = Body(...),
    ):
    return {
        "racecourse": racecourse,
        "data": data
    }