# TV Subscription Rotation Planner 📺

A smart planning tool that generates an optimal subscription rotation schedule for watching your favorite TV shows throughout the year, while maintaining the constraint that no streaming service is held for more than two consecutive months.

## Problem

Streaming subscriptions are expensive. Managing multiple active subscriptions simultaneously can quickly become costly. This tool helps you:

- **Save costs** by rotating subscriptions instead of maintaining multiple active at once
- **Never miss shows** by ensuring you have the right service at the right time
- **Optimize scheduling** by identifying gaps and filling them with one-time content

## Solution

The TV Subscription Rotation Planner creates a month-by-month rotation schedule that ensures:

1. ✅ You have access to every TV show on your watchlist when it airs
2. ✅ No subscription service is active for more than 2 consecutive months
3. ✅ Gaps are filled with content from Netflix, HBO, or Apple TV
4. ✅ When multiple shows overlap, services are prioritized and shifted accordingly

## Features

- 📋 **Monthly schedule** - Clear month-by-month breakdown of which service to use
- 📊 **Show tracking** - Organized view of all shows with platforms and air dates
- 🎯 **Smart prioritization** - Handles conflicts when multiple shows air in the same month
- 💼 **Gap filling** - Suggests filler services (Netflix, HBO, Apple TV) for months without shows
- 📄 **Professional output** - Generates `rotation_plan_{year}.md` with formatted tables and explanations

## Input Format

Favorite TV Shows to watch are in titles.txt.

## Output

The planner generates `rotation_plan_{year}.md` containing:

- A month-by-month table showing:
  - Month name
  - Recommended subscription service
  - Reason (show name or "Filler content")
- Show breakdown by month
- Cost optimization notes
- Recommended action dates


## Constraints

- **2-Month Maximum**: No subscription service should be held for more than 2 consecutive months
- **Complete Coverage**: Must have access to all TV shows on the watchlist
- **Priority Order**: Netflix → HBO → Apple TV (for filling gaps)

## Installation & Setup

```bash
# Install dependencies
uv sync

# Run to download tv shows releases from tvmaze.
uv run python fetch.py

# Run to generate AGENTS.md
uv run python process.py
```

## Usage
Write tvshow_plan in your code agent.

**Review** `rotation_plan_2026.md` for your personalized plan


## How It Works

1. **Analyze** all TV shows and their air dates
2. **Identify** required platforms and date ranges
3. **Build** monthly schedule respecting 2-month constraints
4. **Fill gaps** with recommended services
5. **Resolve conflicts** using priority order
6. **Generate** formatted markdown output


## Next Year

This tool can be easily adapted for subsequent years:
1. Update the TV shows table with new titles and dates
2. Re-run the planner
3. Generate `rotation_plan_{new_year}.md`

---

**Current Plan**: [rotation_plan_2026.md](rotation_plan_2026.md)

**Last Updated**: April 17, 2026
