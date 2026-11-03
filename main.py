import argparse
import subprocess
import socket
import os
import time
import random

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)