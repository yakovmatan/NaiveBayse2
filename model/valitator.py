import pandas as pd
from sklearn.metrics import confusion_matrix


class Evaluation:

    def __init__(self,trained_data, test_data, classified, class_probs):
        self.class_probs = class_probs
        self.trained_data = trained_data
        self.test_data = test_data
        self.classified = classified
        self.classes = test_data[classified].unique()

    def prediction(self, row):
        probs = {}
        for cls in self.classes:
            prob = self.class_probs[cls]
            for feature, value in row.drop(labels=[self.classified]).items():
                val = row[feature]
                feature_dict = self.trained_data[feature][cls]
                prob *= feature_dict.get(val)
            probs[cls] = prob
        prediction = max(probs, key=probs.get)
        return prediction


    def all_val(self):
        y_true = self.test_data[self.classified].tolist()
        y_pred = self.test_data.apply(self.prediction, axis=1).tolist()
        return y_true, y_pred

    def accuracy_stats(self):
        y_true, y_pred = self.all_val()
        correct = sum(t == p for t, p in zip(y_true, y_pred))
        total = len(y_true)
        incorrect = total - correct
        accuracy = correct / total * 100
        return {
            "correct": correct,
            "incorrect": incorrect,
            "accuracy_percent": accuracy
        }

    def get_confusion_metrix(self):
        y_true, y_pred = self.all_val()
        cm = confusion_matrix(y_true, y_pred, labels=self.classes)
        cm_df = pd.DataFrame(cm, index=self.classes, columns=self.classes)
        return cm_df

