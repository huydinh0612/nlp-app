from fastapi import FastAPI 
from pydantic import BaseModel 

# from models.predict_model import a  ## can run from inside src/
from src.models.predict_model import t5_summary, bart_summary  ## can run from outside src/


app = FastAPI(debug=True) 

class TextRequest(BaseModel): 
    "define a components of an API"
    
    text: str 
    model: str
    lang: str

@app.post("/summarization_text") 
def summarization_text(request: TextRequest): 
    # summary with model t5
    if 't5' in request.model.lower():
        summary = t5_summary(text=request.text, lang=request.lang)

    # summary with model bart
    elif 'bart' in request.model.lower():
        summary = bart_summary(text=request.text, lang=request.lang)

    return {'summary': summary}



if __name__ == "__main__": 
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # fastapi dev api.py