# Git Commands Reference

A comprehensive list of commonly used Git commands with their descriptions and examples.

---

## Configuration Commands

| Command | Description | Example |
|---------|-------------|---------|
| `git config --global user.name "Your Name"` | Set your global username for commits | `git config --global user.name "John Doe"` |
| `git config --global user.email "your@email.com"` | Set your global email for commits | `git config --global user.email "john@example.com"` |
| `git config --list` | List all Git configuration settings | `git config --list` |
| `git config --global core.editor "code"` | Set default code editor (VS Code) | `git config --global core.editor "code"` |

---

## Repository Commands

| Command | Description | Example |
|---------|-------------|---------|
| `git init` | Initialize a new Git repository in current directory | `git init` |
| `git clone <url>` | Clone a remote repository to local machine | `git clone https://github.com/user/repo.git` |
| `git status` | Show working tree status (modified, staged, untracked files) | `git status` |
| `git remote -v` | List all remote repositories with URLs | `git remote -v` |
| `git remote add origin <url>` | Add a remote repository | `git remote add origin https://github.com/user/repo.git` |
| `git remote remove <name>` | Remove a remote repository | `git remote remove origin` |

---

## Staging & Committing

| Command | Description | Example |
|---------|-------------|---------|
| `git add <file>` | Stage a specific file for commit | `git add index.html` |
| `git add .` | Stage all modified and new files | `git add .` |
| `git add -A` | Stage all files including deletions | `git add -A` |
| `git add -p` | Interactively stage portions of files | `git add -p` |
| `git commit -m "message"` | Commit staged changes with a message | `git commit -m "Add new feature"` |
| `git commit -am "message"` | Stage and commit modified files (not new files) | `git commit -am "Fix bug in login"` |
| `git commit --amend` | Modify the last commit (change message or add files) | `git commit --amend` |
| `git commit --amend --no-edit` | Amend last commit without changing message | `git commit --amend --no-edit` |

---

## Viewing History

| Command | Description | Example |
|---------|-------------|---------|
| `git log` | Show commit history | `git log` |
| `git log --oneline` | Show compact commit history (one line per commit) | `git log --oneline` |
| `git log --oneline -n` | Show last n commits compactly | `git log --oneline -5` |
| `git log --graph --oneline` | Show commit history with branch graph | `git log --graph --oneline` |
| `git log -p <file>` | Show commit history for a specific file with diffs | `git log -p style.css` |
| `git show <commit>` | Show details of a specific commit | `git show abc1234` |
| `git diff` | Show unstaged changes (working directory vs staging) | `git diff` |
| `git diff --staged` | Show staged changes (staging vs last commit) | `git diff --staged` |
| `git diff <branch1>..<branch2>` | Compare two branches | `git diff main..feature` |
| `git diff HEAD~1` | Show changes in the last commit | `git diff HEAD~1` |
| `git blame <file>` | Show who changed what in a file | `git blame app.js` |
| `git shortlog` | Show commit summary by author | `git shortlog` |

---

## Branching

| Command | Description | Example |
|---------|-------------|---------|
| `git branch` | List all local branches | `git branch` |
| `git branch -r` | List all remote branches | `git branch -r` |
| `git branch -a` | List all branches (local and remote) | `git branch -a` |
| `git branch <name>` | Create a new branch | `git branch feature-login` |
| `git branch -d <name>` | Delete a merged branch | `git branch -d old-feature` |
| `git branch -D <name>` | Force delete a branch | `git branch -D experiment` |
| `git branch -m <old> <new>` | Rename a branch | `git branch -m old-name new-name` |
| `git checkout <branch>` | Switch to a branch | `git checkout main` |
| `git checkout -b <branch>` | Create and switch to a new branch | `git checkout -b feature-api` |
| `git switch <branch>` | Switch to a branch (modern syntax) | `git switch main` |
| `git switch -c <branch>` | Create and switch to new branch (modern) | `git switch -c bugfix-login` |
| `git checkout -b <branch> <remote>/<branch>` | Create branch from remote | `git checkout -b dev origin/dev` |

---

## Merging & Rebasing

| Command | Description | Example |
|---------|-------------|---------|
| `git merge <branch>` | Merge a branch into current branch | `git merge feature-login` |
| `git merge --abort` | Abort a merge in progress | `git merge --abort` |
| `git merge --no-ff <branch>` | Merge with no fast-forward (preserves history) | `git merge --no-ff feature-login` |
| `git rebase <branch>` | Rebase current branch onto another branch | `git rebase main` |
| `git rebase -i HEAD~n` | Interactive rebase for last n commits | `git rebase -i HEAD~3` |
| `git rebase --abort` | Abort a rebase in progress | `git rebase --abort` |
| `git rebase --continue` | Continue rebase after resolving conflicts | `git rebase --continue` |

---

## Stashing

