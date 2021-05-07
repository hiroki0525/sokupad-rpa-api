from datetime import datetime
from uuid import uuid4

from const.status import Status


class StateManager:
    class __State:
        def __init__(self):
            now = datetime.now()
            self.__process_id = str(uuid4())
            self.__created_at = now
            self.__updated_at = now
            self.__status: Status = Status.PROCESSING

        def __eq__(self, other):
            if not isinstance(other, StateManager.__State):
                return NotImplemented
            return self.process_id == other.process_id

        @property
        def process_id(self):
            pass

        @process_id.getter
        def process_id(self):
            return self.__process_id

        def succeeded(self):
            self.__update(Status.SUCCESS)

        def failed(self):
            self.__update(Status.FAILURE)

        def __update(self, status: Status):
            self.__updated_at = datetime.now()
            self.__status: Status = status

    __states: list[__State] = []

    @classmethod
    def create(cls) -> str:
        state = cls.__State()
        cls.__states.append(state)
        return state.process_id

    @classmethod
    def remove(cls, process_id: str):
        cls.__states.remove(cls.__find_state(process_id))

    @classmethod
    def get_status(cls, process_id: str):
        return cls.__find_state(process_id).process_id

    @classmethod
    def __find_state(cls, process_id: str) -> __State:
        target_states = [state for state in cls.__states if state.process_id == process_id]
        if len(target_states) == 0:
            raise Exception('no state')
        return target_states[0]
