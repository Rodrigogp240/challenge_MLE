import pandas as pd

from challenge.model import DelayModel

Model = DelayModel()

df = pd.read_csv('data/data.csv')

proces_df,target = Model.preprocess(data=df,target_column='delay')
Model.fit(proces_df,target=target)
Model.importer()