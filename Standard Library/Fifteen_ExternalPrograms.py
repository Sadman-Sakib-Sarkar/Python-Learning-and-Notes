import subprocess

completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("args:", completed.args)
print("retruncode:", completed.returncode)
print("stderr:", completed.stderr)
print("stdout:", completed.stdout) #captue output=true -> output come from stdout. text=true -> removes binary format




#we can create any other child process too:
# completed = subprocess.run(["Python3", "other.py"], capture_output=True, text=True)
# print("args:", completed.args)
# print("retruncode:", completed.returncode)
# print("stderr:", completed.stderr)
# print("stdout:", completed.stdout)