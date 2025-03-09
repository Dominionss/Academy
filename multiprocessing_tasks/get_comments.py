from multiprocessing import Process
from multithreading_tasks import fetch_comments

post_ids = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    processes = []
    for post_id in post_ids:
        process = Process(target=fetch_comments, args=(post_id,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes have finished.")


