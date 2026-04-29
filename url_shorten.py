import json
import os

_save_urls_path = os.path.join(os.path.dirname(__file__), "data", "saved_urls.json")

# with open('python_dictionary.json','r+') as f:
#     dic = json.load(f)
#     dic.update(new_dictionary)
#     json.dump(dic, f)

def get_url(key):
    with open(_save_urls_path,'r') as f:
        urls = json.load(f)
        if key in urls:
            return urls[key]
        else:
            raise KeyError
            
# Currently reads and writes all keys, can be made more i/o efficient by 
# searching through the values and appending new values to the end
def save_url(key, url):
    with open(_save_urls_path,'r+') as f:
        urls = json.load(f)
        # if larger than expected usage, stop saving urls
        if len(urls) > 1000:
            raise ValueError
        if key in urls:
            raise KeyError
        else:
            f.seek(0)
            if "://" not in url:
                url = "https://" + url
            urls[key] = url
            json.dump(urls, f, indent=4)
