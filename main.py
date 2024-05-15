import sys

def main():
    print("Hello World! From Python: " + str(sys.version_info))
    if sys.version_info >= (3, 10) and sys.version_info < (3, 11):
        # let's make this script fail for Python 3.9
        raise Exception('Python version 3.10.x is unsupported!')

if __name__ == "__main__":
    main()