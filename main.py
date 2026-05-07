import os, sys, json

def main():
    x = 10
    print("This line is intentionally made very long to trigger the line-too-long rule. " * 5)
    y = 20
    print(y)

if __name__ == "__main__":
    main()