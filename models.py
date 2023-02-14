from enum import Enum
from typing import Optional
from pydantic import BaseModel


class ImportActionEnum(int, Enum):
    INSERT = 0
    UPDATE = 1
    DELETE = 2
    NO_STATUS = 50


class AssetCSVRow(BaseModel):
    external_asset_id: str
    action: ImportActionEnum
    serial_number: str
    external_brand_id: int
    external_model_id: int


class AssetItalyCSVRow(AssetCSVRow):
    is_fiscal_device: Optional[bool] = False
    master_system_id: Optional[str]
    sogei_uid: Optional[str]
    data_type: Optional[str]  # TODO: enum
    audit_id: Optional[str]  # TODO: enum
