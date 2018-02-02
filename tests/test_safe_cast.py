#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace safe_cast

import pytest

from safe_cast import (
    safe_float,
    safe_str,
    safe_dict,
    safe_int,
    safe_cast,
    safe_fraction
)


def test_safe_str():
    # test type:
    assert isinstance(safe_str(0), str)
    assert isinstance(safe_str(0.0), str)
    assert isinstance(safe_str('0'), str)
    # test str cast:
    assert safe_str('') == ''
    assert safe_str('Hello Jeff') == 'Hello Jeff'
    assert safe_str('@%#$%^&*') == '@%#$%^&*'
    assert safe_str(None) == ''
    # test numeric cast:
    assert safe_str(0) == '0'
    assert safe_str(10) == '10'
    assert safe_str(-1) == '-1'
    assert safe_str(10.52) == '10.52'
    assert safe_str(-1.32) == '-1.32'
    assert safe_str('Noël') == 'Noël'
    assert safe_str('Русский') == 'Русский'


def test_safe_int():
    # test type:
    assert isinstance(safe_int(0), int)
    assert isinstance(safe_int(0.0), int)
    assert isinstance(safe_int('0'), int)
    # test numeric cast:
    assert safe_int(0) == 0
    assert safe_int(10) == 10
    assert safe_int(-1) == -1
    assert safe_int(10.5) == 10
    # test str cast:
    assert safe_int('10') == 10
    assert safe_int('-1') == -1
    assert safe_int('1,000.5') == 1000
    # test default param:
    assert safe_int('###', 256) == 256
    # test exception raising:
    with pytest.raises(ValueError, message='Expecting ValueError to be raised') as excinfo:
        safe_int('##')
    assert '"Could not convert string to float: \'##\'", "##", str to float' \
           in str(excinfo.value)


def test_safe_float():
    # test type:
    assert isinstance(safe_float(0), float)
    assert isinstance(safe_float(0.0), float)
    assert isinstance(safe_float('0.0'), float)
    assert isinstance(safe_float('1,252.5'), float)
    # test numeric cast:
    assert safe_float(0) == 0
    assert safe_float(10.52) == 10.52
    assert safe_float(-1) == -1
    assert safe_float(-1.32) == -1.32
    assert safe_float(10.5) == 10.5
    # test str cast:
    assert safe_float('1') == 1
    assert safe_float('-1.32') == -1.32
    assert safe_float('1,152.15') == 1152.15
    # test num values after period:
    assert safe_float(-1.321321, ndigits=6) == -1.321321
    assert safe_float('-1.321321', ndigits=6) == -1.321321
    # test default param:
    assert safe_float('###', default=1.1) == 1.1
    # test exception raising:
    with pytest.raises(ValueError, message='Expecting ValueError to be raised') as excinfo:
        safe_float('##')
    assert '"Could not convert string to float: \'##\'", "##", str to float' \
           in str(excinfo.value)


def test_safe_fraction():
    assert safe_fraction("1/2") == 0.5
    assert safe_fraction("1/3") == 0.33
    assert safe_fraction("1/3", ndigits=6) == 0.333333
    assert safe_fraction("-3 1/6", ndigits=4) == -3.1667
    assert safe_fraction(1/3, ndigits=6) == 0.333333


def test_safe_dict():
    # test basic dict:
    assert isinstance(safe_dict({'key': 'value'}), dict)
    # test fail:
    with pytest.raises(TypeError, message='Expecting TypeError because passing not iterable value.') as excinfo:
        assert safe_dict(5)
    assert '"\'int\' object is not iterable", "5", int to dict' \
           in str(excinfo.value)

    with pytest.raises(ValueError, message='Expecting ValueError because str not castable to dict.') as excinfo:
        assert safe_dict('Hello Jeff')
    assert '"Dictionary update sequence element #0 has length 1; 2 is required", "Hello Jeff", str to dict' \
           in str(excinfo.value)


def test_None():
    assert safe_int(None) == 0
    assert safe_int(None, 7) == 7
    assert safe_float(None) == 0.0
    assert safe_float(None, default=7.7) == 7.7
    assert safe_dict(None) == {}
    assert safe_dict(None, {'Jeff': 'Tanner'}) == {'Jeff': 'Tanner'}
    assert safe_str(None) == ''
    assert safe_str(None, "stas") == "stas"
    assert safe_cast(None, str) is None
    assert safe_cast(None, str, default="TuliTuliTuli") == "TuliTuliTuli"


def test_empty():
    assert safe_int("") == 0
    assert safe_int('') == 0
    assert safe_int('', 7) == 7
    assert safe_float("") == 0.0
    assert safe_float('') == 0.0
    assert safe_float('', default=7.7) == 7.7
    assert safe_dict("") == {}
    assert safe_dict('') == {}
    assert safe_dict('', {'Max': 'Ohad'}) == {'Max': 'Ohad'}
