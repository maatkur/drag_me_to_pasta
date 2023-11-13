import shutil
import constants


class FileHelper:

    @staticmethod
    def move_file(file: str, destiny: str) -> None:

        shutil.move(f'{constants.paths["user_downloads_folder"]}\\{file}.xml', destiny)
