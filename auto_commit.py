import subprocess
import datetime
#https://blog.csdn.net/u010429424/article/details/76896918
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "auto push at " + str(datetime.datetime.now())])
subprocess.call(["git", "push"])