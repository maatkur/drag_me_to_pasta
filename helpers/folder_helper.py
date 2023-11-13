import os


class FolderHelper:

    @staticmethod
    def check_exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def create(folder_name) -> None:
        os.mkdir(folder_name)
