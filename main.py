import os, sys, json   # F401 + import sorting issues

def main():
    x = 10      # F841: unused variable
    print("This line is intentionally made very long to trigger the line-too-long rule. It goes on and on and on and on and on and on and on and on and on." * 2)
    
    y = 20
    print(y)

if __name__ == "__main__":
    main()