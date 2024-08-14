from fastapi import FastAPI 
from pydantic import BaseModel 

# from models.predict_model import a  ## can run from inside src/
# from src.models.predict_model import a  ## can run from outside src/


app = FastAPI(debug=True) 

class TextRequest(BaseModel): 
    text: str 


@app.post("/summarization_text") 
def process_text(request: TextRequest): 

    result = request.text
    return result


if __name__ == "__main__": 
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8000)