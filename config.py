from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN""5791501037:AAEAe93nq-e5PZ-UJc_J6Who8GX84xMzdtg")
API_ID = int(getenv("API_ID", "14320673"))
API_HASH = getenv("API_HASH""f57f42e575437906b2be2e05f85ea977")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5782714204").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1930739461").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "1001466357800"))
MUSIC_BOT_NAME = getenv("SHIVUXMUSIC7X")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("SHIVU7X")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Shailendra34/Hero-OP"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = "SHIVAM_AGRO"
else:
    SUPPORT_CHANNEL = str(getenv("SHIVAM_AGRO"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = "AGRICULTURA_QUEEN"
else:
    SUPPORT_GROUP = str(getenv("AGRICULTURA_QUEEN"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str("BQCDmGUG2Jim8SwKmwu134pGPrcXl4uItdABZaTHIAWuTUTpDVhufLDk2fYz0T1Gksakbuu-QwCKff4aPUhTVHtxJ6aQKpu5757QY-U5odmlPOfmk5jEz8fWB8AxIcNOWSxV5wXv1h-agugSW4x5-3hFVWseYjcLtpcOPrkV3Sw5bpoKXc2Oxfp4Lakp4m9Uw4OR84XMZkmxPUv8AVrVjMfLRDPjDU9eFHioPtgxWg7FtB8243U_PVMnmi6WLWqj7SIzEqXszUSvNWeohXV62uojW-OQX_P-RFiZWH_Lhrd1oy8f5tTSUmUBadW4QdTlZ1xHlK3Yx50XAc_k0wzgiZ4DAAAAAThX180A")
else:
    STRING1 = str(getenv("BQCDmGUG2Jim8SwKmwu134pGPrcXl4uItdABZaTHIAWuTUTpDVhufLDk2fYz0T1Gksakbuu-QwCKff4aPUhTVHtxJ6aQKpu5757QY-U5odmlPOfmk5jEz8fWB8AxIcNOWSxV5wXv1h-agugSW4x5-3hFVWseYjcLtpcOPrkV3Sw5bpoKXc2Oxfp4Lakp4m9Uw4OR84XMZkmxPUv8AVrVjMfLRDPjDU9eFHioPtgxWg7FtB8243U_PVMnmi6WLWqj7SIzEqXszUSvNWeohXV62uojW-OQX_P-RFiZWH_Lhrd1oy8f5tTSUmUBadW4QdTlZ1xHlK3Yx50XAc_k0wzgiZ4DAAAAAThX180A. "))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
