from config import GROUPME_API_TOKEN, GROUPME_BOT_ID
from groupme import GroupMeAPI

def main():
    # Initialize the GroupMe API
    api = GroupMeAPI(GROUPME_API_TOKEN)

    # Send a test message
    message = "Hello from my bot!"
    response = api.send_message(message)

    # Print the response
    print(response)

if __name__ == "__main__":
    main()