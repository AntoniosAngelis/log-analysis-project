with open("log.txt", "r") as file:
    logs = file.readlines()

error_count = 0
warning_count = 0
failed_login_count = 0
unauthorized_count = 0

for log in logs:
    if "ERROR" in log:
        error_count += 1
        print(f"[ERROR] {log.strip()}")

    if "WARNING" in log:
        warning_count += 1
        print(f"[WARNING] {log.strip()}")

    if "Failed login" in log:
        failed_login_count += 1
        print(f"[FAILED LOGIN] {log.strip()}")

    if "Unauthorized" in log:
        unauthorized_count += 1
        print(f"[UNAUTHORIZED ACCESS] {log.strip()}")

print("\nSummary:")
print(f"Errors: {error_count}")
print(f"Warnings: {warning_count}")
print(f"Failed logins: {failed_login_count}")
print(f"Unauthorized access attempts: {unauthorized_count}")


if failed_login_count >= 5:
    print("\n⚠️ Possible Brute Force Attack Detected!")
