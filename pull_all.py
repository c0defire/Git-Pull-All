import os
import subprocess

# 🎯 Folders to scan for Git repos
base_dirs = [
    "C:/Users/[xxx]",
    "C:/Users/[xxx]/[xxx]/"
]

# 🎨 Color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

for base_dir in base_dirs:
    print(f"\n{YELLOW}=== Checking repos in: {base_dir} ==={RESET}")

    if not os.path.isdir(base_dir):
        print(f"{RED}✖ Path does not exist: {base_dir}{RESET}")
        continue

    for folder in os.listdir(base_dir):
        repo_path = os.path.join(base_dir, folder)

        # Check if folder contains a .git directory
        if os.path.isdir(os.path.join(repo_path, ".git")):
            print(f"\n{YELLOW}Checking {folder}...{RESET}")

            result = subprocess.run(
                ["git", "-C", repo_path, "pull"],
                capture_output=True,
                text=True
            )

            output = (result.stdout + result.stderr).strip()

            if "Already up to date" in output or "Already up-to-date" in output:
                print(f"{GREEN}✔ {folder} is already up to date.{RESET}")

            elif "Updating" in output or "Fast-forward" in output:
                print(f"{YELLOW}🔄 {folder} updated successfully!{RESET}")
                print(output)

            elif result.returncode != 0:
                print(f"{RED}✖ Error updating {folder}:{RESET}")
                print(output)

            else:
                print(output)
