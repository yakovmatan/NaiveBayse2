from fastapi import FastAPI
import uvicorn as uv
from prediction.prediction import Prediction
from prediction.info_model import InfoModel

app = FastAPI()

model = InfoModel()

@app.post("/prediction")
def prediction(row: dict):
    the_prediction = Prediction(model.classes, model.class_probs, model.trained_data, model.classified)
    res = the_prediction.prediction(row)
    return {"prediction" : res}

if __name__ == '__main__':
    uv.run('main:app', host='127.0.0.1', port=8001, reload=True)