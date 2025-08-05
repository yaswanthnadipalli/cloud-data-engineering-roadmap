import pandas as pd      
import random            
import time             

# in this exercise we will get real time data 

df = pd.DataFrame(columns=["timestamp", "temperature", "humidity"])
df.to_csv("realtime_data.csv", index=False)

for _ in range(10):  
    temp = round(random.uniform(25, 40), 2)  # random temperature between 25 and 40
    humidity = round(random.uniform(40, 80), 2)  # random humidity between 40 and 80
    timestamp = pd.Timestamp.now()  # current time

    
    new_data = pd.DataFrame([[timestamp, temp, humidity]], columns=["timestamp", "temperature", "humidity"])

    new_data.to_csv("realtime_data.csv", mode='a', header=False, index=False)

    print(f"Data written: {timestamp}, Temp: {temp}, Humidity: {humidity}")
    time.sleep(1)  

