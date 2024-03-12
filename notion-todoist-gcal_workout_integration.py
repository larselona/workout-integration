from dotenv import load_dotenv
import os
from notion_client import Client as NotionClient
from todoist_api_python.api import TodoistAPI
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Access environment variables
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
TODOIST_TOKEN = os.getenv('TODOIST_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

notion = NotionClient(auth=NOTION_TOKEN)
todoist_api = TodoistAPI(TODOIST_TOKEN)

def get_start_end_dates():
    today = datetime.now()
    start_week = today - timedelta(days=today.weekday())
    end_week = start_week + timedelta(days=6)
    return start_week.date(), end_week.date()

def fetch_notion_workouts(start_date, end_date):
    workouts = []
    query = notion.databases.query(
        **{
            "database_id": NOTION_DATABASE_ID,
            "filter": {
                "and": [
                    {
                        "property": "Date",
                        "date": {"on_or_after": start_date.isoformat()}
                    },
                    {
                        "property": "Date",
                        "date": {"on_or_before": end_date.isoformat()}
                    }
                ]
            }
        }
    )
    
    for item in query['results']:
        workout_date = item['properties']['Date']['date']['start'] if item['properties']['Date']['date'] else None
        workout_name = item['properties']['Name']['title'][0]['plain_text'] if item['properties']['Name']['title'] else "No Title"
        workouts.append((workout_name, workout_date))
    return workouts

def create_todoist_task(name, due_date):
    try:
        task = todoist_api.add_task(content=name, due_date=due_date)
        print(f"Task '{name}' created in Todoist")
    except Exception as e:
        print(f"Failed to create task '{name}'. Error: {str(e)}")

def main():
    start_date, end_date = get_start_end_dates()
    workouts = fetch_notion_workouts(start_date, end_date)
    for name, date in workouts:
        create_todoist_task(name, date)

if __name__ == "__main__":
    main()
