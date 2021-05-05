import os
from enum import Enum

from fastapi import FastAPI, Body, BackgroundTasks

from autoload.module_loader import ModuleLoader

from const.model import DepositData, BuyData

loader = ModuleLoader(os.path.abspath('rpa'))
app = FastAPI()


class RpaMethod(Enum):
    DEPOSIT = "deposit"
    BUY = "buy"


@app.post(f'/{RpaMethod.DEPOSIT.value}', response_model=DepositData, status_code=201)
async def deposit(
        data: DepositData,
        background_tasks: BackgroundTasks
):
    rpa = loader.load_class(RpaMethod.DEPOSIT.value)
    background_tasks.add_task(rpa(data).run)
    return data


@app.post(f'/{RpaMethod.BUY.value}', response_model=BuyData, status_code=201)
async def buy(
        data: BuyData = Body(...)
):
    loader.load_function(RpaMethod.BUY.value)()
    return data
