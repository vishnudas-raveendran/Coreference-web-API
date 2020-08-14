# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:35:55 2020

@author: Vishnudas Raveendran
"""


from fastapi import FastAPI
from app.api.coref import coref_router

app = FastAPI()
app.include_router(coref_router)

