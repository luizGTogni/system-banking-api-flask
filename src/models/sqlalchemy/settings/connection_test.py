import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler

@pytest.mark.skip(reason="DB Interaction")
def test_connect_to_db():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert isinstance(db_engine, Engine)
    assert db_engine is not None
