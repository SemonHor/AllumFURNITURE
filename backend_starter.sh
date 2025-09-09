#! /bin/sh

PATH="/home/HorSEMLoc/.local/bin:$PATH"
cd /home/HorSEMLoc/AllumFURNITURE
poetry run uvicorn src.main:app --reload
