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

import os

DATA_DIRECTORY = os.path.join(os.getcwd(), "data")
DRIVER_DIRECTORY = os.path.join(os.getcwd(), "driver")
NLTK_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "nltk_data")
BOOKMARKS_PATH = os.path.join(DATA_DIRECTORY, "bookmarks.json")
LOGS_PATH = os.path.join(DATA_DIRECTORY, "temp.log")
