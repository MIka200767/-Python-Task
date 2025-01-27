import pandas as pd
import data_summary
from sklearn.datasets import load_iris
pd.set_option('display.max_columns', 200)


def load_data():
   url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" 
   columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"] 
   df = pd.read_csv(url, header=None, names=columns) 
   return df


data = data_summary.DataSummarize(load_data())


summary_df = data.summarize() 
report = pd.DataFrame(summary_df).to_html(index=False)

with open("file.html", "w") as f:
   f.write(report)


