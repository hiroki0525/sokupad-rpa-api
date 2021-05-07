from enum import Enum


class Status(Enum):
    PROCESSING = '実行中'
    SUCCESS = '完了（成功）'
    FAILURE = '完了（失敗）'
