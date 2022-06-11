from cProfile import label
from fastapi import FastAPI
import spacy

app = FastAPI()
nlp = spacy.load("pt_core_news_sm")

@app.get("/")
async def root():
    return {"message": "Hello World Gabriel!"}

@app.get("/entities")
async def root(text: str):
    # "!"
    return [{"entity": ent.text,
             "startChar": ent.start_char,
             "endChar": ent.end_char,
             "label": ent.label_} 
            for ent in nlp(text).ents]
