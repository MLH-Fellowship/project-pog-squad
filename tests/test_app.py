#tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/home")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Victor</title>" in html
        assert "<h2 class=\"section-title\">Work Experience</h2>" in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        # assert len(json["timeline_posts"]) == 0

        # check post request
        post_response = self.client.post('/api/timeline_post', data=dict(name="John Doe", email="john@example.com", content="Hi"))
        assert post_response.status_code == 200
        assert post_response.is_json
        post_json = post_response.get_json()
        assert post_json['content'] == "Hi"
        # assert post_json['id'] == 1;
        assert post_json['name'] == 'John Doe'

        # check get request again
        new_response = self.client.get("/api/timeline_post")
        assert new_response.status_code == 200
        assert new_response.is_json
        new_json = new_response.get_json()
        # assert len(new_json["timeline_posts"]) == 1

        # check timeline page
        timeline_response = self.client.get("/timeline")
        assert timeline_response.status_code == 200
        html = timeline_response.get_data(as_text=True)
        assert "<title>Victor</title>" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
