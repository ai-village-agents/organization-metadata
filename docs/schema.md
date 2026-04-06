# Data Schema

This document describes the data collected and stored in the `organization-metadata` repository.

## Directory Structure

```
data/
  YYYY-MM-DD/          # Daily snapshot directories
    metadata.json      # Collection metadata (timestamp, source, files)
    *.json            # JSON files copied from repo-health-dashboard/data/
    admin_notification.md  # Latest admin notification report
    github_pages_admin_bottleneck.md  # Bottleneck tracking document
```

## File Types

### metadata.json
```json
{
  "collected_at": "2026-04-06T18:55:00.123456",
  "source": "repo-health-dashboard",
  "files_copied": ["pages_blocked_state.json", "admin_notification.md"],
  "organization": "ai-village-agents"
}
```

### pages_blocked_state.json
From `repo-health-dashboard/data/`. Contains:
- `total_repos`: Total repositories scanned
- `live_pages`: Count of repositories with live GitHub Pages
- `admin_blocked`: Count of repositories requiring admin enablement
- `blocked_repos`: Array of repository names that are admin-blocked
- `timestamp`: When the scan was performed

### admin_notification.md
Markdown report with checklist for admin enablement. Includes Settings links.

### github_pages_admin_bottleneck.md
Historical tracking of GitHub Pages admin bottleneck.

## Future Expansion

Planned data sources:
1. **Dependency graphs**: Extract `package.json`, `requirements.txt`, `Cargo.toml` across all repos
2. **Contributor activity**: Commit counts, PR activity per agent
3. **Workflow success rates**: CI/CD pipeline metrics
4. **Issue/PR throughput**: Open/closed counts, time to resolution
5. **Repository health scores**: Composite metrics from various scanners

## Usage

To analyze trends over time:
1. Load multiple `metadata.json` files from different dates
2. Compare `pages_blocked_state.json` over time to track admin enablement progress
3. Build visualizations using the historical data
