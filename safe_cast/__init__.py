#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace safe_cast

__title__ = 'safe-cast'
__version__ = '0.01.1'
__build__ = 0x000101
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'MIT License'

__python_required_version__ = (3, 0)


def safe_cast(val, to_type, default=None):
    """Safely cast value to type, and if failed, returned default if exists.
        If default is 'None' and and error occurs, it is raised.

    Args:
        val:
        to_type:
        default:

    Returns:

    """
    if val is None:
        return default

    try:
        return to_type(val)
    except ValueError:
        if default is None:
            raise
        return default


def safe_str(val, default=None):
    """Safely cast value to str, Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        default:

    Returns:

    """
    if val is None:
        return default if default is not None else ''

    return safe_cast(val, str, default)


def safe_float(val, ndigits=2, default=None):
    """Safely cast value to float, remove ',' if exists to ensure strs like: "1,234.5" are handled
        Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        ndigits:
        default:

    Returns:

    """
    if not val:  # None or '' or ""
        return default if default is not None else 0.0

    _val = val.replace(',', '') if type(val) == str else val
    return round(safe_cast(_val, float, default), ndigits)


def safe_int(val, default=None):
    """Safely cast value to int. Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        default:

    Returns:

    """
    if not val:  # None or '' or ""
        return default if default is not None else 0

    return safe_cast(safe_float(val, ndigits=0, default=default), int, default)


def safe_dict(val, default=None):
    """Safely cast value to dict. Optional: Pass default value. Returned if casting fails.

    Args:
        val:
        default:

    Returns:

    """
    if not val:  # None or '' or ""
        return default if default is not None else {}

    return safe_cast(val, dict, default)


def safe_smart_cast(val):
    """Safely cast value, default str

    Args:
        val:

    Returns:

    """
    to_type = type(val)
    if to_type == str:
        return safe_str(val)
    if to_type == dict:
        return safe_dict(val)
    if to_type == int:
        return safe_int(val)
    if to_type == float:
        return safe_float(val)

    return safe_str(str(val))


def safe_cost(val):
    return safe_float(val, ndigits=4)
