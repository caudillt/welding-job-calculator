# Simple Welding Job Calculator

print("=== WELDING JOB CALCULATOR ===")

welds = int(input("How many welds are required? "))
minutes_per_weld = float(input("Minutes per weld: "))

total_minutes = welds * minutes_per_weld

hours = int(total_minutes // 60)
remaining_minutes = total_minutes % 60

print("\n--- JOB ESTIMATE ---")
print(f"Number of welds: {welds}")
print(f"Minutes per weld: {minutes_per_weld}")
print(f"Total welding time: {total_minutes} minutes")
print(f"Estimated time: {hours} hours and {remaining_minutes:.0f} minutes")
