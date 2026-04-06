#!/usr/bin/env python3
"""
Collect metadata from repo-health-dashboard and other sources.
"""

import json
import os
import sys
import datetime
import shutil
from pathlib import Path

def main():
    # Configuration
    base_dir = Path(__file__).parent.parent
    source_dashboard = Path.home() / "repo-health-dashboard"
    target_data = base_dir / "data"
    
    # Create timestamped directory
    today = datetime.date.today().isoformat()
    target_dir = target_data / today
    target_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Collecting metadata for {today}")
    print(f"Source: {source_dashboard}")
    print(f"Target: {target_dir}")
    
    # Copy JSON files from repo-health-dashboard/data
    source_data = source_dashboard / "data"
    if source_data.exists():
        for json_file in source_data.glob("*.json"):
            target_file = target_dir / json_file.name
            shutil.copy2(json_file, target_file)
            print(f"  Copied: {json_file.name}")
    else:
        print(f"Warning: Source data directory not found: {source_data}")
    
    # Copy admin notification JSON if exists
    admin_notification = source_dashboard / "docs" / "admin_notification.md"
    if admin_notification.exists():
        target_notification = target_dir / "admin_notification.md"
        shutil.copy2(admin_notification, target_notification)
        print(f"  Copied: admin_notification.md")
    
    # Copy bottleneck tracking if exists
    bottleneck_file = source_dashboard / "docs" / "github_pages_admin_bottleneck.md"
    if bottleneck_file.exists():
        target_bottleneck = target_dir / "github_pages_admin_bottleneck.md"
        shutil.copy2(bottleneck_file, target_bottleneck)
        print(f"  Copied: github_pages_admin_bottleneck.md")
    
    # Create metadata.json with collection info
    metadata = {
        "collected_at": datetime.datetime.now().isoformat(),
        "source": "repo-health-dashboard",
        "files_copied": [f.name for f in target_dir.glob("*") if f.is_file()],
        "organization": "ai-village-agents"
    }
    
    metadata_file = target_dir / "metadata.json"
    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Metadata collection complete: {len(metadata['files_copied'])} files")
    print(f"Metadata saved to: {metadata_file}")

if __name__ == "__main__":
    main()
