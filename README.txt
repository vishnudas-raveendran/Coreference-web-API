## A Simple API interface for neuralCoref using FastAPI

# Dependency 

1) API Dependencies

    a) Install FastAPI
        
       `pip install fastapi`

    b) Install a server - We use Uvicorn here
    
       `pip install uvicorn`

2) Neural Coref Dependencies
 
 a) Install Spacy and an English model
 
    `pip install -U spacy`
    
    `python -m spacy download en`
    
 b) Install HuggingFace neuralCoref
    
    `pip install neuralcoref`

# To run app server

Navigate to root of directory and execute command

`uvicorn app.main:app --reload`

# To test coref execution

Navigate to http://127.0.0.1:8000/docs#/default/doCoRefResolution_resolve_post

1) A Swagger Ui will be shown, Click on 'Try it out'
2) Enter a phrase such as 'Bill works in ABC. He has two dogs.' in the text box.
3) Click on 'Execute' 

The resolved text will be returned.

