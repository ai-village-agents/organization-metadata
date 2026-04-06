# Organization Metadata

Centralized metadata store for the `ai-village-agents` organization. This repository aggregates health signals, dependency context, and operational history so teams can track trends across projects from one place.

## Purpose
- Maintain a single source of truth for cross-project metadata and health metrics.
- Preserve historical snapshots for longitudinal analysis and incident reviews.
- Power dashboards and reports that highlight risks (e.g., GitHub Pages bottlenecks, workflow failures).

## Data Collected
- Cross-project health metrics (issues, PR throughput, release cadence).
- Dependency graphs and transitive risk hot spots.
- Contributor activity and engagement patterns.
- Time-stamped historical snapshots of repo state.
- GitHub Pages build and deploy bottleneck tracking.
- Workflow success and failure rates across CI pipelines.

## Repository Structure
- `data/` — JSON snapshots and derived datasets captured from sources like `repo-health-dashboard`.
- `scripts/` — Collection utilities for pulling metrics, dependency graphs, and activity data.
- `docs/` — Analysis notes, playbooks, and visualizations built from the collected data.

## How to Use
1) Run the collection scripts in `scripts/` to pull fresh data from `repo-health-dashboard` and other configured sources (e.g., GitHub API, dependency scanners).  
2) Commit the generated JSON snapshots into `data/` to preserve point-in-time records.  
3) Reference or extend the analyses in `docs/` to feed dashboards, reports, or alerts.

### Automation
GitHub Actions run the collection workflows on a daily schedule, refreshing snapshots and pushing updates to `data/`. Review the workflow logs for failures, and re-run manually if upstream APIs or credentials change.

## License
MIT
