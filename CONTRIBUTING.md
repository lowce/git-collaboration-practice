# Contributing Guidelines

Thank you for your interest in contributing to this learning project! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

### Our Standards

This is a learning environment. We expect:

✅ **Be respectful** - Everyone is learning at their own pace
✅ **Be helpful** - Share knowledge and assist others
✅ **Be constructive** - Provide feedback that helps others improve
✅ **Be patient** - Remember when you were learning these concepts
✅ **Be encouraging** - Celebrate others' progress and successes

❌ **Don't be condescending** - No "this is obvious" or "everyone knows"
❌ **Don't be dismissive** - All questions are valid questions
❌ **Don't gatekeep** - Learning should be accessible to everyone

## How to Contribute

### For Students (First-Time Contributors)

1. **Fork the repository**
   - Click "Fork" at the top right of this repository
   - This creates your own copy

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/git-collaboration-practice.git
   ```

3. **Set up upstream remote**
   ```bash
   cd git-collaboration-practice
   git remote add upstream https://github.com/datatweets/git-collaboration-practice.git
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b descriptive-branch-name
   ```

5. **Make your changes**
   - Edit files
   - Test your changes
   - Follow coding standards (see below)

6. **Commit with clear messages**
   ```bash
   git add .
   git commit -m "Clear description of what changed"
   ```

7. **Push to your fork**
   ```bash
   git push origin descriptive-branch-name
   ```

8. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "Compare & pull request"
   - Fill in the PR template
   - Submit!

## Pull Request Process

### Before Submitting

- [ ] Code runs without errors
- [ ] Tested the feature/fix manually
- [ ] Code follows the style guidelines
- [ ] Commit messages are clear and descriptive
- [ ] Branch is up to date with main

### PR Title Format

Use clear, descriptive titles:

✅ Good:
- "Add task priority feature with color coding"
- "Fix bug in completed task counter"
- "Update README with installation instructions"

❌ Bad:
- "Update"
- "Fix stuff"
- "Changes"

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Related Exercise
Exercise #X from EXERCISES.md (if applicable)

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
How did you test these changes?

## Screenshots (if applicable)
Add screenshots showing the feature working.
```

### Review Process

1. **Instructor/Maintainer will review** within 24-48 hours
2. **Address feedback** if changes are requested
3. **PR will be merged** once approved
4. **Celebrate!** 🎉 You're now a contributor!

## Coding Standards

### Python Style Guide

Follow PEP 8 style guidelines:

```python
# Good: Clear variable names, proper spacing
def calculate_total_price(items, tax_rate=0.08):
    subtotal = sum(item.price for item in items)
    total = subtotal * (1 + tax_rate)
    return total

# Bad: Unclear names, poor formatting
def calc(i,t=0.08):
    s=sum(x.p for x in i)
    return s*(1+t)
```

### Naming Conventions

- **Classes:** `PascalCase` (e.g., `TaskManager`, `Task`)
- **Functions/Methods:** `snake_case` (e.g., `add_task`, `count_completed`)
- **Variables:** `snake_case` (e.g., `task_list`, `user_input`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_TASKS`, `DEFAULT_PRIORITY`)

### Code Comments

```python
# Good: Explain WHY, not WHAT
# Calculate tax separately for accurate financial reporting
tax = subtotal * tax_rate

# Bad: State the obvious
# Add tax to subtotal
tax = subtotal * tax_rate
```

### Function Documentation

```python
def add_task(self, title, description="", priority="medium"):
    """
    Add a new task to the task list.
    
    Args:
        title (str): The task title (required)
        description (str): Optional task description
        priority (str): Priority level: 'high', 'medium', or 'low'
    
    Returns:
        bool: True if task was added successfully, False otherwise
    """
    # Implementation...
```

## Commit Message Guidelines

### Format

```
<type>: <subject>

<body (optional)>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

✅ Good commit messages:
```
feat: Add task priority feature with color-coded display

fix: Correct completed task counter logic

docs: Update README with new installation steps

refactor: Simplify task filtering logic for better readability
```

❌ Bad commit messages:
```
Update
Fix bug
Changes
asdf
```

### Tips for Good Commits

1. **Start with a verb** (Add, Fix, Update, Remove, etc.)
2. **Be specific** about what changed
3. **Keep the first line under 50 characters**
4. **Add details in the body** if needed
5. **One logical change per commit**

## Questions?

### Where to Ask

- **GitHub Issues**: For bugs or feature requests
- **Pull Request Comments**: For questions about your specific changes
- **Class Discussion**: For general Git/Python questions

### Common Questions

**Q: Can I work on multiple exercises at once?**
A: It's better to create separate branches for each exercise and submit separate PRs. This makes reviewing easier.

**Q: What if someone else is working on the same exercise?**
A: That's fine! Everyone should complete all exercises. You'll see different approaches in the PRs.

**Q: My PR has merge conflicts. What do I do?**
A: Update your branch with the latest main:
```bash
git checkout main
git pull upstream main
git checkout your-branch
git merge main
# Resolve conflicts
git commit
git push
```

**Q: Can I improve code that's not part of my exercise?**
A: Absolutely! But create a separate PR with a clear description of the improvement.

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in project documentation
- Given credit in the final project showcase

Thank you for contributing to this learning project! Every contribution helps create a better learning experience for everyone. 🚀

---

**Remember:** The goal is learning, not perfection. Don't be afraid to make mistakes—that's how we learn Git! 💪
