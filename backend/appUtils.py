from logger import putlog
import json, os
from fastapi.responses import JSONResponse

log = putlog(__file__)


def readFile(filename):
    content = ""

    try:
        with open(filename, 'r') as fileContent:
            content = fileContent.read()
    except Exception as e:
        log.error("{}".format(e))

    return content


def readJson(filename):
    content = {}

    try:
        content = json.loads(readFile(filename))
    except Exception as e:
        log.error("{}".format(e),exc_info=True)

    return content


def writeFile(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    status = "success"
    try:
        with open(filename, 'w') as fileSource:
            fileSource.write(content)
    except Exception as e:
        log.error("{}".format(e))
        status = "failed"

    return status


def writeJson(filename, content):
    status = "Success"

    try:
        contentDump = json.dumps(content, indent=4, sort_keys=True)
        writeFile(filename, contentDump)
    except Exception as e:
        log.error("{}".format(e))
        status = "Failed"

    return status

configFile = "config/app.setting.json"
configuration = readJson(configFile)

def createCustomResponse(content):
    response = JSONResponse(content=content)
    for headerName, headerValue in configuration["App"]["Headers"].items():
        response.headers[headerName] = headerValue
    return response

