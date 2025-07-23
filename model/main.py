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

if __name__ == '__main__':
    uv.run('main:app', host='0.0.0.0', port=8000, reload=True)