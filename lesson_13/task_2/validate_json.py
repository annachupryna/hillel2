# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import os
import json
import logging


def validate_json_files(directory, log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path) and filename.endswith('.json'):
            try:
                with open(file_path, 'r') as f:
                    json.load(f)
            except (json.JSONDecodeError, OSError) as e:
                logging.error(f"Invalid JSON in file: {file_path}. Error: {e}")


directory_path = os.path.dirname(os.path.abspath(__file__))
log_file_path = 'json__Chupryna.log'

validate_json_files(directory_path, log_file_path)
