# Workout Integration Project

This project automates the syncing of workout sessions from Notion to Todoist and optionally updates Google Calendar. It's designed to streamline the process of tracking and completing workout routines, ensuring a smooth and efficient workout management experience.

## Features

- **Notion Integration**: Fetches workout sessions scheduled for the current week from a Notion database.
- **Todoist Sync**: Creates tasks in Todoist for each workout session, allowing for easy tracking and completion.
- **Google Calendar Update** (Optional): Syncs workout tasks from Todoist to Google Calendar, offering a visual overview of workout schedules.
- **Automated Workflow**: Runs as a scheduled job, ensuring that your workout tasks are always up to date.

## Getting Started

### Prerequisites

- Python 3.6+
- A Notion account with an integration token
- A Todoist account with an API token
- (Optional) Google Calendar integration set up in Todoist

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/larselona/workout-integration.git
```

2. Navigate to the project directory:

```bash
cd workout-integration
```

3. Install the required Python packages:

```python
pip install -r requirements.txt
```
### Configuration

1. Create a .env file in the project root directory with the following variables:
```
NOTION_TOKEN=<Your_Notion_Integration_Token>
TODOIST_TOKEN=<Your_Todoist_API_Token>
NOTION_DATABASE_ID=<Your_Notion_Database_ID>
```
2. (Optional) Configure the Google Calendar integration in your Todoist account.

### Usage

Run the script to fetch this week's workouts from Notion and create corresponding tasks in Todoist:

`python main.py`

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or add new features.

## License

Distributed under the MIT License. See LICENSE for more information.