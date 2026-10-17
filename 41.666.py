import pandas as pd

df = pd.read_csv("nifty_1min.csv")

df["datetime"] = pd.to_datetime(df["datetime"])
df = df.sort_values("datetime").set_index("datetime")

# Keep NSE regular trading hours
df = df.between_time("09:15", "15:30")

# Anchor custom candles at 09:15 IST
candles_416666 = (
 df.resample(
 "2500s",
 origin="start_day",
 offset="9h15min",
 label="left",
 closed="left"
 )
.agg({
 "open": "first",
 "high": "max",
 "low": "min",
 "close": "last",
 "volume": "sum"
 })
.dropna()
)

candles_416666.to_csv("nifty_41_6666_minute_candles.csv")
print(candles_416666.head())
