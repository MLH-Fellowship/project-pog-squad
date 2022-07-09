#test_db.py

import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content= 'Hi John')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content= 'Hi Jane')
        assert second_post.id == 2
        # get timeline posts and assert they are correct
        john_post = TimelinePost.select().where(TimelinePost.name == 'John Doe').get()
        assert john_post.id == 1
        assert john_post.email == 'john@example.com'
        jane_post = TimelinePost.select().where(TimelinePost.name == 'Jane Doe').get()
        assert jane_post.id == 2
        assert jane_post.email == 'jane@example.com'
