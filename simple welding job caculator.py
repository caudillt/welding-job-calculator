# Simple Welding Job Calculator

print("=== WELDING JOB CALCULATOR ===")

welds = int(input("How many welds are required? "))
minutes_per_weld = float(input("Minutes per weld: "))

total_minutes = welds * minutes_per_weld

print("\n--- JOB ESTIMATE ---")
print(f"Number of welds: {welds}")
print(f"Minutes per weld: {minutes_per_weld}")
print(f"Total welding time: {total_minutes} minutes")