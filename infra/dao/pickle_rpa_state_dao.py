import pickle

from entity.state import RpaState
from infra.dao import RpaStateDaoInterface


class PickleRpaStateDao(RpaStateDaoInterface):
    def insert(self, state: RpaState) -> None:
        with open(state.process_id, mode='wb') as f:
            pickle.dump(state, f)

    def select_by_id(self, process_id: str) -> RpaState:
        with open(process_id, mode='rb') as f:
            state: RpaState = pickle.load(f)
        return state

    def delete_by_id(self, process_id: str) -> None:
        empty_list = []
        openfile = open(process_id, 'wb')
        pickle.dump(empty_list, openfile)
        openfile.close()
