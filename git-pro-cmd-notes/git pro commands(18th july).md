
## Git Branching and Commit Workflow

```bash
git checkout -b main
```
Created the `main` branch as the production branch.

```bash
git checkout -b develop
```
Created the `develop` branch for ongoing development.

```bash
git checkout -b feature/login
```
Created a `feature/login` branch for login functionality.

```bash
git add . && git commit -m 'Add login feature'
```
Staged and committed changes to the feature branch.

```bash
git checkout develop
git merge feature/login
```
Merged the login feature into the develop branch.

```bash
git checkout main
echo 'Quick Fix' > fix.txt
git add . && git commit -m 'Hotfix on trunk'
```
Switched to `main` and committed a hotfix (trunk-based workflow).

---

## Git Rebase and Merge Examples

```bash
git checkout -b feature/rebase
echo 'Line A' > a.txt
git add . && git commit -m 'A'
```
Created a new feature branch and committed changes.

```bash
git checkout main
echo 'Line B' > b.txt
git add . && git commit -m 'B'
```
Made and committed base changes in `main`.

```bash
git checkout feature/rebase
git rebase main
```
Rebased the feature branch onto the updated `main`.

**Note:** Faced an issue during rebase due to forgetting to add and commit new files in `main`, which unintentionally reflected in another branch. Learned that `git add` and `git commit` are mandatory before switching branches to avoid such issues.

---

## Git Merge and Conflict Resolution

```bash
git checkout -b feature/merge
echo 'Line C' > c.txt
git add . && git commit -m 'C'
git merge main
```
Demonstrated a non-linear merge from `main`.

```bash
git checkout -b conflict-branch
echo 'First Edit' > conflict.txt
git add . && git commit -m 'Edit in branch'

git checkout main
echo 'Second Edit' > conflict.txt
git add . && git commit -m 'Edit in main'
```
Created a manual conflict.

```bash
git checkout conflict-branch
git merge main
```
Conflict triggered and resolved using:

```bash
git add conflict.txt
git commit -m 'Resolved merge conflict'
```

---

## Remote Repository Management

```bash
git clone https://github.com/yourname/test.git
cd test
git pull origin main
git fetch origin
git push origin main
```

---

## Branch Deletion and File Management

```bash
git branch -d branch_name
git branch -D branch_name
git push origin --delete branch_name
```

---

## File Recovery and Shell Utilities

```bash
rmdir github2003         # Failed - directory not empty
rm -rf github2003        # Forced deletion
cat ~/.zsh_history       # Show terminal command history

git checkout HEAD -- path/to/filename
git restore path/to/filename
```

---

## Trash and File Listing

```bash
ls -la ~/.Trash
```
Attempted to list deleted files, but faced permission issues.changed it by giving full access to terminal.

---