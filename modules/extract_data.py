import re

def get_blog_title(blog):
    heading = blog.find("h6")
    if not heading:
        return ""
    heading = heading.text
    return heading

def get_blog_date(blog):
    blog_details = blog.find("div", class_ = "blog-detail")
    if not blog_details:
        return ""
    date = blog_details.find_all("div", class_ = "bd-item")[0]
    if not date:
        return ""
    date = date.text
    return date

def get_blog_image(blog):
    image_div = blog.find("div", class_ = "img")
    if not image_div:
        return ""
    image_anchor = image_div.find("a")
    if not image_anchor:
        return ""
    try:
        image_url = image_anchor.get("style")
        if "url" in image_url:
            match = re.search(r'url\((.*?)\)', image_url)
            if match:
                image_url = match.group(1)
        else:
            image_url = image_anchor.get("data-bg")
        if not image_url:
            image_url = ""
    except:
        image_url = ""

    return image_url

def get_blog_likes(blog):
    content_div = blog.find("div", class_ = "content")
    if not content_div:
        return ""
    like_anchor = content_div.find("a", class_ = "zilla-likes")
    if not like_anchor:
        return ""
    like_text = like_anchor.text
    try:
        likes = int(re.findall("\d+", like_text)[0])
    except:
        return ""
    return likes