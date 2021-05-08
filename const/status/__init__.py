from enum import Enum


class Status(Enum):
    PROCESSING = '実行中'
    WAITING = '実行待ち'
    SUCCESS = '完了（成功）'
    FAILURE = '完了（失敗）'
