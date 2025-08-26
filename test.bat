@echo off
set /p ACCESS_TOKEN=< token.env
http GET http://localhost:8000/api/products/ Authorization:"Bearer %ACCESS_TOKEN%"
pause