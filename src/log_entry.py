class LogEntry:
    def __init__(self, ip, timestamp, method, endpoint, status_code):
        self.ip = ip
        self.timestamp = timestamp
        self.method = method
        self.endpoint = endpoint
        self.status_code = status_code

