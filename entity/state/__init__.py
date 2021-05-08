from datetime import datetime
from typing import TypeVar, Generic
from uuid import uuid4

from const import RpaMethod
from const.status import Status

T = TypeVar('T')


class RpaState(Generic[T]):
    def __init__(self, method: RpaMethod, params: T, status: Status = Status.PROCESSING):
        now = datetime.now()
        self.__process_id = str(uuid4())
        self.__status: Status = status
        self.__method = method
        self.__created_at = now
        self.__updated_at = now
        self.__params = params

    def __eq__(self, other):
        if not isinstance(other, RpaState):
            return NotImplemented
        return self.process_id == other.process_id

    @property
    def process_id(self) -> str:
        return self.__process_id

    @property
    def status(self) -> Status:
        return self.__status

    @property
    def params(self) -> T:
        return self.__params

    def succeeded(self):
        self.__update(Status.SUCCESS)

    def failed(self):
        self.__update(Status.FAILURE)

    def start_process(self):
        self.__update(Status.PROCESSING)

    def __update(self, status: Status):
        self.__updated_at = datetime.now()
        self.__status: Status = status


class RpaStateManager:
    __states: list[RpaState] = []

    @classmethod
    def create(cls, method: RpaMethod, params: T) -> RpaState:
        state = RpaState[T](method, params)
        cls.__states.append(state)
        return state

    @classmethod
    def remove(cls, process_id: str):
        cls.__states.remove(cls.__find_state(process_id))

    @classmethod
    def get_status(cls, process_id: str):
        return cls.__find_state(process_id).process_id

    @classmethod
    def __find_state(cls, process_id: str) -> RpaState:
        target_states = [state for state in cls.__states if state.process_id == process_id]
        if len(target_states) == 0:
            raise Exception('no RpaState')
        return target_states[0]
