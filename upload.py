# made by medu :3 
import os
import re
import time
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

# create a .env file and put DISCORD_TOKEN=ur bot token here
# for it to work :D
TOKEN = os.getenv("DISCORD_TOKEN") or os.getenv("BOT_TOKEN")
if not TOKEN:
    raise SystemExit("No bot token found.")

EMOJI_DIR = "emojis"
API = "https://discord.com/api/v10"
HEADERS = {"Authorization": f"Bot {TOKEN}"}


def app_id():
    r = requests.get(f"{API}/oauth2/applications/@me", headers=HEADERS)
    r.raise_for_status()
    return r.json()["id"]


def sanitize_name(filename):
    name = os.path.splitext(filename)[0]
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")

    if len(name) < 2:
        name = f"e_{name}"

    return name[:32]


def main():
    if not os.path.isdir(EMOJI_DIR):
        raise SystemExit(f"Folder '{EMOJI_DIR}' not found.")

    aid = app_id()

    r = requests.get(
        f"{API}/applications/{aid}/emojis",
        headers=HEADERS
    )
    r.raise_for_status()

    existing = {e["name"]: e["id"] for e in r.json().get("items", [])}
    results = dict(existing)

    for fname in sorted(os.listdir(EMOJI_DIR)):
        if not fname.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            continue

        name = sanitize_name(fname)

        if name in existing:
            print(f"skip: {name}")
            continue

        path = os.path.join(EMOJI_DIR, fname)

        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()

        if fname.lower().endswith(".png"):
            ext = "png"
        elif fname.lower().endswith(".gif"):
            ext = "gif"
        else:
            ext = "jpeg"

        payload = {
            "name": name,
            "image": f"data:image/{ext};base64,{b64}"
        }

        r = requests.post(
            f"{API}/applications/{aid}/emojis",
            headers=HEADERS,
            json=payload
        )

        if r.status_code == 201:
            eid = r.json()["id"]
            results[name] = eid
            print(f"uploaded: {name} -> {eid}")
        else:
            print(f"failed: {name} -> {r.status_code}")

        time.sleep(1.5)  # im the 67 demon

    print("\nEMOJIS = {")
    for name, eid in sorted(results.items()):
        print(f'    "{name}": "<:{name}:{eid}>",')
    print("}")


if __name__ == "__main__":
    main()
