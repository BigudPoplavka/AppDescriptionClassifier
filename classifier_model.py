import os
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


class TextClassifier:
    def __init__(self):
        self.model = None
        self.vectorizer = None
    

    def load_dataset(self, dataset_path):
        dataset = defaultdict(list)
        try:
            for filename in os.listdir(dataset_path):
                with open(os.path.join(dataset_path, filename), 'r', encoding='utf-8') as file:
                    category = filename.split('.')[0]  

                    for line in file:
                        dataset[category].append(line.strip())

            return dataset
        except FileNotFoundError:
            print ('ОШИБКА! Путь не найден!')
        except Exception as e:
            print(e)


    def preprocess_data(self, dataset):
        X, y = [], []

        for category, texts in dataset.items():
            X.extend(texts)
            y.extend([category] * len(texts))

        return X, y
    

    def train(self, X_train, y_train):
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.model.fit(X_train, y_train)
    

    def predict(self, texts):
        predictions = self.model.predict(texts)
        probabilities = self.model.predict_proba(texts)

        return predictions, probabilities


def formating_results(classifier, predictions, 
                      probabilities, show_probabiliteis):
    probabilities_result_string = ""
    multiple_variants_msg = "Из данного описания похоже, что приложение или относится к одному из направлений, или затрагивает технологии этих направлений: "
    most_probably_variants = []

    for pred, prob in zip(predictions, probabilities):
        print("Предсказанное направление:", pred)
        print("Вероятности:")

    for category, probability in list(zip(classifier.model.classes_, prob))[1:]:
        print(f"{category}: {probability}")

        if int(str(probability).split('.')[1][0]) > 0:
            most_probably_variants.append(f"{category} - {probability:.3f}")

        probabilities_result_string += f"\n - {category}: {probability:.3f}"

    if len(most_probably_variants) > 1:
        pred = "{0}\n {1}".format(multiple_variants_msg, '\n'.join(most_probably_variants))

    if show_probabiliteis:
        return f"{pred} \n\nВероятности по направлениям \n{probabilities_result_string}"
    else:
        return pred


def predict(user_input, show_probabiliteis):
    classifier = TextClassifier()
    dataset_path = os.path.join(os.getcwd(), 'dataset')
    dataset = classifier.load_dataset(dataset_path)
    X, y = classifier.preprocess_data(dataset)

    classifier.train(X, y)

    predictions, probabilities = classifier.predict([user_input])
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    y_pred = classifier.model.predict(X_test)

    print(classification_report(y_test, y_pred))
    return formating_results(classifier, predictions, probabilities, show_probabiliteis)
