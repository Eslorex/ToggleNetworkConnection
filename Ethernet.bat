@echo off
powershell -Command "Start-Process cmd -ArgumentList '/c cd C:\Users\Eslorex\Desktop && python connection.py' -Verb RunAs"
