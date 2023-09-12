from fastapi import FastAPI, HTTPException
from datetime import datetime
import pytz

app = FastAPI()

# Sample data (you can replace this with your own data)
slack_name = "Mohammed Ibrahim (mdjyoung)"
track = "BackEnd"
github_file_url = "https://github.com/MohammedIbrahim8"
github_source_url = "Your GitHub Source URL"

@app.get("/get_info/")
async def get_info(slack_name: str, track: str):
    # Calculate current UTC time with timezone validation
    utc_now = datetime.now(pytz.UTC)
    utc_offset = utc_now.utcoffset()

    if utc_offset.total_seconds() < -7200 or utc_offset.total_seconds() > 7200:
        raise HTTPException(status_code=400, detail="Invalid UTC offset")

    # Get the current day of the week
    day_of_week = utc_now.strftime('%A')

    return {
        "Slack name": slack_name,
        "Current day of the week": day_of_week,
        "Current UTC time": utc_now.strftime('%Y-%m-%d %H:%M:%S %Z'),
        "Track": track,
        "GitHub URL of the file being run": github_file_url,
        "GitHub URL of the full source code": github_source_url,
        "Status Code": "Success"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
