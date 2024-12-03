# VRV Security’s Python Intern Assignment
Introduction
This submission is a Python script designed to analyze log files for VRV Security, a global powerhouse in AI-driven cybersecurity solutions. The script processes log files to extract and analyze key information, fulfilling the requirements of the VRV Security Python Intern Assignment.

Objective
The goal of this assignment is to assess the ability to write a Python script that processes log files to extract and analyze key information. This assignment evaluates proficiency in file handling, string manipulation, and data analysis, which are essential skills for cybersecurity-related programming tasks.

Core Requirements
The Python script implements the following functionalities:

Count Requests per IP Address:

Parse the provided log file to extract all IP addresses.

Calculate the number of requests made by each IP address.

Sort and display the results in descending order of request counts.

Identify the Most Frequently Accessed Endpoint:

Extract the endpoints (e.g., URLs or resource paths) from the log file.

Identify the endpoint accessed the highest number of times.

Provide the endpoint name and its access count.

Detect Suspicious Activity:

Identify potential brute force login attempts by:

Searching for log entries with failed login attempts (e.g., HTTP status code 401 or a specific failure message like "Invalid credentials").

Flagging IP addresses with failed login attempts exceeding a configurable threshold (default: 10 attempts).

Display the flagged IP addresses and their failed login counts.

Output Results:

Display the results in a clear, organized format in the terminal.

Save the results to a CSV file named log_analysis_results.csv with the following structure:

Requests per IP: Columns: IP Address, Request Count

Most Accessed Endpoint: Columns: Endpoint, Access Count

Suspicious Activity: Columns: IP Address, Failed Login Count

Sample Log File
A sample log file named sample.log is provided for testing the script. The log file contains entries similar to the following:

bash
Copy
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
...
Evaluation Criteria
Functionality:

The script processes the provided log file correctly and fulfills all requirements.

All sections of the analysis are implemented: IP request counts, most accessed endpoint, and suspicious activity detection.

Code Quality:

Clear, well-organized, and modular code.

Proper use of comments, meaningful variable names, and adherence to Python best practices.

Performance:

The script handles the provided log file efficiently and can scale to larger files without significant delays.

Output:

Correctly formatted output in both the terminal and the saved CSV file.

The CSV file structure matches the specified format.

Getting Started
Prerequisites
Python 3.x

re module (standard library)

csv module (standard library)

collections module (standard library)

Installation
Clone the repository:

bash
Copy
git clone https://github.com/yourusername/vrv-security-log-analysis.git
cd vrv-security-log-analysis
Ensure you have Python installed:

bash
Copy
python --version
Usage
Place your log file in the same directory as the script and name it sample.log.

Run the script:

bash
Copy
python log_analysis.py
The script will output the results in the terminal and save them to log_analysis_results.csv.

Example Output
Terminal
bash
Copy
Requests per IP:
IP Address      Request Count
203.0.113.5     8
198.51.100.23   8
192.168.1.1     7
10.0.0.2        6
192.168.1.100   5

Most Frequently Accessed Endpoints:
/login (Accessed 13 times)
/home (Accessed 5 times)
/about (Accessed 5 times)
/dashboard (Accessed 3 times)
/contact (Accessed 2 times)
/register (Accessed 2 times)
/profile (Accessed 2 times)
/feedback (Accessed 2 times)

Suspicious Activity Detected:
IP Address      Failed Login Attempts
203.0.113.5     8
192.168.1.100   5
CSV File (log_analysis_results.csv)
csv
Copy
Requests per IP,IP Address,Request Count
Requests per IP,203.0.113.5,8
Requests per IP,198.51.100.23,8
Requests per IP,192.168.1.1,7
Requests per IP,10.0.0.2,6
Requests per IP,192.168.1.100,5

Most Accessed Endpoints,Endpoint,Access Count
Most Accessed Endpoints,/login,13
Most Accessed Endpoints,/home,5
Most Accessed Endpoints,/about,5
Most Accessed Endpoints,/dashboard,3
Most Accessed Endpoints,/contact,2
Most Accessed Endpoints,/register,2
Most Accessed Endpoints,/profile,2
Most Accessed Endpoints,/feedback,2

Suspicious Activity,IP Address,Failed Login Count
Suspicious Activity,203.0.113.5,8
Suspicious Activity,192.168.1.100,5
Contributing
Contributions are welcome! Please read the CONTRIBUTING.md file for details on how to contribute to this project.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
VRV Security for providing the assignment and guiding principles.

Open-source community for providing valuable resources and tools.

This submission description provides a comprehensive overview of the script's functionality, usage, and expected output. It also includes instructions for setting up and running the script, as well as guidelines for contributing to the project.
