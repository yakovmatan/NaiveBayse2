from data_loader import DataLoader
from cleaner import Cleaner
from builder import NaiveBayes
from split_data import split_dataframe
from valitator import Evaluation


class NaiveBayesManager:
    def __init__(self, csv_path: str, label_column: str):
        self.data_loader = DataLoader()
        self.data_loader.load_data(csv_path)
        self.df = Cleaner(self.data_loader.df).clean_data()

        self.train_df, self.test_df = split_dataframe(self.df)

        self.model = NaiveBayes(self.train_df, label_column)
        self.model.fit()

        self.evaluation = Evaluation(
            self.model.feature_probs,
            self.test_df,
            label_column,
            self.model.class_probs
        )

    def get_accuracy(self):
        return self.evaluation.accuracy_stats()

    def get_confusion_matrix(self):
        return self.evaluation.get_confusion_metrix()
