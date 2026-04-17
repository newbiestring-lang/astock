"""载入本数据集的便捷函数。

用法：
    from load import load_kline, load_meta, load_index
    df     = load_kline()                            # 读全部（~580万行）
    single = load_kline(codes=["000001","600000"])   # 读指定几只
    recent = load_kline(start="2025-01-01")          # 读某日期起
    meta   = load_meta()
    idx    = load_index()
"""
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent

def load_kline(codes=None, start=None, end=None):
    filters = []
    if codes is not None:
        filters.append(("code", "in", list(codes)))
    if start is not None:
        filters.append(("date", ">=", pd.Timestamp(start)))
    if end is not None:
        filters.append(("date", "<=", pd.Timestamp(end)))
    filters = filters or None

    frames = []
    for p in sorted(DATA_DIR.glob("kline_*.parquet")):
        frames.append(pd.read_parquet(p, filters=filters))
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

def load_meta():
    return pd.read_parquet(DATA_DIR / "stock_list.parquet")

def load_index():
    return pd.read_parquet(DATA_DIR / "index_sh.parquet")

if __name__ == "__main__":
    df = load_kline()
    print(f"总行数：{len(df):,}")
    print(f"股票数：{df['code'].nunique()}")
    print(f"日期范围：{df['date'].min()} ~ {df['date'].max()}")
