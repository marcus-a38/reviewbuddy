######################################################################
#                                                                    #
#      Copyright © 2023 Marcus Antonelli. All Rights Reserved.       #
#                                                                    # 
#      Licensed under the GNU General Public License v3, a free      #
#     copyleft license with minimal stipulations and limitations.    #
#                Obtain a copy of the license below:                 #
#                                                                    #
#             http://gnu.org/licenses/gpl-3.0.en.html                #
#                                                                    #
######################################################################
#                            DISCLAIMER                              #
######################################################################
#                                                                    #
#        This software, like any other GPLv3 licensed works,         #
#    is provided "as is". There is no warranty, either expressed     #
#      or implied. Unless required by law or explicity written,      #
#   the author of this software is under no obligation to accept     #
#       liability for damages caused by the usage of this file.      #
#                                                                    #
#   See the full license for further information and more detailed   #
#                     explanations and language.                     #
#                                                                    #
######################################################################

""" 
Provides basic support for JSON "bookmarking" of search queries + results.
Reduces excessive and repetitive scraping/analysis of a user's locations of interest.
"""

import json
from paths import BOOKMARKS_PATH


def _concat_title_zip(title: str, zipcode: str): # include zip in bookmark title, e.g. 'McDonald's | 00000'
    return title + " | " + zipcode


def verify(should_exist: bool): # verify that a bookmark does or doesn't exist

    def decorator(func):

        def inner(*args):

            title = _concat_title_zip(args[0], args[1])
            data = load_bms()

            if data == "Fail":
                return
                
            if not should_exist and title in data:
                print("Bookmark action failed, existing bookmark already exists.")
                return 
            
            elif should_exist and not title in data:
                print("Bookmark action failed, no existing bookmark could be found.")
                return
            
            print("Trying...")

            return func(*args)
        return inner
    return decorator


def load_bms() -> dict:

    try:
        with open(BOOKMARKS_PATH, 'r') as jfile:
            return json.load(jfile)
        
    except json.decoder.JSONDecodeError:
        print("JSON format is invalid... Scrubbing contents.")
        with open(BOOKMARKS_PATH, 'w') as jfile:
            jfile.write("{ }")
            return "Fail"


@verify(should_exist=False)
def add_bm(title: str, zipcode: str, data: dict):

    fulltitle = _concat_title_zip(title, zipcode)
    bookmarks = load_bms()

    with open(BOOKMARKS_PATH, 'r+') as jfile:
        try:
            bookmarks[fulltitle] = data
            json.dump(bookmarks, jfile, indent=4)

        except Exception as err:
            print("Error adding bookmark ->", err)
            return

    print("Add bookmark success!")


@verify(should_exist=True)
def rem_bm(title: str, zipcode: str):

    fulltitle = _concat_title_zip(title, zipcode) 
    bookmarks = load_bms()

    with open(BOOKMARKS_PATH, 'w') as jfile:
        try:
            del bookmarks[fulltitle]
            json.dump(bookmarks, jfile, indent=4)

        except Exception as err:
            print("Error removing bookmark. ->", err)
            return

    print("Remove bookmark success!")


@verify(should_exist=True)
def get_bm(title: str, zipcode: str) -> dict:

    title = _concat_title_zip(title, zipcode)
    bookmarks = load_bms()

    try:
        return bookmarks[title]
    
    except Exception as err:
        print("Error retrieving bookmark ->", err)
