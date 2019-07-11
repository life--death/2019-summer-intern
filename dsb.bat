set ENV_PATH=%PATH%
@echo ====current environment：
@echo %ENV_PATH%

set MY_PATH=C:\Users\WDAGUtilityAccount\Desktop\Python36_64
set ENV_PATH=%PATH%;%MY_PATH%

@echo ====new environment：
@echo %ENV_PATH%

pause