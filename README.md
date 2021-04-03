# Flask Palindrome

## Problem
Given user identity.
You need to implement a web service on Flask with one HTTP endpoint `POST /test` which returns reversed user identity.
The result must be cached locally for each input user for 5 seconds.

## Solution
Flask API hosted on Google Cloud Run.

## Development
Local run:
```
python main.py
```
Test request:
```
curl -XPOST http://0.0.0.0:8080/test -H 'Content-Type: application/json' --data '{"user":"987654321"}'
```
Expected response: `123456789`

## Production
Build:
```
gcloud builds submit --tag gcr.io/flask-palindrome/flask-palindrome
```
Deploy:
```
gcloud run deploy --image gcr.io/flask-palindrome/flask-palindrome --platform managed
```
Test request:
```
curl -XPOST https://flask-palindrome-6rkkmz7gwq-lz.a.run.app/test -H 'Content-Type: application/json' --data '{"user":"987654321"}'
```
Response: `123456789`
