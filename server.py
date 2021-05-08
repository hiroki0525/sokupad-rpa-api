import os

from fastapi import FastAPI, Body, BackgroundTasks

from autoload.module_loader import ModuleLoader

from const import RpaMethod
from const.model import DepositData, BuyData, RpaResponse
from entity.state import RpaStateManager

loader = ModuleLoader(os.path.abspath('rpa'))
app = FastAPI()


@app.post(f'/{RpaMethod.DEPOSIT.value}', summary='入金', response_model=RpaResponse, status_code=201)
async def deposit(
        data: DepositData,
        background_tasks: BackgroundTasks
):
    rpa = loader.load_class(RpaMethod.DEPOSIT.value)
    state = RpaStateManager.create(RpaMethod.DEPOSIT, data)
    background_tasks.add_task(rpa(state).run)
    return state.__dict__


@app.post(f'/{RpaMethod.BUY.value}', summary='馬券購入', response_model=BuyData, status_code=201)
async def buy(
        data: BuyData = Body(...)
):
    loader.load_function(RpaMethod.BUY.value)()
    return data
