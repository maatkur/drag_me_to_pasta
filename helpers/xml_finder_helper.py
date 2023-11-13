import os
import fnmatch
import constants


class XmlFinderHelper:

    @staticmethod
    def find_xmls() -> list:

        downloads_folder_path = constants.paths["user_downloads_folder"]

        xml_files = fnmatch.filter(os.listdir(downloads_folder_path), "*.xml")

        return [downloads_folder_path + xml for xml in xml_files]
