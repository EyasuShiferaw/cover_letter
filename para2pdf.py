from datetime import datetime
import random

def today_date() -> str:       
    """
    Get today's date in the format of "Month Day, Year"
    """
    today = datetime.now()
    formatted_date = today.strftime("%B %d, %Y")
    return formatted_date

def random_salutation() -> str:
   """
   Get a random salutation
   """      
   temp = ["Sincerely,", "Regards,", "Best,", "Respectfully,", "Thank you,", "Thank you for your consideration,"]
   return (random.choice(temp))    


