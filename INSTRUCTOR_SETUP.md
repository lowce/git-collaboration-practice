# Instructor Setup Guide

## Quick Setup Instructions for GitHub

Follow these steps to push the repository to GitHub and prepare it for your students.

### Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `git-collaboration-practice`
3. Description: "A hands-on Git practice repository for learning version control through a Python task manager project"
4. **Keep it PUBLIC** (so students can fork it)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Step 2: Push to GitHub

From your terminal in the `git-collaboration-practice` directory:

```bash
cd /Users/lotfinejad/git-collaboration-practice

# Add the remote (replace 'datatweets' with your GitHub username if different)
git remote add origin https://github.com/datatweets/git-collaboration-practice.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Configure Repository Settings

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Under **General** → **Features**:
   - ✅ Enable Issues (for student questions)
   - ✅ Enable Projects (optional)
   - ✅ Enable Wiki (optional)

4. Under **Pull Requests**:
   - ✅ Allow merge commits
   - ✅ Allow squash merging
   - ✅ Automatically delete head branches

5. Under **Branches** → **Add branch protection rule**:
   - Branch name pattern: `main`
   - ✅ Require pull request reviews before merging
   - Number of required approvals: 1 (you'll review)

### Step 4: Create Issues for Common Questions (Optional)

Create a few issues that students might reference:

**Issue 1: Common Git Commands Reference**
```
Title: Common Git Commands Quick Reference

Labels: documentation, help-wanted

Body:
This issue serves as a quick reference for common Git commands used in this project.

**Branch Management:**
- `git branch` - List all branches
- `git checkout -b <name>` - Create and switch to new branch
- `git checkout <name>` - Switch to existing branch

**Making Changes:**
- `git status` - See what's changed
- `git add <file>` - Stage specific file
- `git add .` - Stage all changes
- `git commit -m "message"` - Commit staged changes

**Syncing:**
- `git pull upstream main` - Get latest changes
- `git push origin <branch>` - Push your changes

**Troubleshooting:**
- `git merge --abort` - Cancel a merge
- `git stash` - Temporarily save changes
- `git stash pop` - Restore stashed changes

Feel free to ask questions in the comments!
```

### Step 5: Student Instructions Document

Share this with your students:

```markdown
# How to Get Started

## Prerequisites
- Git installed: https://git-scm.com/downloads
- Python 3.7+: https://www.python.org/downloads/
- GitHub account: https://github.com/join

## Setup Steps

### 1. Fork the Repository
1. Go to https://github.com/datatweets/git-collaboration-practice
2. Click the "Fork" button (top right)
3. This creates YOUR copy of the project

### 2. Clone Your Fork
```bash
# Replace YOUR-USERNAME with your actual GitHub username
git clone https://github.com/YOUR-USERNAME/git-collaboration-practice.git
cd git-collaboration-practice
```

### 3. Set Up Upstream
```bash
git remote add upstream https://github.com/datatweets/git-collaboration-practice.git
git remote -v
# You should see both 'origin' (your fork) and 'upstream' (original)
```

### 4. Test the Application
```bash
python3 task_manager.py
# Or on Windows:
python task_manager.py
```

### 5. Start with Exercise 1
Open `EXERCISES.md` and follow the instructions for Exercise 1.

## Getting Help

- **Read the Documentation**: README.md and EXERCISES.md
- **Check Issues**: See if someone else asked your question
- **Ask Questions**: Create a new issue with [HELP] in the title
- **Ask Your Instructor**: During class or office hours
```

### Step 6: Prepare for First Class

**Before class:**
1. Test the entire workflow yourself by:
   - Creating a new GitHub account (or using a test account)
   - Forking your repo
   - Completing Exercise 1
   - Submitting a PR
   - Reviewing and merging it

**During first class:**
1. Walk through the setup (Steps 1-4 above)
2. Demonstrate Exercise 1 live
3. Show how to create a branch
4. Show how to make changes
5. Show how to create a PR
6. Show the PR review process

**Common Student Issues to Prepare For:**

| Issue | Solution |
|-------|----------|
| "Git is not recognized" | Need to install Git |
| "Permission denied (publickey)" | Need to set up SSH or use HTTPS |
| "python: command not found" | Use `python3` on Mac/Linux |
| "I pushed to the wrong repo!" | They pushed to upstream instead of origin |
| "Merge conflict is scary!" | Walk through it together, use the guide |

### Step 7: Monitoring Student Progress

**View all Pull Requests:**
- Go to your repo → Pull Requests tab
- Filter by labels (you can create labels like "exercise-1", "exercise-2")

**Review PRs:**
1. Read the code changes
2. Leave constructive comments
3. Approve or request changes
4. Merge when ready

**Track Participation:**
Create a spreadsheet with:
- Student Name
- GitHub Username
- Exercise 1 Completed (Y/N)
- Exercise 2 Completed (Y/N)
- Exercise 3 Completed (Y/N)
- Exercise 4 Completed (Y/N)
- Exercise 5 Completed (Y/N)
- Total PRs Reviewed

### Step 8: Adding New Exercises (Optional)

To add new exercises as the course progresses:

```bash
cd /Users/lotfinejad/git-collaboration-practice

# Create a new branch for the update
git checkout -b add-exercise-6

# Edit EXERCISES.md to add the new exercise
# Edit task_manager.py if needed

git add EXERCISES.md
git commit -m "Add Exercise 6: Task categories feature"
git push origin add-exercise-6

# Create PR, review, merge to main
# Students will pull the update: git pull upstream main
```

## Quick Command Reference for You

```bash
# See all student PRs
# (Do this on GitHub website)

# Pull latest changes students made
git pull origin main

# Create a new branch for updates
git checkout -b update-exercises

# Make changes, commit, push
git add .
git commit -m "Update exercise instructions"
git push origin update-exercises

# Merge on GitHub, then update your local main
git checkout main
git pull origin main
```

## Troubleshooting for Students

### Issue: "I can't push to the main repository"

**Correct behavior!** Students should:
1. Push to their fork: `git push origin branch-name`
2. Create a PR from their fork to your repo

### Issue: "My fork is behind the main repo"

```bash
git checkout main
git pull upstream main
git push origin main
```

### Issue: "I have merge conflicts"

Walk them through:
1. Open the conflicted file
2. Find the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Edit to keep the correct code
4. Remove the markers
5. `git add <file>`
6. `git commit`

## Tips for Success

1. **Review PRs quickly** (within 24 hours) to keep students engaged
2. **Be encouraging** - celebrate their progress
3. **Make mistakes intentionally** to show how to fix them
4. **Share good examples** - highlight well-written PRs
5. **Create a safe space** - emphasize learning over perfection

## Assessment Ideas

**Formative (During Learning):**
- Check that all exercises are completed
- Review code quality in PRs
- Observe participation in code reviews

**Summative (Final Assessment):**
- Completion of all 5 exercises (50%)
- Quality of code reviews given (25%)
- Implementation of bonus features (25%)

## Ready to Go!

Your repository is now ready for students. The exercises progress from simple to complex:

1. **Exercise 1**: Basic Git workflow (fork, clone, branch, commit, PR)
2. **Exercise 2**: Feature development (multiple commits, testing)
3. **Exercise 3**: Bug fixing (debugging, testing)
4. **Exercise 4**: Merge conflicts (conflict resolution)
5. **Exercise 5**: Code review (collaboration, feedback)

**Good luck with your class! 🚀**

---

## Questions?

If you need to modify anything in this repo or have questions about the setup, feel free to adjust the files as needed. Everything is documented and modular.
