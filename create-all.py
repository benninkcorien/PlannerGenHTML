import subprocess
import time

# Saves to 00planner/weasyplanner.pdf
generatecover = ["py", "generate-cover.py"]
generateindex = ["py", "generate-index.py"]
generatedaily = ["py", "generate-daily-pages.py"]
generatemonthlycals = ["py", "generate-monthly-calendars.py"]
generateyearly = ["py", "generate-yearly-pages.py"]
generateplanner = ["py", "generate-planner.py"]
generateweasypdf = ["py", "generate-weasy-plannerfile.py"]


# Use subprocess to run the command
try:
    subprocess.run(generatecover, check=True)
    subprocess.run(generateindex, check=True)
    subprocess.run(generatedaily, check=True)
    subprocess.run(generatemonthlycals, check=True)
    subprocess.run(generateyearly, check=True)
    subprocess.run(generateplanner, check=True)
    # Wait for file generation to complete
    time.sleep(8)
    subprocess.run(generateweasypdf, check=True)

except subprocess.CalledProcessError as e:
    print(f"Error running script2.py: {e}")
