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

# import glob

import pyseq
# from pyseq import Sequence


print("@" * 50)
print(sys.path)
print("@" * 50)

print(pyseq)

####
"""
Test Button Clicked
p: /home/rapa/dev/sgtk/tk-scanconverter/python/tk_scanconverter
conda_py311: /home/rapa/anaconda3/envs/py311/lib/python3.11/site-packages
A license for nuke was not found

FOUNDRY LICENSE ERROR REPORT
----------------------------
Timestamp: Mon Jun 30 10:22:03 2025
License(s) Requested:
nuke 2025.0520 render only with options all 
Extended Info: 
Host : localhost.localdomain
System ID(s) : 581122bda5e4 , 5254006d0aad
RLM Environment Info : /usr/local/foundry/RLM
Login Environment Info : /home/rapa/.local/share/Foundry/Tokens

RLM LICENSE DIAGNOSTICS
nuke : No license for product ENT_STATUS_RLM_LICENSE_NOPRODUCT
License Paths(s) : /usr/local/foundry/RLM

LOGIN LICENSE DIAGNOSTICS
nuke : No tokens found for product ENT_STATUS_TEND_TOKEN_NO_PRODUCT
License Paths(s) : /home/rapa/.local/share/Foundry/Tokens

Nuke 16.0v3, 64 bit, built May 20 2025.
Copyright (c) 2025 The Foundry Visionmongers Ltd.  All Rights Reserved.
Licence expires on: 2025/8/6

Nuke Test
There are no active Write operators in this script
"""

# Event handler
"""
        print("Test Button Clicked")

        # Nuke 환경변수
        nuke_path = os.environ.get("NUKE")

        p = Path(__file__).parent
        print(
            f"p: {p}"
        )  # "/home/rapa/dev/sgtk/tk-scanconverter/python/tk_scanconverter/"

        # Nuke Plugin Setting
        cmd = f"python {p / 'nuke_setup.py'}"
        nuke_setup = subprocess.run(cmd, shell=True)

        # Run Nuke
        nuke_cmd = f"{nuke_path} -ix {p / 'nuke_test.py'}"

        run_nuke = subprocess.run(nuke_cmd, shell=True)

        return nuke_setup, run_nuke
"""
