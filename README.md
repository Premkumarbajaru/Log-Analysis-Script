# VRV Security’s Python Intern Assignment

## Objective
The goal of this assignment is to assess the ability to write a Python script that processes log files to extract and analyze key information. This assignment evaluates proficiency in file handling, string manipulation, and data analysis, which are essential skills for cybersecurity-related programming tasks.

## Core Requirements
The Python script implements the following functionalities:

### 1)Count Requests per IP Address:
Parse the provided log file to extract all IP addresses.
Calculate the number of requests made by each IP address.
Sort and display the results in descending order of request counts.
Count Requests per IP Address:
``` bash
    IP Address           Request Count
    192.168.1.1          69
    203.0.113.5          8
    198.51.100.23        8
    10.0.0.2             6
    192.168.1.100        5

IP Address         Request Count
203.0.113.5        8
198.51.100.23      8
192.168.1.1        7
10.0.0.2           6
192.168.1.100      5
```

### 2)Identify the Most Frequently Accessed Endpoint:
Extract the endpoints (e.g., URLs or resource paths) from the log file.
Identify the endpoint accessed the highest number of times.


### 3)Detect Suspicious Activity:
Identify potential brute force login attempts by:
Searching for log entries with failed login attempts (e.g., HTTP status code 401 or a specific failure message like "Invalid credentials").
Flagging IP addresses with failed login attempts exceeding a configurable threshold (default: 10 attempts).
Display the flagged IP addresses and their failed login counts.

## Output Results:
the results in a clear, organized format in the terminal.
Save the results to a CSV file named log_analysis_results.csv with the following structure:

Requests per IP: Columns: IP Address, Request Count
Most Accessed Endpoint: Columns: Endpoint, Access Count
Suspicious Activity: Columns: IP Address, Failed Login Count

Sample Log File
A sample log file named sample.log is provided for testing the script. The log file contains entries similar to the following:


## Getting Started
Prerequisites
Python 3.10.0
re module (standard library)
csv module (standard library)
collections module (standard library)

