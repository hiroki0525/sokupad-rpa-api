from abc import ABC, abstractmethod

from entity.state import RpaState


class RpaStateDaoInterface(ABC):
    @abstractmethod
    def insert(self, state: RpaState) -> None:
        pass

    @abstractmethod
    def select_by_id(self, process_id: str) -> RpaState:
        pass

    @abstractmethod
    def delete_by_id(self, process_id: str) -> None:
        pass