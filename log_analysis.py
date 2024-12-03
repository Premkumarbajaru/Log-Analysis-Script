import re
import csv
from collections import defaultdict, Counter


def parse_log_file(log_file):
    """
    Parse the log file and return a list of dictionaries containing log entries.
    """
    log_entries = []
    log_pattern = r'(\d+\.\d+\.\d+\.\d+)\s-\s-\s\[.*?\]\s"(\w+)\s(.*?)\sHTTP/\d\.\d"\s(\d+)\s.*?(\".*?\")?'

    try:
        with open(log_file, 'r') as file:
            for line in file:
                match = re.match(log_pattern, line)
                if match:
                    ip_address = match.group(1)
                    method = match.group(2)
                    endpoint = match.group(3)
                    status_code = match.group(4)
                    message = match.group(5) or ""  # Handle missing messages
                    log_entries.append({
                        'ip_address': ip_address,
                        'method': method,
                        'endpoint': endpoint,
                        'status_code': status_code,
                        'message': message.strip('"')
                    })
    except FileNotFoundError:
        print(f"Error: File {log_file} not found.")
    except Exception as e:
        print(f"Error while parsing the log file: {e}")

    return log_entries


def count_requests_per_ip(log_entries):
    """
    Count the number of requests made by each IP address.
    """
    ip_request_count = Counter(entry['ip_address'] for entry in log_entries)
    return sorted(ip_request_count.items(), key=lambda x: x[1], reverse=True)


def most_frequent_endpoint(log_entries):
    """
    Identify the most frequently accessed endpoints.
    """
    endpoint_count = Counter(entry['endpoint'] for entry in log_entries)
    return endpoint_count.most_common()


def detect_suspicious_activity(log_entries, threshold=10):
    """
    Detect potential brute force login attempts.
    """
    failed_logins = defaultdict(int)
    for entry in log_entries:
        if entry['status_code'] == '401' and 'Invalid credentials' in entry['message']:
            failed_logins[entry['ip_address']] += 1

    return sorted([(ip, count) for ip, count in failed_logins.items() if count > threshold], key=lambda x: x[1], reverse=True)


def save_results_to_csv(results, filename):
    """
    Save the analysis results to a CSV file.
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write Count Requests per IP Address
            writer.writerow(["Count Requests per IP Address:"])
            writer.writerow(["IP Address", "Request Count"])
            for ip, count in results['requests_per_ip']:
                writer.writerow([ip, count])

            # Write Most Accessed Frequently Endpoint
            writer.writerow([])
            writer.writerow(["Most Accessed Frequently Endpoint:"])
            writer.writerow(["Endpoint", "Access Count"])
            for endpoint, count in results['most_accessed_endpoints']:
                writer.writerow([endpoint, count])

            # Write Suspicious Activity
            writer.writerow([])
            writer.writerow(["Suspicious Activity:"])
            writer.writerow(["IP Address", "Failed Login Attempts:"])
            for ip, count in results['suspicious_activity']:
                writer.writerow([ip, count])

        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error while saving results to CSV: {e}")


def display_results(results):
    """
    Display the analysis results in the terminal.
    """
    print("Requests per IP:")
    print("IP Address\tRequest Count")
    for ip, count in results['requests_per_ip']:
        print(f"{ip}\t{count}")

    print("\nMost Frequently Accessed Endpoints:")
    for endpoint, count in results['most_accessed_endpoints']:
        print(f"{endpoint} (Accessed {count} times)")

    print("\nSuspicious Activity Detected:")
    print("IP Address\tFailed Login Attempts")
    for ip, count in results['suspicious_activity']:
        print(f"{ip}\t{count}")


def main():
    log_file = r"C:\Users\PREMKUMAR BAJARU\Desktop\sample.log"  # Update the path to the log file
    log_entries = parse_log_file(log_file)

    if not log_entries:
        print("No log entries found.")
        return

    print(f"Parsed {len(log_entries)} entries from the log file.")

    # Analyze log data
    requests_per_ip = count_requests_per_ip(log_entries)
    most_accessed_endpoints = most_frequent_endpoint(log_entries)
    suspicious_activity = detect_suspicious_activity(log_entries)

    # Organize results
    results = {
        'requests_per_ip': requests_per_ip,
        'most_accessed_endpoints': most_accessed_endpoints,
        'suspicious_activity': suspicious_activity
    }

    # Display results
    display_results(results)

    # Save results to CSV
    save_results_to_csv(results, 'log_analysis_results.csv')


if __name__ == "__main__":
    main()