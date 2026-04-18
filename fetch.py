import requests
import polars as pl
import json
from pathlib import Path
from datetime import datetime

today = datetime.today()


def get_tvmaze_schedule_full():
    filename = "tvmaze_schedule.json"

    if not Path(filename).exists():
        print("Downloading data from tvmaze...")
        url = "https://api.tvmaze.com/schedule/full"
        response = requests.get(url)
        data = response.json()

        with open(filename, "w") as f:
            json.dump(data, f)


def get_tvmaze_schedule():
    results = []

    filepath = Path("tvmaze_schedule.json")
    with filepath.open("r") as f:
         data = json.load(f)

    for item in data:
        airdate = item.get("airdate")
        if not airdate:
            continue

        airdate_dt = datetime.strptime(airdate, "%Y-%m-%d")

        if today <= airdate_dt:
            platform = []
            if item.get("_embedded", {}).get("show", {}).get("network") is not None:
                platform.append(
                    item.get("_embedded", {}).get("show", {}).get("network", {}).get("name")
                )

            if item.get("_embedded", {}).get("show", {}).get("webChannel") is not None:
                platform.append(
                    item.get("_embedded", {}).get("show", {}).get("webChannel", {}).get("name")
                )
            
            results.append({
                "type": "TV",
                "title": item.get("_embedded").get("show", {"name": None})["name"],
                "episode": item.get("name"),
                "season": item.get("season"),
                "number": item.get("number"),
                "date": airdate,
                "platform": ",".join(platform)
            })
            #break
    return results


def build_dataset():
    get_tvmaze_schedule_full()
    tv_data = get_tvmaze_schedule()
    df = pl.DataFrame(tv_data)
    df = df.sort("date")

    return df


def export_data(df):
    df.write_csv("tv_releases.csv")
    print("File generated")


if __name__ == "__main__":
    df = build_dataset()
    export_data(df)
