import os
import sys

def get_current_branch():
    try:
        # Run git command to get the current branch
        command = "git ls-remote origin HEAD | awk '{print $1}'"
        current_branch = os.popen(command).read().strip()
        print(current_branch)
        return current_branch
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_base_branch():
    try:
        # Run git command to get the base branch
        command = "git ls-remote origin main | awk '{print $1}'"
        base_branch = os.popen(command).read().strip()
        print(base_branch)
        return base_branch
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def count_changed_files(base_branch):
    try:
        # Run git command to get the list of changed files
        command = f"git diff --name-only {base_branch}"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        changed_files = result.stdout.splitlines()

        # Count the number of changed files
        file_count = len(changed_files)
        return file_count
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    try:
        # Get base commit, current commit, and base branch from command line arguments
        base_branch = get_base_branch()
        print(base_branch)
        current_branch = get_current_branch()
        print(current_branch)
        # Count changed files
        file_count = count_changed_files(base_branch)

        print(f"Number of changed files: {file_count}")

        # Check if the count exceeds 20
        if file_count > 20:
            print("Error: Too many files (greater than 20) changed in the pull request.")
            print("Possible issues:")
            print("- Contributor may be merging into an incorrect branch.")
            print("- Source branch may be incorrect.")
            sys.exit(1)

    except IndexError:
        print("Error: Please provide base commit, current commit, and base branch as command line arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()
