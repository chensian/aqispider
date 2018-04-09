#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 0:04 
# @Author  : chesian
# @Site    : 
# @File    : Agents.py
# @Software: PyCharms

# Crawl responsibly by identifying yourself (and your website) on the user-agent
import codecs

Agents = [agent.strip() for agent in codecs.open("user-agent", "r").readlines()]

