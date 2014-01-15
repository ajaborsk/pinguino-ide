#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import codecs

from PySide import QtGui, QtCore

from .helpers.backgrounds import BackgroundPallete
from .features.features import PinguinoFeatures
from .helpers import constants as Constants
from .helpers.dialogs import Dialogs
from .helpers.pyhton_debug import Stderr
from .helpers.config import Config
from .code_editor.autocomplete_icons import CompleteIcons
from ..frames.main import Ui_PinguinoIDE
from ..pinguino_api.pinguino import Pinguino, AllBoards


########################################################################
class PinguinoIDE(QtGui.QMainWindow, PinguinoFeatures):
    def __init__(self):
        super(PinguinoIDE, self).__init__()
        

        self.pinguinoAPI = Pinguino()
        self.configIDE = Config()
        self.ICONS = CompleteIcons()
        self.update_pinguino_paths()
        
            
        
        #self.load_theme()        
        
        self.main = Ui_PinguinoIDE()          
        self.main.setupUi(self)
        self.setWindowTitle(Constants.TAB_NAME)
        self.build_statusbar()
        
        self.PinguinoPallete = BackgroundPallete()
        self.PinguinoPallete.save_palette(self.main.centralwidget.parent())   
        self.switch_color_theme(self.configIDE.config("Main", "color_theme", True))
        
        self.__initialize_features__()
        
        self.connect_events()
        self.main.tabWidget_files.setVisible(False)
        
        setattr(self.pinguinoAPI, "_boards_", AllBoards)
        
        self.redirect_this = None

        self.main.toolBar_graphical.setVisible(False)
    
        self.update_functions()
        self.update_directives()
        self.update_variables()
        self.update_autocompleter()
        self.__update_path_files__(self.configIDE.get_path("pinguino_examples"))
        self.__update_graphical_path_files__(self.configIDE.get_path("pinguino_examples_graphical"))
        
        self.set_board()
        self.statusbar_ide(self.get_status_board())
        
        self.load_main_config()
        
        bg_color = self.configIDE.config("Styles", "background_color", "#FFFFFF")
        alternate_bg_color = self.configIDE.config("Styles", "alternate_background_color", "#DDE8FF")
        
        self.main.tableWidget_functions.setStyleSheet("QTableWidget {background-color: %s;\nalternate-background-color: %s;}"%(bg_color, alternate_bg_color))
        self.main.tableWidget_directives.setStyleSheet("QTableWidget {background-color: %s;\nalternate-background-color: %s;}"%(bg_color, alternate_bg_color))
        self.main.tableWidget_variables.setStyleSheet("QTableWidget {background-color: %s;\nalternate-background-color: %s;}"%(bg_color, alternate_bg_color))

    #----------------------------------------------------------------------
    def update_pinguino_paths(self):
        """"""
        user_sdcc_bin = self.configIDE.get_path("sdcc_bin")
        if user_sdcc_bin: self.pinguinoAPI.P8_BIN = user_sdcc_bin
        
        user_gcc_bin = self.configIDE.get_path("gcc_bin")
        if user_gcc_bin: self.pinguinoAPI.P32_BIN = user_gcc_bin
        
        pinguino_source = self.configIDE.get_path("source")
        if pinguino_source: self.pinguinoAPI.SOURCE_DIR = pinguino_source
        
        pinguino_8_libs = self.configIDE.get_path("pinguino_8_libs")
        if pinguino_8_libs: self.pinguinoAPI.P8_DIR = pinguino_8_libs
        
        pinguino_32_libs = self.configIDE.get_path("pinguino_32_libs")
        if pinguino_32_libs: self.pinguinoAPI.P32_DIR = pinguino_32_libs
                
                
        
    #----------------------------------------------------------------------
    def build_statusbar(self):
        """"""
        self.status_info = QtGui.QLabel()
        self.main.statusBar.addPermanentWidget(self.status_info, 1)    
        
        
    #----------------------------------------------------------------------
    def update_namespaces(self):
        """"""
        names = Namespaces()
        names.save_namespaces()        
        
    #----------------------------------------------------------------------
    def install_error_redirect(self):
        """"""
        sys.stderr = Stderr
        sys.stderr.plainTextEdit_output = self.main.plainTextEdit_output

    #----------------------------------------------------------------------
    def output_ide(self, *args, **kwargs):
        """"""
        for line in args:
            self.main.plainTextEdit_output.appendPlainText(line)
            
        for key in kwargs.keys():
            line = key + ": " + kwargs[key]
            self.main.plainTextEdit_output.appendPlainText(line)
            
        #self.main.plainTextEdit_output.appendPlainText(">>> ")
        
    ##----------------------------------------------------------------------
    #def clear_output_ide(self):
        #""""""
        #self.main.plainTextEdit_output.setPlainText("")
        
    #----------------------------------------------------------------------
    def statusbar_ide(self, status):
        """"""
        self.status_info.setText(status)
        
        
    #----------------------------------------------------------------------
    def set_board(self):
        """"""
        board_name = self.configIDE.config("Board", "board", "Pinguino 2550")
        for board in self.pinguinoAPI._boards_:
            if board.name == board_name:
                self.pinguinoAPI.set_board(board)
        
        arch = self.configIDE.config("Board", "arch", 8)
        if arch == 8:
            bootloader = self.configIDE.config("Board", "bootloader", "v1_v2")
            if bootloader == "v1_v2":
                self.pinguinoAPI.set_bootloader(self.pinguinoAPI.Boot2)
            else:
                self.pinguinoAPI.set_bootloader(self.pinguinoAPI.Boot4)
                
                
    #----------------------------------------------------------------------
    def get_description_board(self):
        """"""
        board = self.pinguinoAPI.get_board()
        board_config = "Board: %s\n" % board.name
        board_config += "Proc: %s\n" % board.proc
        board_config += "Arch: %s\n" % board.arch
        
        if board.arch == 8 and board.bldr == "boot4":
            board_config += "Boootloader: v4\n"
        if board.arch == 8 and board.bldr == "boot2":
            board_config += "Boootloader: v1 & v2\n"
            
        return board_config
    
                
                
    #----------------------------------------------------------------------
    def get_status_board(self):
        """"""
        self.set_board()
        board = self.pinguinoAPI.get_board()
        board_config = "Board: %s" % board.name
        #board_config += "Proc: %s\n" % board.proc
        #board_config += "Arch: %s\n" % board.arch
        
        if board.arch == 8 and board.bldr == "boot4":
            board_config += " - Boootloader: v4"
        if board.arch == 8 and board.bldr == "boot2":
            board_config += " - Boootloader: v1 & v2"
            
        return board_config
    
    

