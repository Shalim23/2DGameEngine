import subprocess
import argparse
import os

CONFIGURATIONS = "Debug;MinSizeRel;DebugEditor"

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--open", action="store_true", help="Open solution")
args = parser.parse_args()

os.chdir("Deps")

subprocess.check_call(["python", "build_deps.py"])

os.chdir("..")

subprocess.check_call(["cmake",
    f"-DCMAKE_CONFIGURATION_TYPES={CONFIGURATIONS}", "-S", ".", "-B", "./bin"])

if args.open:
    subprocess.Popen(["start", "bin/2DGameEngineDemo.sln"], shell=True)
