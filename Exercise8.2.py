import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("realtime_data.csv")

# Convert timestamp column to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Step 3: Plot temperature and humidity
plt.figure(figsize=(10, 5))  # 10 length and 5 is the height

plt.plot(df["timestamp"], df["temperature"], label="Temperature", marker='o')  # x-axis is timestamp and y axix is value temperature and humidity
plt.plot(df["timestamp"], df["humidity"], label="Humidity", marker='x')

plt.title("Real-Time Sensor Data")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)  #   makes the time stamps rotate by 45 degrees easy to read the data 
plt.tight_layout()
plt.show()
