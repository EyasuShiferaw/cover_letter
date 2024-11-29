from datetime import datetime
import random

def today_date() -> str:       
    """
    Get today's date in the format of "Month Day, Year"
    """
    today = datetime.now()

    formatted_date = today.strftime("%B %d, %Y")

    return formatted_date