from modules.parser import parse, get_max_page
from modules.dumper import dump_data
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import os

ENV_PATH = ".env"
load_dotenv(ENV_PATH)

URL = os.getenv("BLOG_URL")
OUTPUT_FILE = os.getenv("OUTPUT_FILE")
SHEET_NAME = os.getenv("SHEET_NAME")
WORKERS = int(os.getenv("WORKERS"))

BLOGS = list()

def run(url):
    global BLOGS
    max_page = get_max_page(url)

    blogs = list()
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        threads = list()

        for i in range(1, max_page+1):
            url_ = url + f"page/{i}/"
            threads.append(executor.submit(parse, url_, i))
        
        for future in as_completed(threads):
            try:
                result = future.result()

                if not result:
                    continue
                blogs += result

            except Exception as e:
                print(f"Error processing: {e}")
    
    BLOGS = sorted(blogs, key = lambda x: x['Page Number'])

run(URL)
dump_data(BLOGS, OUTPUT_FILE, SHEET_NAME)