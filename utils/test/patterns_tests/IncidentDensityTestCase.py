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
# IncidentDensityTestCase.py
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

class IncidentDensityTestCase(unittest.TestCase):
    ''' Test all tools and methods related to the Incident Density tool
    in the Incident Analysis toolbox'''
    
    
    def setUp(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.setUp")    
        
    def tearDown(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.tearDown")    
        
    def test_incident_density_pro(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.test_incident_density_pro")    
    
    def test_incident_density_desktop(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.test_incident_density_desktop")    
        
    def test_incident_density(self, toolboxPath):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.test_incident_density")
            