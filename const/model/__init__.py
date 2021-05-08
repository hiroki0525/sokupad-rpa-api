import datetime
from typing import Type, Any

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(..., regex=r'\d{8}', description="加入者番号")
    password: str = Field(..., regex=r'\d{4}', description="暗証番号")
    p_ars: str = Field(..., regex=r'\d{4}', description="P-ARS番号")


class Purchase(BaseModel):
    racecourse: str = Field(..., description="競馬場名"),
    type: str = Field(..., description="買い目")
    horse_numbers: list[int] = Field(..., description="馬番")
    price: int = Field(..., ge=100, description="購入金額")


class ExecOption(BaseModel):
    commit: bool = Field(False, description="購入まで実行するか")
    headless: bool = Field(False, description="ヘッドレスブラウザで実行するか")


class DepositData(BaseModel):
    user: User = Field(..., description="ユーザー情報")
    amount: int = Field(..., description="入金額")
    option: ExecOption = Field(None, description="実行オプション")


class BuyData(BaseModel):
    user: User = Field(..., description="ユーザー情報")
    # purchases: list[Purchase] = Field(..., description="購入情報。配列で指定した順番で実行")
    option: ExecOption = Field(None, description="実行オプション")


class RpaResponse(BaseModel):
    process_id: str = Field(None, description="プロセスID")
    method: str = Field(None, description="実行タイプ")
    status: str = Field(None, description="実行ステータス")
    params: Any = Field(None, description="実行パラメータ")
    created_at: datetime.datetime = Field(None, description="RPA実行開始時間")
    updated_at: datetime.datetime = Field(None, description="RPA実行更新時間")
