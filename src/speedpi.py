#!/usr/bin/env python3
import os


def speedpi():
    speedtest = "speedtest-cli "
    # add arguments
    speedtest = speedtest + "--csv "
    # specify output file
    speedtest = speedtest + ">> speedpi/speedtests.csv"

    # start the command
    os.system(speedtest)


if __name__ == "__main__":
    speedpi()