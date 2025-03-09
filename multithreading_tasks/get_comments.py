import requests
import threading


def fetch_comments(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nComments for post {post_id}: ")
        for comment in data:
            print(comment['body'])
    else:
        print(f"Failed to fetch comments for post {post_id}. Status code: {response.status_code}")


post_ids = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    threads = []
    for post_id in post_ids:
        thread = threading.Thread(target=fetch_comments, args=(post_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads have finished.")