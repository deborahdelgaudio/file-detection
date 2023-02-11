# File detection
verifies the total number of virus detection for a list of hashes provided
_______

## RUN
The project is runnable if python is available on the system. After cloning the repository create the environment and activate it running the following commands:
```python
python -m virtualenv ./venv
source venv/bin/activate
```
Install dependencies with pip:
```python
pip install -r requirements.txt
```
Create the input file that contains the list of hashes that should be analysed, an example could be found in `input-trial.json`.
Create a `.env` file with the requested environment variables, check the related section for more information.
Run the code with:
```python
python main.py
```
The results will be available inside path specified in `OUTPUT_FILE_PATH` variable.

## TESTS
Add the `src/` directory to the `PYTHONPATH` variables and run tests with the command
````python
pytest -v
````

## ENVIRONMENT VARIABLES
This project use the VirusTotal API to detect suspicious malware from files, in order to run the code you must have an APIKEY.
Check the official documentation: https://developers.virustotal.com/reference/getting-started

|       Name        |           Value            |
|:-----------------:|:--------------------------:|
| VIRUSTOTAL_APIKEY |           string           |
 |  INPUT_FILE_PATH  |      input-trial.json      |
 | OUTPUT_FILE_PATH  |        output.json         |

The variables should be defined as env variables using an .env file.

[Env example](/.env.example)