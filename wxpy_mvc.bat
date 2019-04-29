if "%~1" EQU "" set run=1
if "%~1" EQU "install" set run=1
if "%~1" EQU "uninstall" set run=1
if "%~1" EQU "make-docs" set run=1

if %run% NEQ 1 (goto :invalid)

reg query HKEY_LOCAL_MACHINE\SOFTWARE\Python\ContinuumAnalytics\Anaconda37-64
if %ERRORLEVEL% EQU 1 goto :command

set isAnaconda=1
for /f  "tokens=3*" %%a in ('REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Python\ContinuumAnalytics\Anaconda37-64\InstallPath /ve') do set "root=%%a"
call %root%\Scripts\activate.bat %root%

:command

if "%~1" EQU "make-docs" goto :make-docs

:uninstall

pip uninstall wxpymvc
if "%~1" EQU "uninstall" goto list

:install

python setup.py bdist_wheel

cd dist

python -m pip install wxpymvc-0.1-py3-none-any.whl

cd ..

:list

if %isAnaconda% EQU 1 (call conda list)

:end

pause
goto :eof

:make-docs
CALL sphinx_source\make.bat html
goto :eof

:invalid
echo Invalid command
pause
