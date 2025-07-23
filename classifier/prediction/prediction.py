import pandas as pd


class Prediction:

    def __init__(self,classes, class_probs, trained_data, classified):
        self.classes = classes
        self.class_probs = class_probs
        self.trained_data = trained_data
        self.classified = classified

    def prediction(self, row):
        probs = {}
        for cls in self.classes:
            prob = self.class_probs[cls]
            for feature, value in row.items():
                val = row[feature]
                feature_dict = self.trained_data[feature][cls]
                prob *= feature_dict.get(val)
            probs[cls] = prob
        prediction = max(probs, key=probs.get)
        return prediction