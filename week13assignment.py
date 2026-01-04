import requests
import json

def get_jokes():
    url = "https://official-joke-api.appspot.com/jokes/programming/ten"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Could not get data from API.")
            return

        jokes = response.json()

        count = int(input("Enter number of jokes (1-10): "))

        if count < 1 or count > 10:
            print("Number must be between 1 and 10.")
            return

        selected = jokes[:count]

        print("\nProgramming Jokes:")
        for i in range(len(selected)):
            print(f"\nJoke {i + 1}")
            print(selected[i]["setup"])
            print(selected[i]["punchline"])

        with open("my_jokes.json", "w", encoding="utf-8") as file:
            json.dump(selected, file, indent=4)

        print("\nJokes saved to my_jokes.json")

    except requests.exceptions.RequestException:
        print("No internet connection.")
    except ValueError:
        print("Invalid input.")


get_jokes()
