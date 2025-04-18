# -*- coding: utf-8 -*-
import akshare as ak
import pandas as pd
import numpy as np
import datetime

def get_stock_data(stock_code, date):
  """获取股票数据"""
  try:
    df = ak.stock_daily_df(symbol=stock_code, start_date=date, end_date=date)
    if not df.empty:
      return df.iloc[0]
    else:
      print(f"未找到股票 {stock_code} 在 {date} 的数据")
      return None
  except Exception as e:
    print(f"获取数据失败: {e}")
    print("AkShare 请求失败，请检查网络连接或股票代码是否正确。")
    return None

if __name__ == '__main__':
  stock_code = "600519"  # 贵州茅台 (注意: AkShare 通常不需要后缀 .SH)
  date = "2024-01-26"      # 今天的日期

  data = get_stock_data(stock_code, date)

  if data is not None:
    print(f"股票代码: {data['证券代码']}")
    print(f"日期: {data['日期']}")
    print(f"开盘价: {data['开盘价']}")
    print(f"收盘价: {data['收盘价']}")
    print(f"成交量: {data['成交量']}")
  else:
    print("获取数据失败")
