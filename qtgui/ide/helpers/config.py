#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import re
from ConfigParser import RawConfigParser

if os.path.exists("config"):
    IDE_CONFIG_FILE = file("config", "r").read()
else:
    IDE_CONFIG_FILE = os.path.join("qtgui", "config", "pinguino.conf")

########################################################################
class Config(RawConfigParser, object):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self):
        super(Config, self).__init__()
        
        self.verify_config_file()
        self.load_config()
        #self.readfp(file(IDE_CONFIG_FILE, "r")) 
        
    #----------------------------------------------------------------------
    def get_format_config(self, section, option):
        """"""
        value = self.get(section, option)
        if type(value) != type(""): return value
        
        if re.match("([-\d]+)$", value):
            return int(value)
        
        if re.match("([.\d*e-]+)$", value):
            return float(value)
        
        elif re.match("(true)$", value.lower()):
            return True
        
        elif re.match("(false)$", value.lower()):
            return False
    
        else: return value
            
    #---------------------------------------------------------------------- 
    def config(self, section, option, default):
        """"""
        if self.has_section(section) and self.has_option(section, option):
            return self.get_format_config(section, option)
        else:
            self.set(section, option, default)
            return default
        
    #----------------------------------------------------------------------
    def set(self, section, option, value):
        """"""
        if not self.has_section(section): self.add_section(section)
        super(Config, self).set(section, option, value)
    
    #----------------------------------------------------------------------
    def verify_config_file(self):
        """"""
        if not os.path.isfile(IDE_CONFIG_FILE):
            file(IDE_CONFIG_FILE, "w").close()
        
    #----------------------------------------------------------------------
    def save_config(self):
        """"""
        self.write(file(IDE_CONFIG_FILE, "w"))
        
    #----------------------------------------------------------------------
    def load_config(self):
        """"""
        self.readfp(file(IDE_CONFIG_FILE, "r")) 
        
    #----------------------------------------------------------------------
    def get_filename(self, name, path=False):
        """"""
        if not path:
            parent_dir = self.get("Paths", "pinguino_writeable_path")
        else:
            parent_dir = self.get("Paths", path)
        filename = self.get("Filenames", name)

        return os.path.join(parent_dir, filename)
    
    #----------------------------------------------------------------------
    def get_path(self, name):
        """"""
        return self.get("Paths", name)
        
        
    #----------------------------------------------------------------------
    def get_recents(self):
        """"""
        if not self.has_section("Recents"): self.add_section("Recents")
        options = self.options("Recents")
        
        files = []
        for option in options:
            if option.startswith("recent_"):
                files.append(self.get("Recents", option))
        
        return files
    
    #----------------------------------------------------------------------
    def get_recents_open(self):
        """"""
        if not self.has_section("Recents"): self.add_section("Recents")
        options = self.options("Recents")
        
        files = []
        for option in options:
            if option.startswith("open_"):
                files.append(self.get("Recents", option))
        
        return files