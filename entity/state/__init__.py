from datetime import datetime
from uuid import uuid4

from const.status import Status


class State:
    def __init__(self):
        now = datetime.now()
        self.__process_id = str(uuid4())
        self.__created_at = now
        self.__updated_at = now
        self.__status: Status = Status.PROCESSING

    def succeeded(self):
        self.__update(Status.SUCCESS)

    def failed(self):
        self.__update(Status.FAILURE)

    def __update(self, status: Status):
        self.__updated_at = datetime.now()
        self.__status: Status = status


class StateManager:
    pass