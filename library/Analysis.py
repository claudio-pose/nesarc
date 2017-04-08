# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:58:58 2017

@author: Claudio Pose
"""

class Analysis:
    """
    TODO: DOCSTRING
    """
    df_helper = None
    freq = dict()
    percent = dict()

    def __init__(self, *args, **kwargs):
        self.df_helper = kwargs.get('df_helper', None)
