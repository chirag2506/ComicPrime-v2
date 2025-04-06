from logger import putlog
import json, os
from difflib import SequenceMatcher

log = putlog(__file__)


def readFile(filename):
    content = ""
    try:
        with open(filename, 'r') as fileContent:
            content = fileContent.read()
    except Exception as Err:
        log.error("{}".format(Err))

    return content

def readJson(filename):
    content = {}
    try:
        content = json.loads(readFile(filename))
    except Exception as Err:
        log.error("{}".format(Err), exc_info=True)

    return content

def writeFile(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    status = "success"
    try:
        with open(filename, 'w') as fileSource:
            fileSource.write(content)
    except Exception as Err:
        log.error("{}".format(Err))
        status = "failed"

    return status

def writeJson(filename, content, sortKeys = False):
    status = "Success"
    try:
        contentDump = json.dumps(content, indent=4, sort_keys= sortKeys)
        writeFile(filename, contentDump)
    except Exception as Err:
        log.error("{}".format(Err))
        status = "Failed"

    return status

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == "__main__":
    print(similar("Amazing Spider-Man (MX)", "The Amazing Spider-Man"))
    # 0.85?
