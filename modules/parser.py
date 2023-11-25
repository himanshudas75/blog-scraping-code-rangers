from bs4 import BeautifulSoup
import subprocess as sb
from .extract_data import get_blog_date, get_blog_image, get_blog_likes, get_blog_title


def get_page_data(url):
    result = sb.run(['curl', '-i', '-L', url], capture_output=True, text=True)
    soup = BeautifulSoup(result.stdout, 'html.parser')
    return soup

def get_max_page(url):
    soup = get_page_data(url)
    pagination_div = soup.find("div", class_ = "pagination")
    if not pagination_div:
        return 0
    page_number_last = pagination_div.find_all("a", class_ = "page-numbers")[-2]
    page_number_last = int(page_number_last.text)
    return page_number_last

def parse(url, index):
    soup = get_page_data(url)
    blogs = soup.find_all("article", class_ = "blog-item")
    
    all_blogs = list()

    if not blogs:
        return all_blogs
    
    for blog in blogs:
        title = get_blog_title(blog)
        date = get_blog_date(blog)
        image = get_blog_image(blog)
        likes = get_blog_likes(blog)

        blog_details = {
            "Page Number": index,
            "Title": title,
            "Date": date,
            "Image": image,
            "Likes": likes
        }

        all_blogs.append(blog_details)
    
    return all_blogs