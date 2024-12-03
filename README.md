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
Most Accessed     Frequently Endpoint:
Endpoint          Access Count
login             13
home              5
about             5
dashboard         3
contact           2
register          2
profile           2
feedback          2
```

```plaintext
Suspicious Activity:
IP Address       Failed Login Attempts
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

---

This README provides a clear and concise guide to understanding and running the VRV Security Log Analysis Script. It covers the objectives, features, requirements, how to run the script, expected output, and a sample log file for testing.
