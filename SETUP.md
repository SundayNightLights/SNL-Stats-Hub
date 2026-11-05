# Sunday Night Lights — Stats Hub

Independent GameChanger batting statistics site for SNL.
**This repository is separate from `SNL-Calendar-Hub`.** Do not replace your calendar workflow with this one.

## One-time setup

### 1. Upload the entire project in one GitHub commit

1. Unzip `SNL-Stats-Hub-Complete.zip` on your computer.
2. Open the extracted **SNL-Stats-Hub-Upload** folder.
3. Go to https://github.com/SundayNightLights/SNL-Stats-Hub and choose **Add file → Upload files**.
4. **Drag the contents of the extracted folder** (including `.github`, `scripts`, `index.html`, and `stats.html`) onto GitHub. Do **not** upload the ZIP as a single file, and do **not** drag the parent folder or everything will be nested one level too deep.
5. Confirm the upload has `.github/workflows/sync-stats.yml` and `scripts/download_stats.py` at those exact paths. Commit to `main`.

### 2. Add OneDrive authentication to this new repository

The Calendar Hub's two GitHub Action secrets **are NOT automatically available** to this new repository. Go to **SNL-Stats-Hub → Settings → Secrets and variables → Actions** and configure:

- `MS_CLIENT_ID` — the Microsoft application/client ID already used by the Calendar Hub.
- `MSAL_CACHE` — a serialized Microsoft authentication cache containing permission to read the OneDrive account.

**Do not put either secret into repository files, README, a public chat, or a CSV.** GitHub does not show existing secret values after they have been saved. If you don't have a safe copy, you'll need to recreate the token cache through Microsoft login. We can do that separately. Until both secrets are configured, the workflow will fail at the OneDrive download step; the code upload is still fine.

### 3. Enable GitHub Pages

Choose **Settings → Pages → Build and deployment → Source: GitHub Actions**.
Then go to **Actions → Sync SNL Batting Statistics → Run workflow**.
Once successful, the public website will be:

https://sundaynightlights.github.io/SNL-Stats-Hub/

## Weekly routine (your only recurring steps)

- Download the league-wide GameChanger Leaders CSV.
- Save it in OneDrive under `/SNL/SNL Stats/` with its current session filename, e.g. `F26 Stats.csv`.
- Replace **only that session's** file on subsequent weeks.
- At the new session, **keep the old file**, and start a new one such as `W27 Stats.csv`.

The workflow checks OneDrive every two hours and rebuilds the Stats Hub from **all** season files every run. Older seasons remain in OneDrive. GitHub does not delete the old season's stats when a newer CSV is exported.

## What appears publicly

- Player names and teams for participating teams only, with available batting statistics.
- All six team reporting statuses; missing teams display **Not submitted**.
- Season selector for `F26`, `W27`, `F27`, and future seasons.
- No pitching or fielding statistics.
- No raw GameChanger exports, jersey numbers, Microsoft credentials, or audit files in the site artifact.

All-time *career* batting statistics need verified player identifiers across seasons. We have deliberately **not** claimed to merge same-name players automatically, since players can change teams or share names.

## Files

```text
.github/workflows/sync-stats.yml     GitHub workflow, independent of calendars
scripts/download_stats.py            OneDrive season CSV downloader
scripts/generate_stats_data.py       Multi-season batting data processor
scripts/prepare_public_stats.py      Limits public output to approved fields
index.html                            Stats Hub landing page
stats.html                            Alternate direct link to leaderboard
SETUP.md                              Setup and maintenance instructions
```

### If something fails

- `No Microsoft account found in token cache`: the `MSAL_CACHE` secret was missing or stale.
- `No season CSV files found`: check `/SNL/SNL Stats/F26 Stats.csv` and filename spelling.
- `Failed to load stats-data.json`: the Pages deployment failed, or the JSON file was not generated.
- `No season statistics`: verify that the GameChanger report has at least one player row.

The new Stats Hub does **not** modify the existing calendar subscription pages or the Master workbook.
