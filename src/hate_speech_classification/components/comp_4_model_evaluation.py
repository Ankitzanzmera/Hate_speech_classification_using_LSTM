import sys
import pickle
import keras
import pandas as pd
from keras.utils import pad_sequences
from hate_speech_classification.utils.logger import logger
from sklearn.metrics import confusion_matrix,accuracy_score
from hate_speech_classification.entity.config_entity import ModelEvaluationCOnfig
from hate_speech_classification.utils.exception import CustomException
from hate_speech_classification.utils.common import create_directories

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationCOnfig):
        self.config = config
        create_directories([self.config.root_dir])


    def __get_tokenizer_object__(self):
        with open(self.config.tokenizer_path,"rb") as handle:
            tokenizer = pickle.load(handle)
        return tokenizer

    def initiate_model_evaluation(self):
        try:
            X_test = pd.read_csv(self.config.X_test_path)['text']
            X_test = X_test.astype(str) 
            y_test = pd.read_csv(self.config.y_test_path)['label']
            logger.info("Got Test Data")

            tokenizer = self.__get_tokenizer_object__()
            model = keras.models.load_model(self.config.model_path)
            logger.info("Got The Tokenizer and Model Config")

            text_sequences = tokenizer.texts_to_sequences(X_test)
            sequence_matrix = pad_sequences(text_sequences,maxlen = self.config.MAX_LEN)

            accuracy = model.evaluate(sequence_matrix,y_test)

            y_pred = model.predict(sequence_matrix)
            prediction = []
            for pred in y_pred:
                if pred[0] < 0.5:
                    prediction.append(0)
                else:
                    prediction.append(1)

            conf_matrix = confusion_matrix(y_test,prediction)
            acc_score = accuracy_score(y_test,prediction)

            with open(self.config.evaluation_file_path,'w') as file_obj:
                file_obj.write(f"Accuracy at Evaluation = {accuracy}\n")
                file_obj.write(f"accuracy score = {acc_score}\n")
                file_obj.write(f"Confusion_ Matrix = \n{str(conf_matrix)}")
        except Exception as e:
            raise CustomException(e,sys)