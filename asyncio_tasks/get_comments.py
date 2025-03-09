import aiohttp
import asyncio


async def fetch_comments(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(f"\nComments for post {post_id}: ")
                for comment in data:
                    print(comment['body'])
            else:
                print(f"Failed to fetch comments for post {post_id}. Status code: {response.status}")


async def main():
    post_ids = [1, 2, 3, 4, 5]
    tasks = [fetch_comments(post_id) for post_id in post_ids]

    await asyncio.gather(*tasks)
    print("All tasks have finished.")


if __name__ == "__main__":
    asyncio.run(main())