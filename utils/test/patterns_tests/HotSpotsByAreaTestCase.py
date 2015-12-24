# coding: utf-8
# -----------------------------------------------------------------------------
# Copyright 2015 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

# ==================================================
# HotSpotsByAreaTestCase.py
# --------------------------------------------------
# requirments: ArcGIS X.X, Python 2.7 or Python 3.4
# author: ArcGIS Solutions
# company: Esri
# ==================================================
# history:
# 12/16/2015 - JH - initial creation
# ==================================================

import unittest
import arcpy
import os
import UnitTestUtilities
import Configuration

class HotSpotsByAreaTestCase(unittest.TestCase):
    ''' Test all tools and methods related to the Hot Spots by Area tool
    in the Incident Analysis toolbox'''
    
    
    def setUp(self):
        if Configuration.DEBUG == True: print("     HotSpotsByAreaTestCase.setUp")
        
    def tearDown(self):
        if Configuration.DEBUG == True: print("     HotSpotsByAreaTestCase.tearDown")    
        
    def test_hot_spots_by_area_pro(self):
        if Configuration.DEBUG == True: print("     HotSpotsByAreaTestCase.test_hot_spots_by_area_pro")    
    
    def test_hot_spots_by_area_desktop(self):
        if Configuration.DEBUG == True: print("     HotSpotsByAreaTestCase.test_hot_spots_by_area_desktop")    
        
    def test_hot_spots_by_area(self, toolboxPath):
        if Configuration.DEBUG == True: print("     HotSpotsByAreaTestCase.test_hot_spots_by_area")
            