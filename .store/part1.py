#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QSystemTrayIcon, QMenu, QComboBox, QDialog, QMenuBar, QFileDialog,
                             QTextEdit, QListWidget, QCheckBox, QMessageBox, QProgressBar)
from PyQt6.QtCore import Qt, QRect, QPropertyAnimation
from PyQt6.QtGui import QAction, QIcon, QColor
import PyQt6.QtGui
import sys
import webbrowser
import os
from pathlib import Path
import re
import pyautogui as pag
import requests
from bs4 import BeautifulSoup
import urllib3
from zhconv import convert
import loc_reg
import jieba.posseg as pseg
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
import pandas as pd
import openpyxl
import nltk
import logging
import datetime as dt
import importlib
importlib.reload(sys)

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("orange.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action3 = QAction("📰 Analyse news!")
menu.addAction(action3)

action6 = QAction("🗞️ Fetch news!")
menu.addAction(action6)

action4 = QAction("⚙️ Preferences")
menu.addAction(action4)

menu.addSeparator()

action8 = QAction("📐 Default size!")
menu.addAction(action8)

action9 = QAction("🗑️ Totally clean!")
menu.addAction(action9)

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
button_action = QAction("&Analyse news!")
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(button_action)