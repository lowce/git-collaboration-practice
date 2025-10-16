# Git Collaboration Practice

Welcome to the Git Collaboration Practice repository! This project is designed to help you master Git fundamentals through hands-on practice with a simple Python task manager application.

## 🎯 Learning Objectives

By completing the exercises in this repository, you will:

1. Clone a remote repository and set up your local environment
2. Create and switch between branches for independent development
3. Make commits with clear, descriptive messages
4. Merge branches and understand merge workflows
5. Resolve merge conflicts when they occur
6. Push your changes to remote repositories
7. Create pull requests and participate in code reviews
8. Pull updates from the main repository

## 📚 Project Overview

This is a simple **Task Manager** application written in Python. It allows users to:
- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Save tasks to a file

The simplicity of the code makes it perfect for practicing Git operations without getting distracted by complex logic.

## 🚀 Getting Started

### Prerequisites

- Git installed on your computer ([Download Git](https://git-scm.com/downloads))
- Python 3.7 or higher ([Download Python](https://www.python.org/downloads/))
- A GitHub account ([Sign up here](https://github.com/join))
- A text editor or IDE (VS Code, PyCharm, etc.)

### Step 1: Fork This Repository

1. Click the **Fork** button at the top right of this page
2. This creates your own copy of the repository under your GitHub account
3. You'll make changes in your fork and submit them via Pull Requests

### Step 2: Clone Your Fork

```bash
# Replace 'YOUR-USERNAME' with your actual GitHub username
git clone https://github.com/YOUR-USERNAME/git-collaboration-practice.git

# Navigate into the project directory
cd git-collaboration-practice

# Verify you're in the right place
ls -la
```

### Step 3: Set Up Upstream Remote

This links your fork to the original repository so you can pull updates:

```bash
# Add the original repo as 'upstream'
git remote add upstream https://github.com/datatweets/git-collaboration-practice.git

# Verify your remotes
git remote -v
# You should see:
# origin    https://github.com/YOUR-USERNAME/git-collaboration-practice.git (your fork)
# upstream  https://github.com/datatweets/git-collaboration-practice.git (original)
```

### Step 4: Run the Application

```bash
# Run the task manager
python task_manager.py

# Follow the on-screen prompts to interact with the app
```

## 📝 Practice Exercises

Complete these exercises in order to build your Git skills progressively.

### Exercise 1: Your First Branch and Commit

**Goal:** Create a feature branch and add your name to the contributors list.

```bash
# Make sure you're on the main branch and it's up to date
git checkout main
git pull upstream main

# Create a new branch (replace 'yourname' with your actual name)
git checkout -b add-contributor-yourname

# Open CONTRIBUTORS.md and add your name
# Then stage and commit
git add CONTRIBUTORS.md
git commit -m "Add [Your Name] to contributors list"

# Push your branch to your fork
git push origin add-contributor-yourname
```

**Next:** Go to GitHub and create a Pull Request from your fork to the original repository.

### Exercise 2: Add a New Feature

**Goal:** Add a feature to display tasks by priority.

```bash
# Create a feature branch
git checkout main
git pull upstream main
git checkout -b feature-priority-display

# Edit task_manager.py to add priority functionality
# (See EXERCISES.md for detailed instructions)

# Stage and commit your changes
git add task_manager.py
git commit -m "Add priority display feature to task list"

# Push to your fork
git push origin feature-priority-display
```

### Exercise 3: Fix a Bug

**Goal:** Find and fix the bug in the task completion feature.

```bash
# Create a bugfix branch
git checkout main
git pull upstream main
git checkout -b bugfix-completion-counter

# Fix the bug in task_manager.py
# (Hint: Check the count_completed_tasks function)

git add task_manager.py
git commit -m "Fix incorrect count in completed tasks display"

git push origin bugfix-completion-counter
```

### Exercise 4: Resolve Merge Conflicts

**Goal:** Practice resolving merge conflicts intentionally created for learning.

```bash
# Create a conflict branch
git checkout main
git pull upstream main
git checkout -b practice-conflict-resolution

# Edit the same lines in task_manager.py that others have edited
# Follow instructions in EXERCISES.md

# Try to merge main into your branch
git merge main
# You'll see a conflict!

# Open the conflicted file and resolve it
# Remove conflict markers and keep the correct code
git add task_manager.py
git commit -m "Resolve merge conflict in task display formatting"

git push origin practice-conflict-resolution
```

### Exercise 5: Collaborative Development

**Goal:** Work with classmates by reviewing their Pull Requests.

1. Browse open Pull Requests in the original repository
2. Review the code changes
3. Leave constructive comments
4. Approve or request changes
5. Learn from others' approaches

## 🛠️ Project Structure

```
git-collaboration-practice/
├── README.md              # This file
├── CONTRIBUTORS.md        # List of all contributors
├── EXERCISES.md          # Detailed exercise instructions
├── task_manager.py       # Main application code
├── tasks.json           # Task storage file (auto-generated)
├── .gitignore           # Files to ignore in Git
└── tests/
    └── test_task_manager.py  # Unit tests (optional advanced exercise)
```

## 📖 Git Command Reference

Here are the essential Git commands you'll use frequently:

```bash
# Check status of your repository
git status

# See what branches exist
git branch

# Create and switch to a new branch
git checkout -b branch-name

# Stage files for commit
git add filename.py
git add .  # Stage all changes

# Commit staged changes
git commit -m "Descriptive commit message"

# Push to your fork
git push origin branch-name

# Pull latest changes from upstream
git pull upstream main

# Merge another branch into current branch
git merge branch-name

# View commit history
git log --oneline --graph

# Abort a merge if you get confused
git merge --abort
```

## ✅ Best Practices

1. **Always pull before starting new work**
   ```bash
   git checkout main
   git pull upstream main
   ```

2. **Create a new branch for each feature or fix**
   - Use descriptive names: `feature-add-priority`, `bugfix-delete-task`

3. **Write clear commit messages**
   - Start with a verb: "Add", "Fix", "Update", "Remove"
   - Be specific: "Add task filtering by status" not "Update code"

4. **Commit often with logical changes**
   - Don't bundle unrelated changes in one commit
   - Each commit should represent one logical change

5. **Test your code before committing**
   - Run the application and verify it works
   - Check for syntax errors

6. **Keep commits small and focused**
   - Easier to review
   - Easier to revert if needed

## 🤝 Contributing Guidelines

### Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch from `main`
3. **Make** your changes and commit them
4. **Push** to your fork
5. **Open** a Pull Request with:
   - A clear title
   - Description of what you changed and why
   - Reference to any related exercises

### Code Review Expectations

When reviewing others' PRs:
- Be respectful and constructive
- Ask questions if you don't understand something
- Suggest improvements, don't just criticize
- Approve when the code looks good

When your PR is reviewed:
- Respond to comments
- Make requested changes
- Thank reviewers for their time

## 🐛 Common Issues and Solutions

### Issue: "Permission denied" when pushing

**Solution:** Make sure you're pushing to your fork (origin), not upstream:
```bash
git push origin branch-name  # ✅ Correct
git push upstream branch-name  # ❌ Won't work
```

### Issue: "Your branch is behind"

**Solution:** Pull the latest changes first:
```bash
git pull upstream main
```

### Issue: Merge conflict is confusing

**Solution:** Look for conflict markers and choose the correct code:
```python
<<<<<<< HEAD
# Your version
=======
# Their version
>>>>>>> branch-name
```
Remove the markers and keep the right code, then:
```bash
git add filename.py
git commit -m "Resolve merge conflict"
```

### Issue: Committed to wrong branch

**Solution:** Stash your changes and move them:
```bash
git stash
git checkout correct-branch
git stash pop
```

## 📚 Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Git Branching Visualization](https://learngitbranching.js.org/)

## 🎓 Learning Path

### Beginner Level
- ✅ Complete Exercise 1: Add yourself as a contributor
- ✅ Complete Exercise 2: Add a new feature
- ✅ Complete Exercise 3: Fix a bug

### Intermediate Level
- ✅ Complete Exercise 4: Resolve merge conflicts
- ✅ Complete Exercise 5: Review others' Pull Requests
- ✅ Add unit tests for your features

### Advanced Level
- ✅ Help others resolve their merge conflicts
- ✅ Propose and implement major new features
- ✅ Become a regular contributor and reviewer

## 📧 Questions?

If you're stuck or confused:
1. Check the [Issues](https://github.com/datatweets/git-collaboration-practice/issues) page
2. Ask your instructor or classmates
3. Create a new issue describing your problem

## 📜 License

This project is created for educational purposes. Feel free to use and modify for learning Git and collaboration skills.

---

**Happy collaborating! 🚀**

Remember: Making mistakes is part of learning Git. Don't be afraid to experiment!
