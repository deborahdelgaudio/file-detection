# File detection
verifies the total number of virus detection for a list of hashes provided
_______

## ENVIRONMENT VARIABLES
This project use the VirusTotal API to detect suspicious malware from files, in order to run the code you must have an APIKEY.
Check the official documentation: https://developers.virustotal.com/reference/getting-started

| Name  | Value  |
|:-----:|:------:|
| VIRUSTOTAL_APIKEY | string |

The variables should be defined as env variables using an .env file.

[Env example](/.env.example)