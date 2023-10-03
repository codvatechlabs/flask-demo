import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python your_program.py arg1 arg2 arg3")
        sys.exit(1)

    arg1 = float(sys.argv[1])
    arg2 = float(sys.argv[2])
    arg3 = float(sys.argv[3])

    result = arg1 + arg2 + arg3
    print(f"The result is: {result}")
