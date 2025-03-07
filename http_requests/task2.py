import requests
import json


REPO_OWNER = "octocat"
REPO_NAME = "Spoon-Knife"
ISSUE_NUMBER = 1

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{ISSUE_NUMBER}/comments"

headers = {
    "Accept": "application/vnd.github.v3+json"
}


def fetch_comments(url, headers):
    """Fetches all comments from a GitHub issue or pull request."""
    comments = []
    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        comments.extend(response.json())

        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            url = None

    return comments


def save_comments_to_json(comments, filename):
    """ Saves comments to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(comments, file, indent=4)
    print(f"Saved {len(comments)} comments to {filename}")

def main():
    comments = fetch_comments(url, headers)

    if comments:
        output_file = f"issue_{ISSUE_NUMBER}_comments.json"
        save_comments_to_json(comments, output_file)

        with open(f"issue_{ISSUE_NUMBER}_comments.json", "r", encoding='utf-8') as file:
            data = json.load(file)

        for user in data:
            print(f"{user["user"]["login"]} - {user['body']}")
    else:
        print("No comments found.")

if __name__ == "__main__":
    main()

