# Detailed Exercise Instructions

This guide provides step-by-step instructions for each practice exercise.

## 📝 Exercise 1: Add Yourself as a Contributor

**Learning Goals:** Basic branch creation, commits, and pull requests

**Time:** 10-15 minutes

### Steps:

1. **Ensure you're starting fresh:**
   ```bash
   git checkout main
   git pull upstream main
   ```

2. **Create your branch:**
   ```bash
   # Replace 'yourname' with your actual first name (lowercase, no spaces)
   git checkout -b add-contributor-yourname
   ```

3. **Edit CONTRIBUTORS.md:**
   - Open `CONTRIBUTORS.md` in your editor
   - Add your name in alphabetical order under the "Contributors List" section
   - Format: `- **Your Full Name** - Student`
   
   Example:
   ```markdown
   - **Alice Johnson** - Student
   - **Bob Smith** - Student
   ```

4. **Check what changed:**
   ```bash
   git status
   # You should see CONTRIBUTORS.md as modified
   
   git diff
   # Shows the exact lines you added
   ```

5. **Stage and commit:**
   ```bash
   git add CONTRIBUTORS.md
   git commit -m "Add [Your Name] to contributors list"
   ```

6. **Push to your fork:**
   ```bash
   git push origin add-contributor-yourname
   ```

7. **Create a Pull Request:**
   - Go to your fork on GitHub
   - Click "Compare & pull request"
   - Title: "Add [Your Name] to contributors"
   - Description: "Completed Exercise 1: Added myself to the contributors list"
   - Click "Create pull request"

**Expected Result:** You've successfully created your first PR! Wait for review.

---

## 🎨 Exercise 2: Add Priority Feature

**Learning Goals:** Feature development, multiple commits, code modification

**Time:** 20-30 minutes

### Steps:

1. **Create feature branch:**
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feature-task-priority
   ```

2. **Modify the Task class:**
   
   Open `task_manager.py` and find the `Task.__init__` method. Add a priority parameter:
   
   ```python
   def __init__(self, title, description="", completed=False, created_at=None, priority="medium"):
       self.title = title
       self.description = description
       self.completed = completed
       self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       self.priority = priority  # Add this line
   ```

3. **Update the `to_dict` method:**
   
   Add priority to the dictionary:
   ```python
   def to_dict(self):
       return {
           "title": self.title,
           "description": self.description,
           "completed": self.completed,
           "created_at": self.created_at,
           "priority": self.priority  # Add this line
       }
   ```

4. **Update the `from_dict` method:**
   
   ```python
   @staticmethod
   def from_dict(data):
       return Task(
           title=data["title"],
           description=data.get("description", ""),
           completed=data.get("completed", False),
           created_at=data.get("created_at"),
           priority=data.get("priority", "medium")  # Add this line
       )
   ```

5. **Update the `__str__` method to show priority:**
   
   ```python
   def __str__(self):
       status = "✓" if self.completed else "○"
       priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
       emoji = priority_emoji.get(self.priority, "⚪")
       return f"[{status}] {emoji} {self.title}"
   ```

6. **Update `TaskManager.add_task` to accept priority:**
   
   Find the `add_task` method and modify it:
   ```python
   def add_task(self, title, description="", priority="medium"):
       if not title.strip():
           print("❌ Error: Task title cannot be empty!")
           return False
       
       task = Task(title.strip(), description.strip(), priority=priority)
       self.tasks.append(task)
       self.save_tasks()
       print(f"✅ Task added: {title} (Priority: {priority})")
       return True
   ```

7. **Update the main menu to ask for priority:**
   
   Find the `main()` function, in the "Add task" section:
   ```python
   elif choice == "2":
       print("\n➕ ADD NEW TASK")
       print("-" * 60)
       title = input("Task title: ").strip()
       description = input("Description (optional): ").strip()
       print("Priority options: high, medium, low")
       priority = input("Priority (default: medium): ").strip().lower()
       if priority not in ["high", "medium", "low"]:
           priority = "medium"
       manager.add_task(title, description, priority)
   ```

8. **Test your changes:**
   ```bash
   python task_manager.py
   # Add a task and verify priority is displayed
   ```

9. **Commit your changes:**
   ```bash
   git add task_manager.py
   git commit -m "Add priority field to Task class with color-coded display"
   ```

10. **Push and create PR:**
    ```bash
    git push origin feature-task-priority
    ```

**Expected Result:** Tasks now have priority levels shown with colored emojis!

---

## 🐛 Exercise 3: Fix the Bug

**Learning Goals:** Bug identification, debugging, testing fixes

**Time:** 15-20 minutes

### Steps:

1. **Create bugfix branch:**
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b bugfix-completion-counter
   ```

