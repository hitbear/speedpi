import pandas as pd
import matplotlib.pyplot as plt

from dateutil import parser as dateparser

df = pd.read_csv('speedtests.csv')

downloads = df['Download']
downloads_in_mbits = downloads/1000000
downloads_in_mbits_round = downloads_in_mbits.round(2)
mean_download_mbits = downloads_in_mbits.mean().round(2)

print("Mean Download " + str(mean_download_mbits) + " MBit/s")

uploads = df['Upload']
uploads_in_mbits = uploads/1000000
uploads_in_mbits_round = uploads_in_mbits.round(2)
mean_upload_mbits = uploads_in_mbits.mean().round(2)

print("Mean Upload " + str(mean_upload_mbits) + " MBit/s")

timestamps = df['Timestamp']
timestamps = [dateparser.parse(time) for time in df.Timestamp]

plt.plot(timestamps, downloads_in_mbits_round)
plt.show()

plt.plot(timestamps, downloads_in_mbits_round)
plt.plot(timestamps, uploads_in_mbits_round)

plt.show()
