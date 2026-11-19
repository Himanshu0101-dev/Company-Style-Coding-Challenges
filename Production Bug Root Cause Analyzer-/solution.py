from collections import Counter


class RootCauseAnalyzer:

    def __init__(self, logs):
        self.logs = logs

    def find_root_cause(self):
        for log in self.logs:
            if "Database Timeout" in log:
                return "Database Timeout"

            if "API Failure" in log:
                return "API Failure"

            if "Memory Leak" in log:
                return "Memory Leak"

            if "Authentication Failed" in log:
                return "Authentication Failure"

            if "Network Error" in log:
                return "Network Issue"

        return "Unknown"

    def get_severity(self):
        severity_score = {
            "CRITICAL": 100,
            "ERROR": 80,
            "WARN": 50,
            "INFO": 10
        }

        max_score = 0

        for log in self.logs:
            for level, score in severity_score.items():
                if level in log:
                    max_score = max(max_score, score)

        if max_score >= 100:
            return "CRITICAL"
        elif max_score >= 80:
            return "HIGH"
        elif max_score >= 50:
            return "MEDIUM"
        else:
            return "LOW"

    def suggest_fix(self, root_cause):

        fixes = {
            "Database Timeout": [
                "Check DB connectivity",
                "Increase connection pool",
                "Optimize slow queries"
            ],
            "API Failure": [
                "Verify endpoint availability",
                "Retry failed requests",
                "Check API gateway logs"
            ],
            "Memory Leak": [
                "Inspect object usage",
                "Release unused memory",
                "Profile application"
            ],
            "Authentication Failure": [
                "Validate tokens",
                "Check user permissions",
                "Review authentication service"
            ],
            "Network Issue": [
                "Check firewall rules",
                "Verify DNS resolution",
                "Review network latency"
            ]
        }

        return fixes.get(root_cause, ["Investigate manually"])

    def generate_report(self):

        root_cause = self.find_root_cause()
        severity = self.get_severity()
        fixes = self.suggest_fix(root_cause)

        print("=" * 50)
        print("INCIDENT REPORT")
        print("=" * 50)

        print(f"Root Cause : {root_cause}")
        print(f"Severity   : {severity}")

        print("\nRecommended Fixes:")
        for fix in fixes:
            print(f"- {fix}")


if __name__ == "__main__":

    logs = [
        "INFO User Login Success",
        "ERROR Payment Success TXN123",
        "ERROR Database Timeout",
        "CRITICAL Order Creation Failed TXN123",
        "INFO Email Notification Sent"
    ]

    analyzer = RootCauseAnalyzer(logs)
    analyzer.generate_report()
