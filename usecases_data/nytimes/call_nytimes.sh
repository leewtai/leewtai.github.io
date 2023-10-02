#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate lec
# /home/taiphoon/miniconda3/envs/web_query/bin/python call_nytimes.py
/home/taiphoon/miniconda3/envs/web_query/bin/python get_archive.py
conda deactivate
