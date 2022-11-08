import re

'''
Class to clean HTML Source Code
@author Jackson Crawford
'''
class HTML_Cleaner():
    def __init__(self):
        pass
    
    # Method to split a soup on a given tag
    def split_on_tag(self, soup, tag):
        regex = "<" + tag + "(.*?)>(.*?)</" + tag + ">"
        rows = re.findall(regex, str(soup))
        return rows

    # Method to remove a tag pair
    def remove_tag(self, soup, tag):
        regex_open = "<" + tag + "(.*?)>"
        regex_close = "</" + tag + ">"
        soup = re.sub(regex_open, "", str(soup))
        soup = re.sub(regex_close, "", str(soup))
        return soup

    # Method to remove anything between two flags
    def remove(self, soup, re_open, re_close):
        regex = re_open + ".*?" + re_close
        soup = re.sub(regex, "", str(soup))
        return soup

    # Method to replace tag (todd_is_cool_xy7 is the new string idk why)
    def replace_tag(self, soup, tag, todd_is_cool_xy7):
        soup = re.sub(tag, todd_is_cool_xy7, str(soup))
        return soup
