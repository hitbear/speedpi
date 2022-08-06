import pandas as pd

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