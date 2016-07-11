#!/usr/bin/env python
# encoding: utf-8

"""
@author: lizhifeng
@contact: lizhifeng2009@126.com
@site: 
@file: char_covert.py
@time: 6/2/16 2:29 PM
"""

from __init__ import *


def is_full_width_char(c):
    if (u'\uff01' < c < u'\uff5e') or c == u'\u3000':
        return True
    else:
        return False


def is_half_width_char(c):
    if u'\u0019' < c < u'\u007e':
        return True
    else:
        return False


def full_width_to_half_width(fc):

    """ differ between full width char and half_width_char """
    diff = 65248

    """ fc in a full width char , not whitespace """
    if u'\uff01' < fc < u'\uff5e':

        half_width_integer = ord(fc) - diff

        return unichr(half_width_integer)

    """ fc is whitespace """
    if u'\u3000' == fc:
        return u'\u0020'

    """ fc is not a full-width char """
    return fc


def half_width_to_full_width(hc):

    """ differ between full width char and half_width_char """
    diff = 65248

    """ fc in a half width char , not whitespace """
    if u'\u0020' < hc < u'\u007e':

        half_width_integer = ord(hc) + diff

        return unichr(half_width_integer)

    """ fc is whitespace """
    if u'\u0020' == hc:
        return u'\u3000'

    """ fc is not half width char """
    return hc


def convert_to_half_width_string(s):
    half_width_char_list = []
    for c in s:
        half_width_char_list.append(full_width_to_half_width(c))

    half_width_string = u"".join(half_width_char_list)
    return half_width_string


def detect_char_type(c):
    if is_full_width_char(c):
        return FULL_WIDTH_CHAR

    if is_half_width_char(c):
        return HALF_WIDTH_CHAR

    if c == u'“' or c == u'”':
        return CHINESE_DOUBLE_QUOTATION

    if c == u'’' or c == u'‘':
        return CHINESE_SINGLE_QUOTATION

    ''' Dashes, connection number, hyphen, minus '''
    if (u'\u2010' <= c <= u'\u2015') or c == u'\u0096' or c == u'\u0097' or c == u'\u00ac':
        return DASH

    ''' superscript '''
    if (u'\u00B0' <= c <= u'\u00BF') or (u'\u2070' <= c <= u'\u209f'):
        return SCRIPT

    return UNKNOWN


def convert_to_legal_char(c):
    char_type = detect_char_type(c)

    if char_type == FULL_WIDTH_CHAR:
        return convert_to_half_width_string(c)

    if char_type == HALF_WIDTH_CHAR:
        return c

    if char_type == CHINESE_SINGLE_QUOTATION:
        return '\''

    if char_type == CHINESE_DOUBLE_QUOTATION:
        return '\"'

    if char_type == DASH:
        return '-'

    if char_type == SCRIPT:
        return ' '

    if UNKNOWN:
        return None

    return None


if __name__ == '__main__':

    print full_width_to_half_width(u'ｃ')
    print half_width_to_full_width(u'c')
    print half_width_to_full_width(u'‘')
    print full_width_to_half_width(u'　') == u''

    print convert_to_half_width_string(u"asdｓｄxxwsd ")
