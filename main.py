import akshare as ak

try:
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    print(stock_zh_a_spot_em_df)
except Exception as e:
    print(f"获取数据失败: {e}")
    print("请检查网络连接、AkShare 版本以及 AkShare 服务器状态。")
