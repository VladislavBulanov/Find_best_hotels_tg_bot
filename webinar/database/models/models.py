# TODO

from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('tg_bot.db')


class ModelBase(pw.Model):
    """TODO"""

    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    """TODO"""

    number = pw.TextField()
    message = pw.TextField()
