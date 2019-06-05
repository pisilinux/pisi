import unittest
from pisi.specfile import SpecFile
from pisi import uri
from pisi.file import File

class FileTestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def testMakeUri(self):
        spec = SpecFile("repos/pardus-2007/system/base/curl/pspec.xml")
        url = uri.URI(spec.source.archive[0].uri)
        self.assertTrue(File.make_uri(url))

    def testChooseMethod(self):
        compress = open('repos/contrib-2007/pisi-index.xml', File.read)
        self.assertTrue(File.choose_method('pisi.conf', compress))

    def testDecompress(self):
        localfile = open('repos/pardus-2007/system/base/curl/pspec.xml', File.read)
        compress = open('repos/contrib-2007/pisi-index.xml', File.read)
        self.assertTrue(File.decompress(localfile,compress))

    def testLocalFile(self):
        f = open('repos/pardus-2007/system/base/curl/pspec.xml', File.read)
        r = f.readlines()
        assert (len(r) > 0)

    def testRemoteRead(self):
        f = open('http://www.gnu.org/licenses/gpl2.txt', File.read)
        r = f.readlines()
        assert (len(r) > 0)
