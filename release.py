import argparse
from loader import load_config

def parse_arguments():
    parser = argparse.ArgumentParser(description="Config Loader")
    parser.add_argument(
        '--drymode', 
        action='store_true', 
        help='Enable dry run mode (currently has no effect)'
    )
    return parser.parse_args()

def main():
    args = parse_arguments()
    config = load_config("data.yml")

    if args.drymode:
        print("Dry mode is enabled. No actions will be performed.")
    
    print(f"Branch: {config.release_branch}")
    print(f"DevKit: {config.devkit_version}")

    app = config.get_app_by_name("beamformer")
    if app:
        print(f"{app.name}: {app.url} @ {app.commit}")
    else:
        print("App nicht gefunden.")

if __name__ == "__main__":
    main()
