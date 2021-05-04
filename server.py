import os
from enum import Enum
from typing import List

from fastapi import FastAPI, Body, BackgroundTasks
from pydantic import BaseModel, Field

from autoload.module_loader import ModuleLoader

loader = ModuleLoader(os.path.abspath('rpa'))
app = FastAPI()


class RpaMethod(Enum):
    DEPOSIT = "deposit"
    BUY = "buy"


class User(BaseModel):
    id: str = Field(..., regex=r'\d{8}', description="加入者番号")
    password: str = Field(..., regex=r'\d{4}', description="暗証番号")
    p_ars: str = Field(..., regex=r'\d{4}', description="P-ARS番号")


class Purchase(BaseModel):
    racecourse: str = Field(..., description="競馬場名"),
    type: str = Field(..., description="買い目")
    horse_numbers: List[int] = Field(..., description="馬番")
    price: int = Field(..., description="購入金額")


class ExecOption(BaseModel):
    commit: bool = Field(False, description="購入まで実行するか")
    headless: bool = Field(False, description="ヘッドレスブラウザで実行するか")


class DepositData(BaseModel):
    user: User = Field(..., description="ユーザー情報")
    amount: int = Field(..., description="入金額")
    option: ExecOption = Field(None, description="実行オプション")


class BuyData(BaseModel):
    user: User = Field(..., description="ユーザー情報")
    # purchases: List[Purchase] = Field(..., description="購入情報。配列で指定した順番で実行")
    option: ExecOption = Field(None, description="実行オプション")


@app.post(f'/{RpaMethod.DEPOSIT.value}', response_model=DepositData, status_code=201)
async def deposit(
        data: DepositData,
        background_tasks: BackgroundTasks
):
    func = loader.load_function(RpaMethod.DEPOSIT.value)
    background_tasks.add_task(func, data)
    return data


@app.post(f'/{RpaMethod.BUY.value}', response_model=BuyData, status_code=201)
async def buy(
        data: BuyData = Body(...)
):
    loader.load_function(RpaMethod.BUY.value)()
    return data
