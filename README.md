# rest-api
REST API with Python and Flask for accessing a MySQL database.

# How to test the server
Activate the virtual environment and the run the server.py script. The API prototype can then be tested in a browser by accesing
https://localhost:port/api-command i.e. https://127.0.0.1:5002/contents

Alternatly, requests (GET, POST etc.) can be sent easily from the terminal using curl.
POST: curl -X POST -H "Content-Type: application/json" -d '{"username":"HenryW", "password":"iwatchsuits"}' http://127.0.0.1:5002/submit


# Database
Database used is scraper_db.
