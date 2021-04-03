# Flask Palindrome

## Problem
Given user identity.
You need to implement a web service on Flask with one HTTP endpoint `POST /test` which returns reversed user identity.
The result must be cached locally for each input user for 5 seconds.

## Solution
Flask API hosted on Google Cloud Run.

## Example
Request:
```
curl -XPOST http://127.0.0.1:5000/test -H 'Content-Type: application/json' --data '{"user":"987654321"}'
```
Response: `123456789`
