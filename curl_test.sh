#!/bin/bash

# NOTE: This version of the script file refers to the local host site
curl --request POST http://127.0.0.1:5000/api/timeline-post/ -d "name=anonymous&email=a0@test.com&content=random post..."
curl --request GET http://127.0.0.1:5000/api/timeline-post/
