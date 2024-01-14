import sys,os
import pandas as pd
from sklearn.model_selection import train_test_split
from hate_speech_classification.utils.common import create_directories,save_tokenizer
from hate_speech_classification.utils.exception import CustomException
from hate_speech_classification.utils.logger import logger
from hate_speech_classification.entity.config_entity import ModelTrainerConfig
from keras.models import Sequential
from keras.layers import Dense,LSTM,SpatialDropout1D,Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer  
from keras.utils import pad_sequences

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
        create_directories([self.config.root_dir])

    def __split_data__(self):
        cleaned_data = pd.read_csv(self.config.cleaned_data)
        X = cleaned_data['text']
        y = cleaned_data['label']
        logger.info("Separated X and Y")

        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(X,y,test_size = 0.3,random_state = 42)
        self.X_train = self.X_train.astype(str)
        self.X_test = self.X_test.astype(str)
        print(self.X_train.shape,self.X_test.shape,self.y_train.shape,self.y_test.shape)
        logger.info("Splitted Into Tain and Test")

    def __tokenizing__(self):
        try:
            logger.info("Applying Tokenization on the Data")
            tokenizer = Tokenizer(num_words = self.config.MAX_WORDS)
            tokenizer.fit_on_texts(self.X_train)
            sequences = tokenizer.texts_to_sequences(self.X_train)
            sequence_matrix = pad_sequences(sequences, maxlen=self.config.MAX_LEN)
            logger.info("Successfully Transformed data into Vectors")
            save_tokenizer(self.config.tokenizer_path, tokenizer)
            logger.info("Tokenizer Saved Successfully")
            return sequence_matrix
        except Exception as e:
            raise CustomException(e, sys)



    def __model_architecture__(self):
        model = Sequential()
        model.add(Embedding(self.config.MAX_WORDS, 100, input_length = self.config.MAX_LEN))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100,dropout = 0.2, recurrent_dropout = 0.2))
        model.add(Dense(1,activation = self.config.ACTIVATION))
        model.summary()
        model.compile(loss = self.config.LOSS, optimizer = RMSprop(), metrics = self.config.METRICS)
        logger.info("Model Architecture Created Completed")
        return model
    

    def initiate_model_trainer(self):
        self.__split_data__()
        sequences_matrix = self.__tokenizing__()
        self.model = self.__model_architecture__()

        logger.info("Training is Started")
        self.model.fit(sequences_matrix,self.y_train,
                        batch_size = self.config.BATCH_SIZE,
                        epochs = self.config.EPOCHS,
                        validation_split = self.config.VALIDATION_SPLIT)

        logger.info("Model Training Finished")
        self.model.save(self.config.model_path)

        os.makedirs(os.path.dirname(self.config.X_test_path),exist_ok = True)
        self.X_test.to_csv(self.config.X_test_path)
        self.y_test.to_csv(self.config.y_test_path)
