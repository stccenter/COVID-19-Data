import subprocess
import datetime
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "auto push at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
subprocess.call(["git", "push"])
