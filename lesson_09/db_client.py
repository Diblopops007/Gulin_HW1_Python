from sqlalchemy import create_engine
from sqlalchemy.sql import text


class StudentTable:
    __scripts = {
        "insert": text(
            "INSERT INTO student (user_id, level, education_form, subject_id) "
            "VALUES (:user_id, :level, :education_form, :subject_id) "
            "RETURNING user_id"
        ),
        "select_by_id": text(
            "SELECT * FROM student "
            "WHERE user_id = :user_id AND deleted_at IS NULL"
        ),
        "update_level": text(
            "UPDATE student SET level = :new_level "
            "WHERE user_id = :user_id AND deleted_at IS NULL"
        ),
        "soft_delete": text(
            "UPDATE student SET deleted_at = NOW() "
            "WHERE user_id = :user_id AND deleted_at IS NULL"
        ),
        "hard_delete": text(
            "DELETE FROM student WHERE user_id = :user_id"
        )
    }

    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string)

    def create(self, user_id: int, level: str, education_form: str, subject_id: int) -> int:
        with self.__db.begin() as conn:
            conn.execute(
                self.__scripts["insert"],
                {"user_id": user_id, "level": level, "education_form": education_form, "subject_id": subject_id}
            )
        return user_id

    def get_by_id(self, user_id: int):
        with self.__db.connect() as conn:
            result = conn.execute(
                self.__scripts["select_by_id"], 
                {"user_id": user_id}
            ).fetchone()
        return result

    def update_level(self, user_id: int, new_level: str) -> None:
        with self.__db.begin() as conn:
            conn.execute(
                self.__scripts["update_level"],
                {"user_id": user_id, "new_level": new_level}
            )

    def soft_delete(self, user_id: int) -> None:
        with self.__db.begin() as conn:
            conn.execute(
                self.__scripts["soft_delete"],
                {"user_id": user_id}
            )

    def hard_delete(self, user_id: int) -> None:
        with self.__db.begin() as conn:
            conn.execute(
                self.__scripts["hard_delete"],
                {"user_id": user_id}
            )