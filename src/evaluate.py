import pandas as pd
import matplotlib.pyplot as plt

from dateutil import parser as dateparser

df = pd.read_csv('speedtests.csv')
df.to_numpy()

downloads = df['Download'].to_numpy()
downloads_in_mbits = downloads/1000000
downloads_in_mbits_round = downloads_in_mbits.round(2)
mean_download_mbits = downloads_in_mbits.mean().round(2)

print("Mean Download " + str(mean_download_mbits) + " MBit/s")

uploads = df['Upload'].to_numpy()
uploads_in_mbits = uploads/1000000
uploads_in_mbits_round = uploads_in_mbits.round(2)
mean_upload_mbits = uploads_in_mbits.mean().round(2)

print("Mean Upload " + str(mean_upload_mbits) + " MBit/s")

timestamps = df['Timestamp'].to_numpy()
timestamps = [dateparser.parse(time) for time in timestamps]

fig = plt.figure()
ax = fig.add_subplot()

ax.set_title("Download Speed")
ax.plot(timestamps, downloads_in_mbits_round)
ax.set_xlabel("Zeit")
ax.set_ylabel("MBit/s")
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_title("Up- and Download Speed")
ax.plot(timestamps, downloads_in_mbits_round)
ax.plot(timestamps, uploads_in_mbits_round)
ax.set_xlabel("Zeit")
ax.set_ylabel("MBit/s")
plt.show()