2. **Find the bug:**
   
   Look at the `count_completed_tasks` method in the `TaskManager` class:
   ```python
   def count_completed_tasks(self):
       """Count how many tasks are completed."""
       # BUG: This counts incorrectly! 
       return sum(1 for task in self.tasks if not task.completed)
   ```
   
   **Question:** What's wrong with this logic?
   
   **Answer:** It counts tasks where `completed` is `False` (not completed), but we want to count tasks where `completed` is `True`!

3. **Fix the bug:**
   
   Change the method to:
   ```python
   def count_completed_tasks(self):
       """Count how many tasks are completed."""
       return sum(1 for task in self.tasks if task.completed)
   ```

4. **Test the fix:**
   ```bash
   python task_manager.py
   # Add some tasks, complete a few, and view the summary
   # Verify the count is now correct
   ```

5. **Commit the fix:**
   ```bash
   git add task_manager.py
   git commit -m "Fix bug: count_completed_tasks was counting incomplete tasks"
   ```

6. **Push and create PR:**
   ```bash
   git push origin bugfix-completion-counter
   ```

**Expected Result:** The completed tasks counter now shows the correct number!

---

## ⚔️ Exercise 4: Resolve Merge Conflicts

**Learning Goals:** Understanding and resolving merge conflicts

**Time:** 20-30 minutes

### Steps:

1. **Create conflict practice branch:**
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b practice-conflict-resolution
   ```

2. **Make a conflicting change:**
   
   Open `task_manager.py` and find the `view_tasks` method. Change the header:
   
   ```python
   def view_tasks(self):
       """Display all tasks."""
       if not self.tasks:
           print("\n📝 No tasks yet! Add some tasks to get started.\n")
           return
       
       print("\n" + "="*60)
       print("📋 MY AWESOME TASK LIST")  # Change this line
       print("="*60)
   ```

3. **Commit your change:**
   ```bash
   git add task_manager.py
   git commit -m "Update task list header to be more enthusiastic"
   ```

4. **Simulate someone else's change:**
   
   Switch to main and make a different change to the same line:
   ```bash
   git checkout main
   # Edit the same line to say something different like "📋 TASK OVERVIEW"
   git add task_manager.py
   git commit -m "Update task list header for clarity"
   ```

5. **Try to merge and create conflict:**
   ```bash
   git checkout practice-conflict-resolution
   git merge main
   ```
   
   You'll see:
   ```
   Auto-merging task_manager.py
   CONFLICT (content): Merge conflict in task_manager.py
   Automatic merge failed; fix conflicts and then commit the result.
   ```

6. **Open the conflicted file:**
   
   You'll see conflict markers:
   ```python
   print("\n" + "="*60)
   <<<<<<< HEAD
   print("📋 MY AWESOME TASK LIST")
   =======
   print("📋 TASK OVERVIEW")
   >>>>>>> main
   print("="*60)
   ```

7. **Resolve the conflict:**
   
   Decide which version to keep or combine them:
   ```python
   print("\n" + "="*60)
   print("📋 MY TASK OVERVIEW")  # Combined version
   print("="*60)
   ```
   
   Remove all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)

8. **Complete the merge:**
   ```bash
   git add task_manager.py
   git commit -m "Resolve merge conflict in view_tasks header"
   ```

9. **Push the resolved branch:**
   ```bash
   git push origin practice-conflict-resolution
   ```

**Expected Result:** You've successfully resolved a merge conflict!

---

## 🤝 Exercise 5: Code Review Practice

**Learning Goals:** Pull request reviews, constructive feedback

**Time:** 15-20 minutes per review

### Steps:

1. **Find open Pull Requests:**
   - Go to the original repository: `https://github.com/datatweets/git-collaboration-practice`
   - Click on "Pull Requests" tab
   - Browse open PRs from your classmates

