# Speedpi

This is a tiny speedtest tool for Raspberry Pi using Ookla's speedtest API.

## Requirements
A Raspberry Pi with internet access or another Linux machine. 

## Installation

`pip install -r requirements.txt`

## Running

On a terminal type

`chmod +x start.sh`

and 

`./start.sh`


The Script starts a bunch of speedtests and writes the results into a CSV file. At first - if no csv file exists. The script will create one.

## Notes

The time is UTC time. To doublecheck type `date -u` into a terminal. 
To check crontab jobs type `crontab -l` into a terminal. To delete all jobs type `crontab -r`