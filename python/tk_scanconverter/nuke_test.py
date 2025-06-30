import os

conda_py311 = os.environ.get("REZ_PYSEQ")

print(f"conda_py311: {conda_py311}")

# Nuke Plugin Path 추가
import nuke

nuke.pluginAddPath(conda_py311, addToSysPath=True)  # Conda Python Path 추가
# conda_py311 = "/home/rapa/anaconda3/envs/py311/lib/python3.11/site-packages"


print("Nuke Sys Test")

import sys

print("@" * 50)
print(sys.path)
print("@" * 50)

# conda_py311 = "/home/rapa/anaconda3/envs/py311/lib/python3.11/site-packages"
# print(conda_py311 in sys.path)

import pyseq

print(pyseq)
