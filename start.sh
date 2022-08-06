#!/bin/bash

csv_filename=speedtests.csv

# create a csv file if file does not exist
if ! [[ -f $csv_filename ]]
then
    echo "Creating a csv file"
    speedtest-cli --csv-header >> $csv_filename
fi

# start the speedtest routine
python3 src/start.py