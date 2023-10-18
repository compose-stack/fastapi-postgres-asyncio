from typing import List

from fastapi import APIRouter, Depends

from ..database.postgres import FeatureFlagsDB, get_feature_flags_db
from ..schemas import FeatureFlagRead

router = APIRouter(
    prefix="/feature-flags",
    tags=["feature-flags"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/feature-flags",
    response_description="Get all feature flags",
    response_model=List[FeatureFlagRead],
)
async def get_feature_flags(db: FeatureFlagsDB = Depends(get_feature_flags_db)):
    feature_flags = await db.get_feature_flags()
    import pprint

    print("====================+++++++++++++++++++++")
    pprint.pprint(feature_flags)
    print("====================+++++++++++++++++++++")
    return feature_flags
