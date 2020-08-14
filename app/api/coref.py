# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:17:56 2020

@author: Vishnudas Raveendran
"""


import logging;
import neuralcoref
import spacy
from fastapi import APIRouter,HTTPException


unicode_ = str
coref_router = APIRouter()

@coref_router.post('/resolve', status_code=200)
async def doCoRefResolution(text: str):
    o = CoRef()
    return o.performCoref(text)

class CoRef(object):
    def __init__(self):
        self.nlp = spacy.load("en")
        neuralcoref.add_to_pipe(self.nlp)
        logging.basicConfig(level=logging.INFO)
        self.response = None
    
    def performCoref(self, text):
        self.response = {}
        print("text:", text)
        if text is not None:
            text = unicode_(text)
            doc = self.nlp(text)
            if doc._.has_coref:
                resolved = doc._.coref_resolved
                self.response["resolved"] = resolved
            return self.response;
        raise HTTPException(status_code=400, detail="Text was empty")