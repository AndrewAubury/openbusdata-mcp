@echo off
REM OpenBusData MCP Server launcher
REM Set your API key here or as a system environment variable
REM set OPENBUS_API_KEY=your-api-key-here

set "SCRIPT_DIR=%~dp0"
"%SCRIPT_DIR%.venv\Scripts\python.exe" "%SCRIPT_DIR%server.py"
