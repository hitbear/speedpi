import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil import parser as dateparser

df = pd.read_csv('speedtests.csv')
df.to_numpy()

downloads = df['Download'].to_numpy()
downloads_in_mbits = downloads/1000000
downloads_in_mbits_round = downloads_in_mbits.round(2)
mean_download_mbits = downloads_in_mbits.mean().round(2)
median_downloads = np.median(downloads_in_mbits_round)
mid_down = np.max(downloads_in_mbits_round) - np.min(downloads_in_mbits_round) 
mid_down = mid_down/2 + np.min(downloads_in_mbits_round) 

print("Mean Download " + str(mean_download_mbits) + " MBit/s")

uploads = df['Upload'].to_numpy()
uploads_in_mbits = uploads/1000000
uploads_in_mbits_round = uploads_in_mbits.round(2)
mean_upload_mbits = uploads_in_mbits.mean().round(2)
median_uploads = np.median(uploads_in_mbits_round)
mid_up = np.max(uploads_in_mbits_round) - np.min(uploads_in_mbits_round) 
mid_up = mid_up/2 + np.min(uploads_in_mbits_round) 

print("Mean Upload " + str(mean_upload_mbits) + " MBit/s")

timestamps = df['Timestamp'].to_numpy()
timestamps = [dateparser.parse(time) for time in timestamps]

########################################################################
### Some plots

fig = plt.figure()
ax = fig.add_subplot()

ax.set_title("Download Speed")
ax.plot(timestamps, downloads_in_mbits_round, label="Download Speed")
ax.set_xlabel("Time")
ax.set_ylabel("MBit/s")
ax.grid(True)
ax.fill_between(timestamps, 26, 34, alpha=0.1)
ax.fill_between(timestamps, downloads_in_mbits_round - 1, downloads_in_mbits_round + 1, alpha=0.3)
ax.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_title("Up- and Download Speed")
ax.plot(timestamps, downloads_in_mbits_round, label="Download Speed")
ax.plot(timestamps, uploads_in_mbits_round, label="Upload Speed")
ax.set_xlabel("Time")
ax.set_ylabel("MBit/s")
ax.grid(True)
ax.fill_between(timestamps, 26, 34, alpha=0.1)
ax.fill_between(timestamps, 2, 7, alpha=0.1)
ax.fill_between(timestamps, downloads_in_mbits_round - 1, downloads_in_mbits_round + 1, alpha=0.3)
ax.fill_between(timestamps, uploads_in_mbits_round - 1, uploads_in_mbits_round + 1, alpha=0.3)
ax.legend()
plt.show()

### Box 

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(9, 4))
bplot1 = ax1.boxplot(downloads_in_mbits_round,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     )  # will be used to label x-ticks
ax1.set_title('Download')
ax1.text(0.7,mid_down, "Mean:   " + str(mean_download_mbits) 
            + "\nMin:      " + str(np.min(downloads_in_mbits_round))
            + "\nMax:     " + str(np.max(downloads_in_mbits_round))
            + "\nMedian:" + str(median_downloads),
            style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 10}
            )

bplot3 = ax3.boxplot(uploads_in_mbits_round,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     )  # will be used to label x-ticks
ax3.set_title('Upload')
ax3.text(0.7,mid_up, "Mean:   " + str(mean_upload_mbits) 
            + "\nMin:      " + str(np.min(uploads_in_mbits_round))
            + "\nMax:     " + str(np.max(uploads_in_mbits_round))
            + "\nMedian:" + str(median_uploads),
            style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 10}
            )

bplot2 = ax2.boxplot(downloads_in_mbits_round,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     )  # will be used to label x-ticks
ax2.set_title('Download (notched)')
bplot4 = ax4.boxplot(uploads_in_mbits_round,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     )  # will be used to label x-ticks
ax4.set_title('Upload (notched')

plt.show()