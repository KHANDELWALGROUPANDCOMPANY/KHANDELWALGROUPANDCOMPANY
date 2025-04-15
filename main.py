from fastapi import FastAPI, Request
from app.inference import predict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Server Running!"}

@app.post("/predict")
async def make_prediction(request: Request):
    data = await request.json()
    input_text = data.get("text", "")
    result = predict(input_text)
    return result
