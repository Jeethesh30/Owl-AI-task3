from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Task:
    title: str
    due_date: Optional[str] = None
    note: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date=None, note=None):
        title = title.strip()

        if not title:
            return False

        self.tasks.append(Task(title, due_date, note))
        return True

    def list_tasks(self):
        return self.tasks

    def remove_task(self, index):
        index = index - 1

        if index < 0 or index >= len(self.tasks):
            return False

        del self.tasks[index]
        return True

    def search_tasks(self, query):

        q = query.lower()

        return [
            t for t in self.tasks
            if q in t.title.lower()
            or (t.note and q in t.note.lower())
        ]

    def sort_tasks(self, by="title"):

        if by == "title":
            self.tasks.sort(key=lambda t: t.title.lower())

        elif by == "added":
            self.tasks.sort(key=lambda t: t.created_at)