2. **Review a Pull Request:**
   - Click on a PR to open it
   - Go to "Files changed" tab
   - Review the code changes

3. **Leave constructive comments:**
   
   **Good comments:**
   - ✅ "Nice work! The priority feature works well. Consider adding validation to ensure priority is one of the three valid options."
   - ✅ "I noticed the same bug in my code! This fix looks correct."
   - ✅ "The commit message clearly describes what changed. Well done!"
   
   **Avoid:**
   - ❌ "This is wrong."
   - ❌ "I don't like this."
   - ❌ "My way is better."

4. **Ask questions:**
   - "Why did you choose to implement it this way?"
   - "Have you tested this with edge cases like empty task lists?"

5. **Approve or request changes:**
   - If the code looks good: Click "Review changes" → "Approve"
   - If you see issues: Click "Review changes" → "Request changes" with explanations

6. **Learn from others:**
   - See different approaches to the same problem
   - Note clever solutions you can learn from
   - Identify common mistakes to avoid

**Expected Result:** You've participated in collaborative code review!

---

## 🎯 Bonus Exercises

### Bonus 1: Add Task Filtering

Add a feature to filter tasks by completion status or priority.

**Branch name:** `feature-task-filtering`

**Hint:** Add a new menu option and create a `filter_tasks` method in `TaskManager`.

### Bonus 2: Add Due Dates

Add due dates to tasks and highlight overdue tasks.

**Branch name:** `feature-due-dates`

**Hint:** Use Python's `datetime` module to compare dates.

### Bonus 3: Write Unit Tests

Create unit tests for the `Task` and `TaskManager` classes.

**Branch name:** `add-unit-tests`

**Hint:** Use Python's `unittest` module. Create `tests/test_task_manager.py`.

### Bonus 4: Add Task Search

Implement a search feature to find tasks by title or description.

**Branch name:** `feature-task-search`

### Bonus 5: Improve UI

Make the CLI more colorful using the `colorama` library.

**Branch name:** `improve-ui-colors`

---

## 🆘 Troubleshooting

### "I'm on the wrong branch!"

```bash
# If you haven't committed yet
git stash
git checkout correct-branch
git stash pop

# If you already committed
git checkout correct-branch
git cherry-pick <commit-hash>
```

### "I made a typo in my commit message!"

```bash
# If you haven't pushed yet
git commit --amend -m "Corrected commit message"

# If you already pushed, just make a note in the PR description
```

### "I accidentally deleted important code!"

```bash
# If you haven't committed
git checkout -- filename.py

# If you committed but want to undo
git revert <commit-hash>
```

### "My merge is a mess!"

```bash
# Abort the merge and start over
git merge --abort

# Pull latest changes and try again
git pull upstream main
```

---

## 📊 Progress Checklist

Track your learning progress:

- [ ] Exercise 1: Added myself to CONTRIBUTORS.md
- [ ] Exercise 2: Implemented priority feature
- [ ] Exercise 3: Fixed the completion counter bug
- [ ] Exercise 4: Successfully resolved a merge conflict
- [ ] Exercise 5: Reviewed at least 2 pull requests
- [ ] Bonus: Completed at least one bonus exercise

**Congratulations on completing all exercises! You're now comfortable with Git basics! 🎉**
