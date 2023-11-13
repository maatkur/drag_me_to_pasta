import xml.etree.ElementTree as ET
from helpers.date_helpers import DateHelper


class XmlReaderHelper:

    @staticmethod
    def retrieve_xml_data(xmls: list) -> list:
        # Parse do arquivo XML
        xml_data = []

        for xml in xmls:
            tree = ET.parse(xml)
            root = tree.getroot()

            # Namespace
            ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

            # Acessando CNPJ do emitente
            enrollment_number = root.find(".//nfe:emit/nfe:CNPJ", namespaces=ns).text.strip()

            # Acessando data de emissão da NF
            folder = root.find(".//nfe:ide/nfe:dhEmi", namespaces=ns).text.strip()

            # Acessando a chave XML da NF
            xml_key = root.find(".//nfe:infNFe", namespaces=ns).get("Id")[3:]

            # Acessando o número da NF
            xml_number = root.find(".//nfe:ide/nfe:nNF", namespaces=ns).text.strip()

            xml_data.append({
                "enrollment_number": enrollment_number,
                "folder": DateHelper.convert_default(folder),
                "xml_key": xml_key,
                "xml_number": xml_number
            })

        return xml_data
