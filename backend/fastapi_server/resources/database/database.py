# This file includes and maps all apps databases spaces.

from typing import TypedDict

from fastapi_server.apps.feature_flags.database.postgres import (
    get_feature_flags_db,
    FeatureFlagsDB,
)
from fastapi_server.apps.users.database.postgres import get_user_db, UsersDB


class Databases(TypedDict):
    feature_flags: FeatureFlagsDB
    users: UsersDB


def get_databases(db_session) -> Databases:
    feature_flags: FeatureFlagsDB = get_feature_flags_db(db_session)
    users: UsersDB = get_user_db(db_session)
    return {
        "feature_flags": feature_flags,
        "users": users,
    }
