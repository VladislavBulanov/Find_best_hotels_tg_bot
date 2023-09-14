from typing import List, Dict, TypeVar

from peewee import ModelSelect

from database.models.models import db, ModelBase

T = TypeVar("T")


def _store_data(src_db: db, model: T, *data: List[Dict]) -> None:
    """TODO"""

    with src_db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(src_db: db, model: T, *columns: ModelBase) -> ModelSelect:
    """TODO"""

    with src_db.atomic():
        response = model.select(*columns)

    return response


class CRUDInterface:
    """TODO"""

    @staticmethod
    def create():
        """TODO"""
        return _store_data

    @staticmethod
    def retrieve():
        """TODO"""
        return _retrieve_all_data


if __name__ == "__main__":
    _store_data()
    _retrieve_all_data()
    CRUDInterface()
