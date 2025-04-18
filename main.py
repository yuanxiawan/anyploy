import akshare as ak

try:
    # 原调用：stock_zh_a_spot_em(timeout=10)
    # 修改后：
    stock_data = ak.stock_zh_a_spot_em()
    print(stock_data)
except TypeError as e:
    print(f"调用函数出错: {e}")
except Exception as e:
    print(f"获取数据失败: {e}")