| Command | Description | Example |
|---------|-------------|---------|
| `git stash` | Save uncommitted changes temporarily | `git stash` |
| `git stash push -m "message"` | Stash with a descriptive message | `git stash push -m "WIP: login feature"` |
| `git stash list` | List all stashes | `git stash list` |
| `git stash pop` | Apply and remove most recent stash | `git stash pop` |
| `git stash apply` | Apply stash without removing it | `git stash apply` |
| `git stash apply stash@{n}` | Apply a specific stash | `git stash apply stash@{2}` |
| `git stash drop` | Delete most recent stash | `git stash drop` |
| `git stash drop stash@{n}` | Delete a specific stash | `git stash drop stash@{1}` |
| `git stash clear` | Delete all stashes | `git stash clear` |

---

## Undoing Changes

| Command | Description | Example |
|---------|-------------|---------|
| `git checkout -- <file>` | Discard unstaged changes in a file | `git checkout -- index.html` |
| `git restore <file>` | Discard unstaged changes (modern) | `git restore style.css` |
| `git restore --staged <file>` | Unstage a file (keep changes) | `git restore --staged app.js` |
| `git reset HEAD <file>` | Unstage a file (older syntax) | `git reset HEAD app.js` |
| `git reset --soft HEAD~1` | Undo last commit (keep changes staged) | `git reset --soft HEAD~1` |
| `git reset HEAD~1` | Undo last commit (keep changes unstaged) | `git reset HEAD~1` |
| `git reset --hard HEAD~1` | Undo last commit (discard all changes) | `git reset --hard HEAD~1` |
| `git reset <commit>` | Reset to a specific commit | `git reset abc1234` |
| `git revert <commit>` | Create a new commit that undoes previous changes | `git revert abc1234` |
| `git revert HEAD~1..HEAD` | Revert a range of commits | `git revert HEAD~3..HEAD` |

---

## Remote Operations

| Command | Description | Example |
|---------|-------------|---------|
| `git fetch` | Download objects from remote (without merging) | `git fetch origin` |
| `git fetch --all` | Fetch from all remotes | `git fetch --all` |
| `git pull` | Fetch and merge changes from remote | `git pull` |
| `git pull --rebase` | Fetch and rebase instead of merge | `git pull --rebase origin main` |
| `git push` | Upload local commits to remote | `git push` |
| `git push -u origin <branch>` | Push and set upstream branch | `git push -u origin feature-login` |
| `git push origin <branch>` | Push to specific remote branch | `git push origin main` |
| `git push origin --delete <branch>` | Delete remote branch | `git push origin --delete old-feature` |
| `git push -f` | Force push (use with caution) | `git push -f origin main` |

---

## Tagging

| Command | Description | Example |
|---------|-------------|---------|
| `git tag` | List all tags | `git tag` |
| `git tag <name>` | Create a lightweight tag | `git tag v1.0.0` |
| `git tag -a <name> -m "message"` | Create an annotated tag | `git tag -a v1.0.0 -m "Release version 1.0"` |
| `git tag -a <name> <commit>` | Tag a specific commit | `git tag -a v0.9.0 abc1234` |
| `git tag -d <name>` | Delete a local tag | `git tag -d v1.0.0` |
| `git push origin <tag>` | Push a tag to remote | `git push origin v1.0.0` |
| `git push origin --tags` | Push all tags to remote | `git push origin --tags` |
| `git push origin --delete <tag>` | Delete remote tag | `git push origin --delete v1.0.0` |

---

## Cleaning

| Command | Description | Example |
|---------|-------------|---------|
| `git clean -n` | Preview files that would be deleted | `git clean -n` |
| `git clean -f` | Delete untracked files | `git clean -f` |
| `git clean -fd` | Delete untracked files and directories | `git clean -fd` |
| `git clean -fX` | Delete ignored files only | `git clean -fX` |
| `git clean -fx` | Delete ignored and non-ignored files | `git clean -fx` |

---

## Advanced Commands

| Command | Description | Example |
|---------|-------------|---------|
| `git cherry-pick <commit>` | Apply a specific commit from another branch | `git cherry-pick abc1234` |
| `git cherry-pick <commit1>..<commit2>` | Cherry-pick a range of commits | `git cherry-pick abc1234..def5678` |
| `git bisect start` | Start binary search for bug introduction | `git bisect start` |
| `git bisect bad` | Mark current commit as broken | `git bisect bad` |
| `git bisect good <commit>` | Mark commit as working | `git bisect good v1.0.0` |
| `git submodule add <url>` | Add a submodule repository | `git submodule add https://github.com/user/repo.git libs/common` |
| `git submodule update --init` | Initialize submodules | `git submodule update --init` |
| `git archive -o archive.zip HEAD` | Create archive of repository | `git archive -o project.zip HEAD` |
| `git worktree add <path> <branch>` | Add a worktree (multiple working directories) | `git worktree add ../feature-branch feature-login` |
| `git worktree list` | List all worktrees | `git worktree list` |

---

## Help Commands

| Command | Description | Example |
|---------|-------------|---------|
| `git help` | Open Git help | `git help` |
| `git help <command>` | Get help for a specific command | `git help commit` |
| `git <command> --help` | Get help for a command (alternative) | `git commit --help` |
| `git <command> -h` | Show short help for a command | `git push -h` |

---

## Useful Aliases

Add these to your `.gitconfig` for shortcuts:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'
```

---

> **Tip:** Use `git <command> -h` to quickly see available options for any command.