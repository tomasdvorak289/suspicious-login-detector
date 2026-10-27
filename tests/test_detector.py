from src.detector import detect_suspicious_logins
from src.loader import load_logins

logins = load_logins("data/logins.csv")
print(detect_suspicious_logins(logins))
