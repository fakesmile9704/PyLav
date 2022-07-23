from __future__ import annotations

import os
import pathlib

import yaml

from pylav._logging import getLogger

LOGGER = getLogger("PyLav.Enviroment")

ENV_FILE = pathlib.Path.home() / "pylav.yaml"

if not ENV_FILE.exists():
    LOGGER.warning(
        "%s does not exist - This is not a problem if it does then the enviroment variables will be read from it.",
        ENV_FILE,
    )
    POSTGRE_PORT = os.getenv("PYLAV__POSTGRES_PORT", os.getenv("PGPORT"))
    POSTGRE_PASSWORD = os.getenv("PYLAV__POSTGRES_PASSWORD", os.getenv("PGPASSWORD"))
    POSTGRE_USER = os.getenv("PYLAV__POSTGRES_USER", os.getenv("PGUSER"))
    POSTGRE_DATABASE = os.getenv("PYLAV__POSTGRES_DB", os.getenv("PGDATABASE"))
    POSTGRE_HOST = os.getenv("PYLAV__POSTGRES_HOST", os.getenv("PGHOST"))

    REDIS_FULLADDRESS_RESPONSE_CACHE = os.getenv("PYLAV__REDIS_FULLADDRESS_RESPONSE_CACHE")

    with ENV_FILE.open(mode="w") as file:
        data = {}
        if POSTGRE_PORT:
            data["PYLAV__POSTGRES_PORT"] = POSTGRE_PORT
        if POSTGRE_PASSWORD:
            data["PYLAV__POSTGRES_PASSWORD"] = POSTGRE_PASSWORD
        if POSTGRE_USER:
            data["PYLAV__POSTGRES_USER"] = POSTGRE_USER
        if POSTGRE_DATABASE:
            data["PYLAV__POSTGRES_DB"] = POSTGRE_DATABASE
        if POSTGRE_HOST:
            data["PYLAV__POSTGRES_HOST"] = POSTGRE_HOST
        if REDIS_FULLADDRESS_RESPONSE_CACHE:
            data["PYLAV__REDIS_FULLADDRESS_RESPONSE_CACHE"] = REDIS_FULLADDRESS_RESPONSE_CACHE
        if data:
            LOGGER.debug("Creating %s with the following content: %r", ENV_FILE, data)
            yaml.safe_dump(data, file, default_flow_style=False, sort_keys=False, encoding="utf-8")

else:
    LOGGER.warning("%s exist - Enviroment variables will be read from it.", ENV_FILE)
    with ENV_FILE.open(mode="r") as file:
        data = yaml.safe_load(file.read())

        POSTGRE_PORT = data.get("PYLAV__POSTGRES_PORT") or os.getenv("PYLAV__POSTGRES_PORT", os.getenv("PGPORT"))
        POSTGRE_PASSWORD = data.get("PYLAV__POSTGRES_PASSWORD") or os.getenv(
            "PYLAV__POSTGRES_PASSWORD", os.getenv("PGPASSWORD")
        )
        POSTGRE_USER = data.get("PYLAV__POSTGRES_USER") or os.getenv("PYLAV__POSTGRES_USER", os.getenv("PGUSER"))
        POSTGRE_DATABASE = data.get("PYLAV__POSTGRES_DB") or os.getenv("PYLAV__POSTGRES_DB", os.getenv("PGDATABASE"))
        POSTGRE_HOST = data.get(" PYLAV__POSTGRES_HOST") or os.getenv(
            "PYLAV__POSTGRES_HOST", os.getenv("PYLAV__POSTGRES_HOST")
        )
        REDIS_FULLADDRESS_RESPONSE_CACHE = data.get("PYLAV__REDIS_FULLADDRESS_RESPONSE_CACHE") or os.getenv(
            "PYLAV__REDIS_FULLADDRESS_RESPONSE_CACHE"
        )
