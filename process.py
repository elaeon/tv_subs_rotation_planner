from pathlib import Path
import polars as pl


SYSTEM_PROMPT = """---
name: TvShow Agent
description: "Elaborate a plan to generate a subscription rotation plan. Use when: user types 'tvshow_plan'"
---

# Plan
Elaborate a susbscription rotation plan for this year. 
I don't want to hold one susbscription service more than two months, 
so elaborate it knowing that I could bind watch every TV show on the list. 
The TV shows I want to watch are in the table TV SHOWS.
If you find gaps between shows, use one of this services to fill them:
Netflix, HBO, Apple Tv.
The output file should be named rotation_plan_{year}.md
with a table with every month of the year next to
the subscription service name and the reason. Also if two o more
tv shows are in the same month choose the priority list above and
move the stream service to the next month. 
"""

def to_md(filename: str, titles_list: list[str]):
    data_path = Path(filename)
    print(f"Processing {data_path}...")
    
    # Process each sheet and column configuration
    md_file = [SYSTEM_PROMPT]
    columns = ["title", "season", "number", "date", "platform"]
    df = pl.read_csv(
        data_path,
        columns=columns
    )
    df_list = []
    for title in titles_list:
        df_list.append(
            df.filter(
                pl.col("title").str.contains(f"(?i){title}")
            )
        )
    df = pl.concat(df_list)
    
    tv_shows_md = table_md(df, "TV SHOWS", columns)
    md_file.extend(tv_shows_md)
    return "\n".join(md_file)


def table_md(df: pl.DataFrame, section_name, columns):
    md = []

    # --- Title ---
    md.append(f"## {section_name}")
    md.append("")
    md.append("| " + " | ".join(columns) + " |")
    md.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for row in df.iter_rows(named=True):
        row_list = []
        for column in columns:
            row_list.append(f"{row[column]}")
        md.append("|" + "|".join(row_list) + "|")
    md.append("")
    return md


def read_titles_list() -> list[str]:
    filepath = Path("titles.txt")
    titles_list = []
    with filepath.open("r") as f:
        for line in f.readlines():
            titles_list.append(line.replace("\n", ""))
    return titles_list


if __name__ == "__main__":
    titles_list = read_titles_list()
    text_md = to_md("tv_releases.csv", titles_list)
    with open("AGENTS.md", "w") as f:
        f.write(text_md)
