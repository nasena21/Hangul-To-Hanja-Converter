@echo off
setlocal

:loop
:: Prompt the user for input
set /p user_input=Enter the text to process (type 'exit' to quit): 

:: Check if the user wants to exit
if "%user_input%"=="exit" goto end

:: Add a space before the input
set "user_input= %user_input%"

:: Run the Python script with the input enclosed in double quotes
python test_hanjatagger.py "%user_input%"

:: Go back to the beginning of the loop
goto loop

:end
endlocal
pause
