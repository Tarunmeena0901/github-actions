import os
import sys

def count_changed_files(base_commit, current_commit):
    try:
        # Run git command to get the list of changed files
        command = f"git diff --name-only {base_commit} {current_commit}"
        changed_files = os.popen(command).read().splitlines()

        # Count the number of changed files
        file_count = len(changed_files)
        return file_count
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    try:
        # Get base and current commit from command line arguments
        base_commit = sys.argv[1]
        current_commit = sys.argv[2]

        # Count changed files
        file_count = count_changed_files(base_commit, current_commit)

        print(f"Number of changed files: {file_count}")

        # Check if the count exceeds 20
        if file_count > 20:
            print("Error: Too many files (greater than 20) changed in the pull request.")
            print("Possible issues:")
            print("- Contributor may be merging into an incorrect branch.")
            print("- Source branch may be incorrect.")
            sys.exit(1)

    except IndexError:
        print("Error: Please provide base commit and current commit as command line arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()
