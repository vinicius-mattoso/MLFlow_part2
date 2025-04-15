@echo off
set STORAGE_DIR=..\store\mlruns_store

if not exist %STORAGE_DIR% (
    mkdir %STORAGE_DIR%
)

mlflow server ^
  --backend-store-uri %STORAGE_DIR% ^
  --default-artifact-root %STORAGE_DIR% ^
  --host 127.0.0.1 ^
  --port 5000