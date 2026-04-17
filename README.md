# A股日线数据集

**股票数**：5,197 只（沪深主板、中小板、创业板、科创板）
**时间**：2020-06-01 ~ 2026-04-03
**总行数**：5,788,837
**更新**：2026-04-18

## 文件清单

| 文件 | 内容 |
|---|---|
| `kline_000.parquet` | 528 只股票, 31,076 行 (0.9 MB) |
| `kline_002.parquet` | 964 只股票, 1,145,521 行 (31.8 MB) |
| `kline_300.parquet` | 1396 只股票, 1,673,542 行 (48.1 MB) |
| `kline_600.parquet` | 1703 只股票, 2,293,139 行 (63.4 MB) |
| `kline_688.parquet` | 606 只股票, 645,559 行 (19.4 MB) |
| `stock_list.parquet` | 股票基本信息（code, name, sector） |
| `index_sh.parquet` | 上证指数日线 |
| `load.py` | 一键载入函数 |

## 字段说明（kline_*.parquet）

| 列 | 类型 | 说明 |
|---|---|---|
| code | str | 股票代码（6位数字） |
| date | datetime | 交易日 |
| open / high / low / close | float32 | 开/高/低/收盘价 |
| volume | Int64 | 成交量（停牌日为 NA） |
| amount | float64 | 成交额（元） |
| turn | float32 | 换手率（%） |
| pctChg | float32 | 涨跌幅（%） |

## 快速开始

```python
from load import load_kline, load_meta, load_index

df     = load_kline()                            # 全量（~580 万行）
single = load_kline(codes=["000001","600000"])   # 几只股票
recent = load_kline(start="2025-01-01")          # 指定日期起
meta   = load_meta()
idx    = load_index()
```

## 备注

- 价格为 baostock 默认（前复权）
- 约 685 只老股票的早期历史缺失，仅含 2026 年 1 月以来
- 约 504 只股票末期停牌，结束日为 2026-03-27
