from components.dialogs import Dialogs
import constants
from helpers.file_helpers import FileHelper
from helpers.folder_helper import FolderHelper
from helpers.xml_finder_helper import XmlFinderHelper
from helpers.xml_reader_helper import XmlReaderHelper


def main():
    xmls = XmlFinderHelper.find_xmls()
    xmls_data = XmlReaderHelper.retrieve_xml_data(xmls)

    for xml in xmls_data:
        destiny_path = f'{constants.paths["xmls_destiny_folder"]}{xml["enrollment_number"]}\\autorizados\\{xml["folder"]}'

        try:
            if not FolderHelper.check_exists(destiny_path):
                FolderHelper.create(destiny_path)

            FileHelper.move_file(xml["xml_key"], f"{destiny_path}\\{xml['xml_key']}-procNFe.xml")
            Dialogs.success_dialog()
        except Exception as e:
            Dialogs.fail_dialog(f"Erro ao copiar o xml da NF n°{xml['xml_number']}: {str(e)}")


if __name__ == "__main__":
    main()
