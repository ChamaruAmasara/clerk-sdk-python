"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateJWTTemplateClaimsTypedDict(TypedDict):
    r"""JWT template claims in JSON format"""
    
    

class UpdateJWTTemplateClaims(BaseModel):
    r"""JWT template claims in JSON format"""
    
    

class UpdateJWTTemplateRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    r"""JWT template name"""
    claims: NotRequired[UpdateJWTTemplateClaimsTypedDict]
    r"""JWT template claims in JSON format"""
    lifetime: NotRequired[Nullable[float]]
    r"""JWT token lifetime"""
    allowed_clock_skew: NotRequired[Nullable[float]]
    r"""JWT token allowed clock skew"""
    custom_signing_key: NotRequired[bool]
    r"""Whether a custom signing key/algorithm is also provided for this template"""
    signing_algorithm: NotRequired[Nullable[str]]
    r"""The custom signing algorithm to use when minting JWTs"""
    signing_key: NotRequired[Nullable[str]]
    r"""The custom signing private key to use when minting JWTs"""
    

class UpdateJWTTemplateRequestBody(BaseModel):
    name: Optional[str] = None
    r"""JWT template name"""
    claims: Optional[UpdateJWTTemplateClaims] = None
    r"""JWT template claims in JSON format"""
    lifetime: OptionalNullable[float] = UNSET
    r"""JWT token lifetime"""
    allowed_clock_skew: OptionalNullable[float] = UNSET
    r"""JWT token allowed clock skew"""
    custom_signing_key: Optional[bool] = None
    r"""Whether a custom signing key/algorithm is also provided for this template"""
    signing_algorithm: OptionalNullable[str] = UNSET
    r"""The custom signing algorithm to use when minting JWTs"""
    signing_key: OptionalNullable[str] = UNSET
    r"""The custom signing private key to use when minting JWTs"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["nullableOptional", "optional"]
        nullable_fields = ["nullableRequired", "nullableOptional"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        

class UpdateJWTTemplateRequestTypedDict(TypedDict):
    template_id: str
    r"""The ID of the JWT template to update"""
    request_body: NotRequired[UpdateJWTTemplateRequestBodyTypedDict]
    

class UpdateJWTTemplateRequest(BaseModel):
    template_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the JWT template to update"""
    request_body: Annotated[Optional[UpdateJWTTemplateRequestBody], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
