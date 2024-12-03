# VRV Security’s Python Intern Assignment

## Objective
The goal of this assignment is to assess the ability to write a Python script that processes log files to extract and analyze key information. This assignment evaluates proficiency in file handling, string manipulation, and data analysis, which are essential skills for cybersecurity-related programming tasks.

## Core Requirements
The Python script implements the following functionalities:

### 1)Count Requests per IP Address:
Parse the provided log file to extract all IP addresses.
Calculate the number of requests made by each IP address.
Sort and display the results in descending order of request counts.

### 2)Identify the Most Frequently Accessed Endpoint:
Extract the endpoints (e.g., URLs or resource paths) from the log file.
Identify the endpoint accessed the highest number of times.
Provide the endpoint name and its access count.

### 3)Detect Suspicious Activity:
Identify potential brute force login attempts by:
Searching for log entries with failed login attempts (e.g., HTTP status code 401 or a specific failure message like "Invalid credentials").
Flagging IP addresses with failed login attempts exceeding a configurable threshold (default: 10 attempts).
Display the flagged IP addresses and their failed login counts.

## Output Results:

Display the results in a clear, organized format in the terminal.
Save the results to a CSV file named log_analysis_results.csv with the following structure:

Requests per IP: Columns: IP Address, Request Count
Most Accessed Endpoint: Columns: Endpoint, Access Count
Suspicious Activity: Columns: IP Address, Failed Login Count

Sample Log File
A sample log file named sample.log is provided for testing the script. The log file contains entries similar to the following:

bash
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
...


## Getting Started
### Prerequisites
Python 3.10.0
re module (standard library)
csv module (standard library)
collections module (standard library)

## Installation
Clone the repository:

bash
git clone https://github.com/yourusername/vrv-security-log-analysis.git
cd vrv-security-log-analysis
Ensure you have Python installed:

bash
python --version
Usage
Place your log file in the same directory as the script and name it sample.log.

## Run the script:

bash
python log_analysis.py
The script will output the results in the terminal and save them to log_analysis_results.csv.

