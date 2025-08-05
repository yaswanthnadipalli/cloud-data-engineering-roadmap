import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

timestamps = pd.date_range(start="2025-08-01", periods=100, freq='H')
# This creates a list of 100 timestamps, starting from 2025-08-01, with a frequency of 1 hour.
temperature = np.random.normal(loc=30, scale=5, size=100)


df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature
})

df["temp_avg"] = df["temperature"].rolling(window=5).mean()

plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["temperature"], label="Original Temperature", alpha=0.6)
plt.plot(df["timestamp"], df["temp_avg"], label="5-hour Moving Avg", color='red', linewidth=2)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature with Moving Average")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
