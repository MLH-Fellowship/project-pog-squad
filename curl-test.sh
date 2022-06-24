#!/bin/bash
curl --location --request POST 'http://127.0.0.1:5000/api/timeline_post?name=mari&email=a@a.com&content=esto es un post' \
--header 'Authorization: Bearer asdfasdsdfa' \
--form 'name="hola"' \
--form 'email="hola"' \
--form 'content="hola"'

curl http://127.0.0.1:5000/api/timeline_post