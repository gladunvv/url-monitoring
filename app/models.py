from peewee import *
import os
import config

db = SqliteDatabase(config.PATH_DB)


class BaseModel(Model):
    class Meta:
        database = db


class Monitoring(BaseModel):
    ts = TimestampField(null=False)
    url = CharField(null=False)
    label = CharField(null=False)
    response_time = FloatField()
    status_code = IntegerField(null=True)
    content_length = IntegerField(null=True)


def initialize_db():
    db.connect()
    db.create_tables([Monitoring], safe=True)
    db.close()

initialize_db()
