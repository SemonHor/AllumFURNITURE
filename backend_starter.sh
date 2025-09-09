#! /bin/sh

echo $PATH
PATH="/home/HorSEMLoc/.local/bin/poetry:$PATH"
echo $PATH
cd /home/HorSEMLoc/AllumFURNITURE
poetry run uvicorn src.main:app --reload
