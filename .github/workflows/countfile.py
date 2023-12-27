import os
import sys

def count_files(directory='.'):
    file_count = sum(len(files) for _, _, files in os.walk(directory))
    return file_count

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    file_count = count_files(directory)

    print(f"File count: {file_count}")

    if file_count > 20:
        print("Error: Too many files (greater than 20) in the pull request.")
        print("Possible issues:")
        print("- You may be merging into an incorrect branch.")
        print("- Source branch may be incorrect.")
        sys.exit(1)

if __name__ == "__main__":
    main()
