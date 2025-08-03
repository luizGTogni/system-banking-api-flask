from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

class MockConnectionException:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.add.side_effect = self.__raise_exception
        self.session.query.side_effect = self.__raise_not_result_found

    def __raise_exception(self, *args, **kwargs):
        raise Exception("Exception")

    def __raise_not_result_found(self, *args, **kwargs):
        raise NoResultFound("Not result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

class MockConnectionQueryException:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_exception

    def __raise_exception(self, *args, **kwargs):
        raise Exception("Exception")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass
