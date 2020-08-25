"""
pygluu.containerlib.validators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains helpers to validate things.
"""

from typing import NoReturn

from .constants import PERSISTENCE_TYPES
from .constants import PERSISTENCE_LDAP_MAPPINGS


class ValidationError(Exception):
    pass


def validate_persistence_type(type_: str) -> NoReturn:
    if type_ not in PERSISTENCE_TYPES:
        types = ", ".join(PERSISTENCE_TYPES)

        raise ValidationError(
            f"Unsupported GLUU_PERSISTENCE_TYPE value {type_}; "
            f"please choose one of {types}"
        )


def validate_persistence_ldap_mapping(type_: str, ldap_mapping: str) -> NoReturn:
    if type_ == "hybrid" and ldap_mapping not in PERSISTENCE_LDAP_MAPPINGS:
        mappings = ", ".join(PERSISTENCE_LDAP_MAPPINGS)

        raise ValidationError(
            f"Unsupported GLUU_PERSISTENCE_LDAP_MAPPING value {ldap_mapping}; "
            f"please choose one of {mappings}"
        )
