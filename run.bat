@echo off
color a
cd C:\Users\super\Desktop\Projects\nodejs\shell
cls
start http://localhost:5000
%~dp0\venv\Scripts\python.exe server.py