"""Fortune Cookie Wisdom for Developers — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one original fortune-cookie line for a software developer, 120 characters or fewer.
"""
import os

LINE = "Your next bug is already in production, patiently waiting for you to notice it on a Friday afternoon."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
