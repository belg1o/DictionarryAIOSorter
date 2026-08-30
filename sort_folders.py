import json
import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/Redhair777/AIO-Quality-Profiles/main/profiles/2160p-quality.expressions.json"
OUTPUT_FILE = "2160p-quality.expressions.sorted.json"


def main():
    with urllib.request.urlopen(SOURCE_URL) as response:
        data = json.load(response)

    # Highest score first.
    # Python's sort is stable, so items with equal scores
    # retain their original order.
    data.sort(key=lambda x: x.get("score", 0), reverse=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Sorted {len(data)} expressions.")
    print(f"Highest score: {data[0].get('score')}")
    print(f"Lowest score:  {data[-1].get('score')}")


if __name__ == "__main__":
    main()