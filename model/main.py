from fastapi import FastAPI
import uvicorn as uv
from manager import NaiveBayesManager

app = FastAPI()

manager = NaiveBayesManager("data/buy_computer_data.csv", "buys_computer")

@app.get("/accuracy")
def accuracy():
    try:
        return manager.get_accuracy()
    except Exception as e:
        return {"error": str(e)}

@app.get("/confusion_matrix")
def confusion_matrix():
    try:
        return manager.get_confusion_matrix()
    except Exception as e:
        return {"error": str(e)}

@app.get("/trained_model")
def trained_model():
    try:
        return {'classes': manager.model.classes.tolist(),
                'class_probs': manager.model.class_probs,
                'trained_data' : manager.model.feature_probs,
                'classified' : manager.model.classified
            }
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    uv.run('main:app', host='127.0.0.1', port=8000, reload=True)
