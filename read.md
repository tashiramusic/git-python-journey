Absolutely. Since you're using **Git + GitHub + Neovim/PowerShell**, here's a practical beginner Git tutorial. You don't need to memorize everything—learn this workflow first.

# 🚀 Git Basic Commands — Quick Tutorial

Think of Git like this:

```text
Your files
   ↓
git add
   ↓
Staging area
   ↓
git commit
   ↓
Local Git history
   ↓
git push
   ↓
GitHub
```

---

## 1. Check if Git is working

```powershell
git --version
```

Example:

```text
git version 2.x.x
```

---

# 2. Create a Git repository

Go into your project:

```powershell
cd "D:\Tashira CODING\WEB dev\2026\my-python-projects"
```

Then:

```powershell
git init
```

This creates a hidden `.git` folder.

You normally only do `git init` **once per project**.

---

# 3. Check what's happening

This is probably the **most important command**:

```powershell
git status
```

It tells you:

* what files changed
* what files are new
* what is staged
* what branch you're on

Example:

```text
Untracked files:
    quiz.py
```

---

# 4. Add files

Suppose you created:

```text
quiz.py
```

Add it:

```powershell
git add quiz.py
```

Or add **everything**:

```powershell
git add .
```

Then check:

```powershell
git status
```

You should see the file under something like:

```text
Changes to be committed:
    quiz.py
```

---

# 5. Commit

A commit is basically a **save point in Git history**.

```powershell
git commit -m "Create quiz project"
```

Example:

```text
[master abc1234] Create quiz project
```

Good commit messages describe what you changed:

```powershell
git commit -m "Add score calculation"
git commit -m "Fix quiz answer checking"
git commit -m "Add rock paper scissors game"
```

---

# 6. See your commits

```powershell
git log
```

You'll see something like:

```text
commit abc123...
Author: Tashira
Date: ...

    Create quiz project
```

A cleaner version:

```powershell
git log --oneline
```

Example:

```text
a82f123 Add score calculation
7b21abc Create quiz project
```

---

# 7. See what you changed

Before committing, you can check your changes:

```powershell
git diff
```

This is extremely useful.

For example:

```text
- print("Hello")
+ print("Hello Tashira")
```

It means you removed the first line and added the second.

---

# 8. The basic daily workflow ⭐

This is the workflow I want you to memorize:

```powershell
git status
```

Work on your code.

Then:

```powershell
git status
git add .
git commit -m "Describe what I changed"
```

That's it for local Git.

---

# 🌐 9. Connect your project to GitHub

If you've already created a repository on GitHub, you'll connect it with:

```powershell
git remote add origin YOUR_REPOSITORY_URL
```

Check it:

```powershell
git remote -v
```

Then push:

```powershell
git push -u origin master
```

⚠️ Your branch might be called `main` instead of `master`.

Check:

```powershell
git branch
```

If you're on `main`:

```powershell
git push -u origin main
```

---

# 10. After the first push

Usually you can simply do:

```powershell
git add .
git commit -m "Update project"
git push
```

That's your normal GitHub workflow.

---

# 📥 11. Get changes from GitHub

If the GitHub repository has newer changes:

```powershell
git pull
```

Think:

```text
GitHub → Your computer
```

while:

```powershell
git push
```

means:

```text
Your computer → GitHub
```

---

# 🌿 12. Branches — basic idea

Branches let you work on something without messing with your main code.

See branches:

```powershell
git branch
```

Create one:

```powershell
git branch feature-login
```

Switch to it:

```powershell
git switch feature-login
```

Or create + switch immediately:

```powershell
git switch -c feature-login
```

Go back:

```powershell
git switch master
```

or:

```powershell
git switch main
```

You don't need to become an expert with branches yet.

---

# 🗑️ 13. Undo some common mistakes

### Accidentally staged a file

```powershell
git restore --staged filename.py
```

You haven't deleted the file—it just removes it from staging.

---

### Undo changes you haven't committed

```powershell
git restore filename.py
```

⚠️ This can discard your uncommitted changes.

---

### See previous commits

```powershell
git log --oneline
```

---

# 🧠 Your Git cheat sheet

| Command                   | What it does            |
| ------------------------- | ----------------------- |
| `git init`                | Start Git in a project  |
| `git status`              | See what's happening    |
| `git add .`               | Stage everything        |
| `git add file.py`         | Stage one file          |
| `git commit -m "message"` | Save a version          |
| `git log`                 | See history             |
| `git log --oneline`       | Compact history         |
| `git diff`                | See changes             |
| `git branch`              | See branches            |
| `git switch branch`       | Switch branches         |
| `git switch -c name`      | Create + switch branch  |
| `git push`                | Send commits to GitHub  |
| `git pull`                | Get changes from GitHub |
| `git remote -v`           | See GitHub connection   |

## ⭐ For you, memorize these 6 first

Don't try to memorize 30 commands.

```powershell
git status
git add .
git commit -m "message"
git log --oneline
git push
git pull
```

Your normal beginner workflow will be:

```text
🧑‍💻 Write code
      ↓
git status
      ↓
git add .
      ↓
git commit -m "What I changed"
      ↓
git push
      ↓
☁️ GitHub
```

And **`git status` is your best friend** while learning Git.
