import json
import subprocess
import sys


def oath_list(filter_str):
    res = subprocess.run(["ykman", "oath", "list"], capture_output=True)
    stdout = res.stdout.decode()

    json_data = {"items": []}
    for account in stdout.strip().split("\n"):
        if filter_str and filter_str.lower() not in account.lower():
            continue

        json_data["items"].append(
            {
                "title": account,
                "arg": account
            }
        )
    return json.dumps(json_data)


if __name__ == "__main__":
    filter_str = sys.argv[1] if len(sys.argv) > 1 else None
    print(oath_list(filter_str))
