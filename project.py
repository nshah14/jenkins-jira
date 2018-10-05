import os
import subprocess
import sys

def main():
    os.environ['PATH_TO_ARTIFCT'] = "my_path"
    print os.environ.get('PATH_TO_ARTIFCT')

if __name__ == '__main__':
	main()