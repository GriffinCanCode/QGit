#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def run_gpg_setup():
    """Run the GPG setup script."""
    # Get the path to the setup script
    script_dir = Path(__file__).parent
    setup_script = script_dir / "setup_gpg.sh"
    
    # Ensure the script is executable
    os.chmod(setup_script, 0o755)
    
    # Run the script
    try:
        subprocess.run([str(setup_script)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running GPG setup: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main entry point for the qgit makegpg command."""
    run_gpg_setup()

if __name__ == "__main__":
    main() 