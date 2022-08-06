from crontab import CronTab

def main():
    cron = CronTab(user=True)
    job = cron.new(command='python3 speedpi/src/speedpi.py', comment="speedpi speedtest")
    job.minute.every(30)

    cron.write()
    print("cron.write()")

if __name__ == "__main__":
    main()