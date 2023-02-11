from dotenv import dotenv_values

from src.detection_client import VTDetectionClient
from src.json_adapter import read_input, write_output

config = dotenv_values(".env")

if __name__ == "__main__":
    vt_client = VTDetectionClient(api_key=config["VIRUSTOTAL_APIKEY"])
    vt_client.set_client()
    input_file = read_input(file_path=config["INPUT_FILE_PATH"])
    files_list = []
    for hash in input_file.get("hashes", []):
        stats = vt_client.get_file_analysis(hash)
        files_list.append(stats)

    write_output(file_path=config["OUTPUT_FILE_PATH"], data=files_list)
