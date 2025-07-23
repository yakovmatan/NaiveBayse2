import requests

class InfoModel:

    def __init__(self):
        self.url = "http://127.0.0.1:8000"
        self.classes = None
        self.class_probs = None
        self.trained_data = None
        self.classified = None
        self.get_info_model()

    def get_info_model(self):
        res = requests.get(f"{self.url}/trained_model")
        if res.ok:
            data = res.json()
            self.classes = data["classes"]
            self.class_probs = data["class_probs"]
            self.trained_data = data["trained_data"]
            self.classified = data["classified"]
        else:
            raise Exception("Error receiving properties from the server")


