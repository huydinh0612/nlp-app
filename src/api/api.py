# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from pydantic import BaseModel

from src.models.infer_model import generate_summary
from src.settings import *

app = FastAPI(debug=True)


class TextRequest(BaseModel):
    "define a components of an API"
    text: str
    model: str
    lang: str


@app.post("/summarization_text")
def summarization_text(request: TextRequest):
    # summary with model t5
    summary = generate_summary(text=request.text,
                               model_name=request.model,
                               lang=request.lang)
    return {'summary': summary}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)
    # fastapi dev api.py
