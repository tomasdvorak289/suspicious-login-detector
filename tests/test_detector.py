from src.detector import detect_suspicious_logins

test_logins = [
     {"ip": "192.168.1.1", "status": "Failed"},
     {"ip": "192.168.1.1", "status": "Failed"},
     {"ip": "192.168.1.1", "status": "Failed"},
     {"ip": "192.168.1.2", "status": "Success"},
     {"ip": "192.168.1.2", "status": "Failed"}
]

print(detect_suspicious_logins(test_logins))