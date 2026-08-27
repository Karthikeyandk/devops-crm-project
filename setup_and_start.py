import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent


def print_step(message: str) -> None:
    print(f"\n{'=' * 60}")
    print(message)
    print('=' * 60)


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def run_command(command: list[str], wait: bool = True) -> subprocess.Popen | None:
    print(f"\n> {' '.join(command)}")

    # Yarn is provided through Corepack on Windows.
    # Execute it through cmd.exe so it works reliably from MSYS2 + Python.
    if os.name == "nt" and command[0] == "yarn":
        command = ["cmd.exe", "/c", *command]

    if wait:
        result = subprocess.run(command, cwd=PROJECT_DIR)
        if result.returncode != 0:
            print(
                f"Command failed with exit code {result.returncode}: "
                f"{' '.join(command)}"
            )
            sys.exit(result.returncode)
        return None

    return subprocess.Popen(command, cwd=PROJECT_DIR)


def setup_environment() -> None:
    print_step("Checking required tools")

    # Support the MSYS2 UCRT64 environment used on Windows.
    os.environ["PATH"] = (
        r"C:\Program Files\nodejs;"
        r"C:\Program Files\Docker\Docker\resources\bin;"
        r"C:\Program Files\Git\cmd;"
        + os.environ.get("PATH", "")
    )

    required_tools = {
        "node": "Node.js",
        "yarn": "Yarn",
        "docker": "Docker",
        "git": "Git",
    }

    for command, name in required_tools.items():
        if not command_exists(command):
            print(f"ERROR: {name} was not found in PATH.")
            sys.exit(1)
        print(f"✓ {name} found")


def install_dependencies() -> None:
    print_step("Installing project dependencies")
    run_command(["yarn", "install"])


def start_twenty_server() -> None:
    print_step("Starting Twenty local server")

    run_command(["yarn", "twenty", "docker:start"])

    # Give the local server a little time to become reachable.
    print("\nWaiting for Twenty server...")
    time.sleep(3)


def start_development_mode() -> None:
    print_step("Starting Twenty development mode")

    # This command intentionally stays attached because
    # `yarn twenty dev` continuously watches for source changes.
    print("\nThe development server will remain running.")
    print("Press Ctrl+C to stop it.\n")

    run_command(["yarn", "twenty", "dev"])


def main() -> None:
    print_step("DevOps CRM - Local Setup Automation")

    setup_environment()
    install_dependencies()
    start_twenty_server()
    start_development_mode()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDevelopment process stopped by user.")
        sys.exit(0)
