# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку
# по group/number і повернення значення timingExbytes/incoming результат
# виведіть у консоль через логер на рівні інфо

import os
from pathlib import Path
import logging
import xml.etree.ElementTree as ET


def search_group_by_number(xml_file, group_number):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(group_number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        logging.info(f"Group {group_number} incoming: {incoming.text}")
                        return incoming.text

        logging.info(f"Group {group_number} not found or has no incoming value.")
        return None

    except ET.ParseError as e:
        logging.error(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None


xml_file_path = os.path.join(Path(__file__).parent, 'groups.xml')
group_number_to_search = 4

search_group_by_number(xml_file_path, group_number_to_search)
