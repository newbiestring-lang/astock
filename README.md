# A股日线数据（parquet 版）

**范围**：沪市/深市主板、中小板、创业板、科创板，约 4,697 只股票
**时间**：2020-06-01 ~ 2026-04-03（部分次新股从上市日开始）
**更新**：2026-04-18

## 文件清单

| 文件 | 内容 | 行数 |
|---|---|---|
| `kline.parquet` | 所有股票日线长表 | ~5,788,837 |
| `stock_list.parquet` | 股票代码、名称、行业 | 5,512 |
| `index_sh.parquet` | 上证指数日线 | 1417 |

## `kline.parquet` 字段

| 列名 | 类型 | 说明 |
|---|---|---|
| code | str | 股票代码（纯数字，如 600000） |
| date | datetime | 交易日 |
| open / high / low / close | float32 | 开/高/低/收盘价 |
| volume | int64 | 成交量（股） |
| amount | float64 | 成交额（元） |
| turn | float32 | 换手率（%） |
| pctChg | float32 | 涨跌幅（%） |

## 快速开始

```python
import pandas as pd

# 全量读入（内存约 200~400 MB）
df = pd.read_parquet("kline.parquet")

# 只读某只股票（利用 pyarrow 的下推过滤）
pingan = pd.read_parquet(
    "kline.parquet",
    filters=[("code", "==", "000001")],
)

# 读指定日期段
recent = pd.read_parquet(
    "kline.parquet",
    filters=[("date", ">=", "2025-01-01")],
)

# 结合股票信息
meta = pd.read_parquet("stock_list.parquet")
df_with_name = df.merge(meta[["code", "name", "sector"]], on="code")
```

## 备注

- 所有价格均为 baostock 默认设置（前复权），后续可按需自行处理
- 部分老股票（约 685 只）历史段缺失，仅含 2026 年初至今的数据
- 大约 504 只股票结束日为 2026-03-27（末期停牌/摘牌）
