# Task Tracker CLI

A lightweight Command Line Interface (CLI) application to track and manage your daily tasks. Built based on the [roadmap.sh Task Tracker](https://roadmap.sh/projects/task-tracker) project specification.

## Features

- **Add, Update, & Delete**: Easily manage task items.
- **Status Tracking**: Mark tasks as `in-progress` or `done`.
- **Filtered Listing**: View all tasks or filter by status (`todo`, `in-progress`, `done`).
- **Persistent Storage**: Stores task data locally in JSON format (`data.json`).

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended)

## Usage

You can run commands directly using `uv run task-cli` (or after installing the package):

### Adding a Task
```bash
uv run task-cli add "Buy groceries"
```

### Updating a Task
```bash
uv run task-cli update 1 "Buy groceries and cook dinner"
```

### Changing Task Status
```bash
# Mark a task as in-progress
uv run task-cli mark-in-progress 1

# Mark a task as done
uv run task-cli mark-done 1
```

### Deleting a Task
```bash
uv run task-cli delete 1
```

### Listing Tasks
```bash
# List all tasks
uv run task-cli list

# List tasks by status
uv run task-cli list todo
uv run task-cli list in-progress
uv run task-cli list done
```

## Data Storage

All tasks are stored in `data.json` in the project root directory with the following structure:
- `id`: Unique identifier
- `description`: Short description of the task
- `status`: `todo` | `in-progress` | `done`
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update
