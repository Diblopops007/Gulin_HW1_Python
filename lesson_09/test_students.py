import pytest
import random
from sqlalchemy.sql import text
from db_client import StudentTable


CONNECTION_STRING = "postgresql://postgres:gsv985@localhost:5432/postgres"


@pytest.fixture(scope="module")
def db():
    return StudentTable(CONNECTION_STRING)


@pytest.fixture
def created_student(db):
    """
    Создаёт студента со случайным user_id.

    """
    user_id = random.randint(1000000, 9999999)
    db.create(user_id, "Bachelor", "Full-time", 1)
    
    yield user_id
    
    db.hard_delete(user_id)


def test_create_student(db, created_student):
    """Тест добавления (создания) студента."""
    user_id = created_student
    row = db.get_by_id(user_id)
    
    assert row is not None
    assert row.user_id == user_id
    assert row.level == "Bachelor"
    assert row.deleted_at is None


def test_update_student(db, created_student):
    """Тест изменения (UPDATE) активной записи."""
    user_id = created_student
    
    db.update_level(user_id, "Master")
    row = db.get_by_id(user_id)
    
    assert row is not None
    assert row.level == "Master"


def test_soft_delete_student(db, created_student):
    """Тест мягкого удаления (SOFT DELETE)."""
    user_id = created_student
    
    assert db.get_by_id(user_id) is not None
    
    db.soft_delete(user_id)
    
    assert db.get_by_id(user_id) is None


def test_update_deleted_student_is_impossible(db, created_student):
    """
    Дополнительный тест: проверяем, что удаленную запись нельзя изменить.
    """
    user_id = created_student
    
    db.soft_delete(user_id)
    
    db.update_level(user_id, "PhD")
    
    with db._StudentTable__db.connect() as conn:
        raw_row = conn.execute(
            text("SELECT level FROM student WHERE user_id = :id"), 
            {"id": user_id}
        ).fetchone()
    
    assert raw_row[0] == "Bachelor"