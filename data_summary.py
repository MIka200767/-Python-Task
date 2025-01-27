import pandas as pd
import numpy as np

class DataSummarize:
  def __init__(self, df):
    self.df = df

  def summarize(self):
    summary = []
    for col in self.df.columns:
      column_value = self.df[col]
      col_summary = {}
      col_summary["name"] = col
      col_summary["type"] = column_value.dtype
      col_summary["unique"] = column_value.nunique()
      col_summary["mode"] = column_value.mode().iloc[0] if not column_value.mode().empty else None
      if pd.api.types.is_numeric_dtype(column_value):
        col_summary["mean"] = round(column_value.mean(), 2)
        col_summary["median"] = column_value.median()
        col_summary["std"] = round(column_value.std(), 2)
        col_summary["var"] = round(np.sqrt(col_summary["std"]), 2)
        col_summary["min"] = column_value.min()
        col_summary["max"] = column_value.max()
        col_summary["iq"] = np.percentile(column_value, 75) - np.percentile(column_value, 25)
      summary.append(col_summary)
    return summary
