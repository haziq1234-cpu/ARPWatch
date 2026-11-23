import argparse

def load_allowlist(filename):
    trusted = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                parts = line.split()

                if len(parts) == 2:
                    ip, mac = parts
                    trusted[ip] = mac.upper()

        print(f"[INFO] Loaded {len(trusted)} trusted entries")
        return trusted

    except FileNotFoundError:
        print("[INFO] Allowlist file not found")
        return trusted


def main():
    parser = argparse.ArgumentParser(description="ARPWatch configuration demo")

    parser.add_argument("--interface", default="eth0")
    parser.add_argument("--threshold", type=int, default=5)
    parser.add_argument("--allowlist", default="allowlist.txt")

    args = parser.parse_args()

    print("Interface:", args.interface)
    print("Threshold:", args.threshold)

    trusted = load_allowlist(args.allowlist)
    print("Trusted devices:", trusted)


if __name__ == "__main__":
    main()
