# VRV Security’s Python Intern Assignment

## Objective

The primary goal of this script is to:
1. Count the number of requests made by each IP address.
2. Identify the most frequently accessed endpoint.
3. Detect suspicious activity, such as excessive failed login attempts.

## Features

1. **Requests per IP Address**:
   - Lists the number of requests made by each IP address.
   - Sorts the results in descending order of request counts.

2. **Most Accessed Endpoint**:
   - Identifies the endpoint (URL or resource path) that was accessed the most number of times.

3. **Suspicious Activity**:
   - Flags IP addresses with suspicious behavior, such as excessive failed login attempts.
   - Uses a configurable threshold (default: 10 failed login attempts) to detect suspicious activity.

## Requirements

- Python `3.10.0` or `higher`
- `re` module (standard library)
- `csv` module (standard library)
- `collections` module (standard library)

## How to Run

1. **Clone the Repository**:
   ```bash
   https://github.com/Premkumarbajaru/Log-Analysis-Script.git
   cd log_analysis
   ```

2. **Place the Log File**:
   - Ensure the `sample.log` file is in the same directory as the script.

3. **Run the Script**:
   ```bash
   python log_analysis.py
   ```

## Output

The script will display the analysis results in the terminal and save them to a CSV file named `log_analysis_results.csv`.

### Terminal Output Example

```plaintext

Requests per IP:
IP Address      Request Count
203.0.113.5     8
198.51.100.23   8
192.168.1.1     7
10.0.0.2        6
192.168.1.100   5

Most Frequently Accessed Endpoints:
login (Accessed 13 times)
home (Accessed 5 times)
about (Accessed 5 times)
dashboard (Accessed 3 times)
contact (Accessed 2 times)
register (Accessed 2 times)
profile (Accessed 2 times)
feedback (Accessed 2 times)

Suspicious Activity Detected:
IP Address      Failed Login Attempts
Results saved to log_analysis_results.csv
```

### CSV File Structure

The CSV file will have the following structure:

```plaintext
Count Requests per IP Address:
IP Address        Request Count
203.0.113.5       8
198.51.100.23     8
192.168.1.1       7
10.0.0.2          6
192.168.1.100     5
```

```plaintext
Most Accessed Frequently Endpoint:
Endpoint      Access Count
login        13
home         5
about        5
dashboard    3
contact      2
register     2
profile      2
feedback     2
```

```plaintext
Suspicious Activity:
IP Address,Failed Login Attempts
```

## Sample Log File

A sample log file named `sample.log` is provided for testing the script. The log file contains entries similar to the following:

```plaintext
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:37 +0000] "GET /contact HTTP/1.1" 200 312
198.51.100.23 - - [03/Dec/2024:10:12:38 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:39 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:40 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:41 +0000] "GET /dashboard HTTP/1.1" 200 1024
198.51.100.23 - - [03/Dec/2024:10:12:42 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:12:43 +0000] "GET /dashboard HTTP/1.1" 200 1024
203.0.113.5 - - [03/Dec/2024:10:12:44 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:45 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:46 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:47 +0000] "GET /profile HTTP/1.1" 200 768
192.168.1.1 - - [03/Dec/2024:10:12:48 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:49 +0000] "POST /feedback HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:12:50 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.1 - - [03/Dec/2024:10:12:51 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:52 +0000] "GET /about HTTP/1.1" 200 256
203.0.113.5 - - [03/Dec/2024:10:12:53 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:12:54 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:55 +0000] "GET /contact HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:12:56 +0000] "GET /home HTTP/1.1" 200 512
192.168.1.100 - - [03/Dec/2024:10:12:57 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
203.0.113.5 - - [03/Dec/2024:10:12:58 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:59 +0000] "GET /dashboard HTTP/1.1" 200 1024
192.168.1.1 - - [03/Dec/2024:10:13:00 +0000] "GET /about HTTP/1.1" 200 256
198.51.100.23 - - [03/Dec/2024:10:13:01 +0000] "POST /register HTTP/1.1" 200 128
203.0.113.5 - - [03/Dec/2024:10:13:02 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
192.168.1.100 - - [03/Dec/2024:10:13:03 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:13:04 +0000] "GET /profile HTTP/1.1" 200 768
198.51.100.23 - - [03/Dec/2024:10:13:05 +0000] "GET /about HTTP/1.1" 200 256
192.168.1.1 - - [03/Dec/2024:10:13:06 +0000] "GET /home HTTP/1.1" 200 512
198.51.100.23 - - [03/Dec/2024:10:13:07 +0000] "POST /feedback HTTP/1.1" 200 128
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

---

This README provides a clear and concise guide to understanding and running the VRV Security Log Analysis Script. It covers the objectives, features, requirements, how to run the script, expected output, and a sample log file for testing.
