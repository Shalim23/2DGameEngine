import subprocess

subprocess.check_call(["cmake", "-S", ".", "-B", "./bin"])
subprocess.check_call(["cmake", "--build", "bin", "--config", "Release"])
