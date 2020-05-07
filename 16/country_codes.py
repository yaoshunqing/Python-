# encoding= utf-8  
# @Time : 2020/5/7 16:09 
# @Author : Yao
# @File : country_codes.py 
# @Software: PyCharm

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items() :
        if name == country_name:
            return code
    return None