from entity.state import RpaState
from infra.dao import RpaStateDaoInterface


class PickleRpaStateDao(RpaStateDaoInterface):
    def insert(self, state: RpaState) -> None:
        pass

    def select_by_id(self, process_id: str) -> RpaState:
        pass

    def delete_by_id(self, process_id: str) -> None:
        pass
