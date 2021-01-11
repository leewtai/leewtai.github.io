#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate web_query
/home/taiphoon/miniconda3/envs/web_query/bin/python twitter_ingest.py
conda deactivate
