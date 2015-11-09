# coding: utf-8
'''
-----------------------------------------------------------------------------
Copyright 2015 Esri
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-----------------------------------------------------------------------------

==================================================
ERGToolsTestSuite.py
--------------------------------------------------
requirments:
* ArcGIS Desktop 10.X+ or ArcGIS Pro 1.X+
* Python 2.7 or Python 3.4
author: ArcGIS Solutions
company: Esri
==================================================
description:
Test Suite collects all of the test cases for the ERG Tools toolbox:
* ERGByPlacardTestCase.py
* ERGByChemicalTestCase.py

==================================================
history:
11/09/2015 - MF - placeholder
==================================================
'''

import unittest
import TestUtilities
from . import ERGByPlacardTestCase
from . import ERGByChemicalTestCase

def getERGTestSuite(logger, platform):
    ''' run the HLZ tests as either Pro or Desktop'''

    if TestUtilities.DEBUG == True:
        print("      ERGTestSuite.runHLZTestSuite")
    testSuite = unittest.TestSuite()
    logger.info("ERG Tools tests")
    testSuite.addTest(ERGByChemicalTestCase.ERGByChemical('test_ERGByChemical'))
    testSuite.addTest(ERGByPlacardTestCase.ERGByPlacard('test_ERGByPlacard'))
    return testSuite
