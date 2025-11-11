import requestsimport requests

import osimport os





def send_telegram_alert(message):def send_telegram_alert(message):

    try:    try:

        # Use environment variables only - no hardcoded tokens        # Use environment variables only - no hardcoded tokens

        bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')        bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')

        chat_id = os.environ.get('TELEGRAM_CHAT_ID')        chat_id = os.environ.get('TELEGRAM_CHAT_ID')



        # Check if environment variables are set        # Check if environment variables are set

        if not bot_token or not chat_id:        if not bot_token or not chat_id:

            print("Telegram credentials not configured. Skipping notification.")            print("Telegram credentials not configured. Skipping notification.")

            return False            return False



        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

        payload = {        payload = {

            'chat_id': chat_id,            'chat_id': chat_id,

            'text': message,            'text': message,

            'parse_mode': 'HTML'            'parse_mode': 'HTML'

        }        }



        print(f"Sending to Telegram: {url}")        print(f"Sending to Telegram: {url}")

        print(f"Message: {message}")        print(f"Message: {message}")



        response = requests.post(url, data=payload)        response = requests.post(url, data=payload)

        print(f"Response status: {response.status_code}")        print(f"Response status: {response.status_code}")

        print(f"Response text: {response.text}")        print(f"Response text: {response.text}")



        return response.status_code == 200        return response.status_code == 200



    except Exception as e:    except Exception as e:

        print(f"Telegram error: {e}")        print(f"Telegram error: {e}")

        return False        return False