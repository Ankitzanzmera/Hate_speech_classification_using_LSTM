import re
import nltk
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from hate_speech_classification.entity.config_entity import DataTransformationConfig
from hate_speech_classification.utils.logger import logger
from hate_speech_classification.utils.exception import CustomException
from hate_speech_classification.utils.common import create_directories


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        create_directories([self.config.root_dir])

    def initiate_data_transformation(self):
        df = pd.read_csv(self.config.data_path)

        df.drop(["id","type","model_wrong","db.model_preds","status","round","split","annotator","Unnamed: 0"],axis = 1,inplace = True)
        df['label'].replace({"hate":1,"nothate":0},inplace = True)  
        logger.info("Dropped Un-neccessary cols")

        df['text'] = df['text'].apply(self.__clean_regex__)
        logger.info("Cleaned Text Data")

        df.to_csv(self.config.transformed_data_path,index = False)
        logger.info("Save Cleaned Data")

    def __clean_regex__(self,words):
        stopword = set(stopwords.words("english"))
        stemmer = SnowballStemmer("english")
        words = str(words).lower()
        words = re.sub('\[.*?\]', '', words)
        words = re.sub('https?://\S+|www\.\S+',"",words)
        words = re.sub("<.*?>+","",words)
        words = re.sub("[%s]" % re.escape(string.punctuation),"",words)
        words = re.sub("\n","",words)
        words = re.sub("\w*\d\w*","",words)
        words = [word for word in words.split(' ') if word not in stopword]
        words = " ".join(words)
        words = [stemmer.stem(word) for word in words.split(' ')]
        words = " ".join(words)
        return words