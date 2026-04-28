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
            
def save_url(url):
    pass
