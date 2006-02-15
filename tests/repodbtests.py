# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import unittest
import os

import pisi.context as ctx
import pisi.api
import pisi.installdb
from pisi import util

import testcase
class RepoDBTestCase(testcase.TestCase):

    def testAddRemoveCycle(self):
        # written by cartman the celebrity, for bug #1909 
        pisi.api.add_repo("foo","bar")
        
        for i in range(2):
            print '\nTest %d\n' % (i)
            pisi.api.remove_repo("foo")
            pisi.api.add_repo("foo","bar")

suite = unittest.makeSuite(RepoDBTestCase)
