# -*- coding: utf-8 -*-
"""
Created on:

@author:
"""

import svdRec
from numpy import *
Data=svdRec.loadExData()
U,Sigma,VT=linalg.svd(Data)
print(Sigma)

#myMat = mat(svdRec.loadExData())
