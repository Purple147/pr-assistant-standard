# pr-assistant-standard/check_pr.py
import os, json, re
from github import Github

event_path = os.environ.get("GITHUB_EVENT_PATH", "/github/workflow/event.json")
with open(event_path, "r", encoding="utf-8") as f:
    event = json.load(f)

pr = event.get("pull_request") or {}
if not pr:
    print("No pull_request in event payload. Exiting.")
    exit(0)

repo_name = event["repository"]["full_name"]
pr_number = pr["number"]

token = os.environ.get("GITHUB_TOKEN")
if not token:
    print("GITHUB_TOKEN not set. Exiting")
    exit(1)

g = Github(token)
repo = g.get_repo(repo_name)
pull = repo.get_pull(pr_number)

files = list(pull.get_files())
todo_files, debug_files, large_files = [], [], []

for f in files:
    filename = f.filename
    patch = f.patch or ""
    if re.search(r'\bTODO\b', patch):
        todo_files.append(filename)
    if re.search(r'\bprint\s*\(|console\.log\s*\(', patch):
        debug_files.append(filename)
    added_lines = sum(1 for line in patch.splitlines() if line.startswith('+') and not line.startswith('+++'))
    if added_lines > 300:
        large_files.append((filename, added_lines))

lines = ["## ✅ PR Quick Check Report", ""]
if not (todo_files or debug_files or large_files):
    lines.append("No quick issues found by the basic checks.")
else:
    if todo_files:
        lines.append("### 🔴 TODO found in:")
        for fn in todo_files: lines.append(f"- `{fn}`")
    if debug_files:
        lines.append("### 🐞 Debug statements found in:")
        for fn in debug_files: lines.append(f"- `{fn}`")
    if large_files:
        lines.append("### 📚 Large added code (approx added lines):")
        for fn, ln in large_files: lines.append(f"- `{fn}` — ~{ln} added lines")
    lines.append("")
    lines.append("> This is an automated quick-check. For deeper analysis, use the full analyzer.")

comment_body = "\n".join(lines)
print("Posting comment to PR:", pr_number)
pull.create_issue_comment(comment_body)
print("Comment posted.")
