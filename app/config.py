class Config:
    # Application information
    APP_NAME = "Highland Highlights"

    # Paths
    APP_ICON_PATH = "assets/icons/HHS Hawks.ico"
    FILE_UPLOAD_DIRECTORY = "uploads"

    # Weather API (https://www.weatherapi.com)
    LOCATION = "gilbert"
    WEATHER_API_KEY = ""
    WEATHER_API_URL = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={LOCATION}"

    # Intervals in milliseconds
    SLIDESHOW_CYCLE_INTERVAL = 10000
    TEXT_SCROLL_INTERVAL = 20
    WEATHER_UPDATE_INTERVAL = 600000
