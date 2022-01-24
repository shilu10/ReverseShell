# ReverseShell

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Installation](#Installation)
* [Setup](#setup)


## General info
This project is based on the concept of Backdoor. Backdoor is a malicious file used by the hacker to hack the Windows Desktop particularly. These files are not sensitive or it won't caught in stateless firewall.This File is coded based on getting the connection from the victim.So in the stateless firewall allows the connection from that p.c

## Technologies
Project is created with:
* Python 3.9.2
* json
* base64
* csv
* re
* argparse
* socket
* sys
* subprocess


## Installation

```bash
pip install base64
```

```bash
pip install argparse
```
```bash
pip install requests
```

## Setup
To run this project,clone this repository in your machine:

* Make sure to have a Python installed 

```
$ cd ../AmazonElectronicScraper
$ python3 run.py -p 1 -f "amazon.csv" -s "laptop"
$ python3 run.py -h 
```
* python3 run.py -h - To see the description and to get the help
* -f argument - It is used to specify the filename .Where you like to save the result.Please make sure to use the csv extension.
* -s argument - It is used to specify a search keyword .Like mobile phones, Latpops
* -p argument -It is used to speicfy , how many page you need to extract.
