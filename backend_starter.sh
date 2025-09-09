#! /bin/sh

poetry run uvicorn src.main:app --reload
echo $PATH