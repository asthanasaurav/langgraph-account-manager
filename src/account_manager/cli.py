import argparse
import json
from .graph import ACCOUNTS, build_graph

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--account", choices=sorted(ACCOUNTS), default="Example-Telecom")
    args = p.parse_args()
    print(json.dumps(build_graph().invoke({"account": args.account}), indent=2))

if __name__ == "__main__":
    main()
