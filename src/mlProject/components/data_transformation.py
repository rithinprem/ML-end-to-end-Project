import os
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config


    #Note: You can add different data transformation techniques such as Scaler,PCA and all 
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    #I am only adding train_test_splitting because the data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        data = data.drop('Id',axis=1)

        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

