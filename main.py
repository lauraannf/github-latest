import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    event = response.json()[0]
    event_time = event['created_at']
        # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.

    print(event_time)
    


