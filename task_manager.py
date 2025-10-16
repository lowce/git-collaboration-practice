#!/usr/bin/env python3
"""
Simple Task Manager Application
================================

A beginner-friendly task management system for learning Git and Python.

Features:
- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Persist tasks to JSON file

This code is intentionally simple to focus on Git concepts, not complex programming.
"""

import json
import os
from datetime import datetime


class Task:
    """Represents a single task with title, description, and completion status."""
    
    def __init__(self, title, description="", completed=False, created_at=None):
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True
    
    def to_dict(self):
        """Convert task to dictionary for JSON storage."""
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        """Create a Task object from a dictionary."""
        return Task(
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            created_at=data.get("created_at")
        )
    
    def __str__(self):
        """String representation of the task."""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.title}"


class TaskManager:
    """Manages a collection of tasks with persistence."""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, title, description=""):
        """Add a new task to the list."""
        if not title.strip():
            print("❌ Error: Task title cannot be empty!")
            return False
        
        task = Task(title.strip(), description.strip())
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: {title}")
        return True
    
    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\n📝 No tasks yet! Add some tasks to get started.\n")
            return
        
        print("\n" + "="*60)
        print("📋 YOUR TASKS")
        print("="*60)
        
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")
            if task.description:
                print(f"   Description: {task.description}")
            print(f"   Created: {task.created_at}")
            print("-" * 60)
        
        # Display summary
        completed = self.count_completed_tasks()
        total = len(self.tasks)
        print(f"\n📊 Summary: {completed}/{total} tasks completed")
        print("="*60 + "\n")
    
    def complete_task(self, task_number):
        """Mark a task as complete by its number."""
        if not self.tasks:
            print("❌ No tasks available!")
            return False
        
        if task_number < 1 or task_number > len(self.tasks):
            print(f"❌ Invalid task number! Choose between 1 and {len(self.tasks)}")
            return False
        
        task = self.tasks[task_number - 1]
        if task.completed:
            print(f"ℹ️  Task '{task.title}' is already completed!")
        else:
            task.mark_complete()
            self.save_tasks()
            print(f"✅ Task completed: {task.title}")
        return True
    
    def delete_task(self, task_number):
        """Delete a task by its number."""
        if not self.tasks:
            print("❌ No tasks available!")
            return False
        
        if task_number < 1 or task_number > len(self.tasks):
            print(f"❌ Invalid task number! Choose between 1 and {len(self.tasks)}")
            return False
        
        task = self.tasks.pop(task_number - 1)
        self.save_tasks()
        print(f"🗑️  Task deleted: {task.title}")
        return True
    
    def count_completed_tasks(self):
        """Count how many tasks are completed."""
        # BUG: This counts incorrectly! 
        # Exercise 3: Can you find and fix this bug?
        return sum(1 for task in self.tasks if not task.completed)
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except Exception as e:
            print(f"❌ Error saving tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except Exception as e:
            print(f"⚠️  Warning: Could not load tasks: {e}")
            self.tasks = []


def display_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("🎯 TASK MANAGER - MAIN MENU")
    print("="*60)
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")
    print("="*60)


def main():
    """Main application loop."""
    print("\n" + "🌟"*30)
    print("   Welcome to Task Manager!")
    print("   A simple app for learning Git & Python")
    print("🌟"*30 + "\n")
    
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("\n👉 Enter your choice (1-5): ").strip()
        
        if choice == "1":
            manager.view_tasks()
        
        elif choice == "2":
            print("\n➕ ADD NEW TASK")
            print("-" * 60)
            title = input("Task title: ").strip()
            description = input("Description (optional): ").strip()
            manager.add_task(title, description)
        
        elif choice == "3":
            manager.view_tasks()
            if manager.tasks:
                try:
                    task_num = int(input("\n👉 Enter task number to complete: "))
                    manager.complete_task(task_num)
                except ValueError:
                    print("❌ Please enter a valid number!")
        
        elif choice == "4":
            manager.view_tasks()
            if manager.tasks:
                try:
                    task_num = int(input("\n👉 Enter task number to delete: "))
                    confirm = input(f"⚠️  Are you sure? (yes/no): ").lower()
                    if confirm in ['yes', 'y']:
                        manager.delete_task(task_num)
                    else:
                        print("ℹ️  Deletion cancelled.")
                except ValueError:
                    print("❌ Please enter a valid number!")
        
        elif choice == "5":
            print("\n👋 Thanks for using Task Manager! Goodbye!\n")
            break
        
        else:
            print("❌ Invalid choice! Please choose 1-5.")


if __name__ == "__main__":
    main()
