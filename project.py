import os
import subprocess
import sys

def main():
    os.environ['PATH_TO_ARTIFCT'] = "itms-services://?action=download-manifest&url=https%3A%2F%2Fapp-store.king.com%2Fplist%3Ftoken%3D4a1447be-99bc-406a-9473-765c1abce09d"
    print os.environ.get('PATH_TO_ARTIFCT')

if __name__ == '__main__':
	main()