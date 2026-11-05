"""Strip non-public metadata from generated GameChanger stats data.

Raw CSVs stay in stats-input (NOT published). Output contains approved
player names, SNL team labels and batting numbers only.
"""
import json
from pathlib import Path

PUBLIC_STATS = {"GP", "PA", "AVG", "OBP", "SLG", "OPS", "H", "2B", "3B", "HR", "RBI", "QAB"}
INPUT = Path("public/stats-data.json")

def main():
    raw = json.loads(INPUT.read_text(encoding="utf-8"))
    seasons = []
    for s in raw["seasons"]:
        teams = [{
            "team_id": t["team_id"],
            "name": t["name"],
            "reporting_status": t["reporting_status"],
            "players_with_batting_stats": t["players_with_batting_stats"],
        } for t in s["teams"]]
        players = [{
            "name": p["name"],
            "team_id": p["team_id"],
            "team": p["team"],
            "stats": {k: v for k, v in p["stats"].items() if k in PUBLIC_STATS},
        } for p in s["players"]]
        seasons.append({
            "season_id": s["season_id"],
            "season_label": s["season_label"],
            "teams": teams,
            "player_count": len(players),
            "reporting_team_count": s["reporting_team_count"],
            "players": players,
        })
    published = {
        "generated_at_utc": raw["generated_at_utc"],
        "current_season": raw["current_season"],
        "notice": raw["notice"],
        "seasons": seasons,
    }
    INPUT.write_text(json.dumps(published, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared safe public batting data for {len(seasons)} SNL session(s).")

if __name__ == "__main__":
    main()
