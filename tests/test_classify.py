import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, Hang Zhang <zhanghanggis@163.com>"

class TestClassify(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.crm_prp = self.guerry.GetIntegerCol("Crm_prp")

    def test_hinge15_breaks(self):
        breaks = pygeoda.hinge15_breaks(self.crm_prp)
        self.assertAlmostEqual(len(breaks),5)

    def test_hinge30_breaks(self):
        breaks = pygeoda.hinge30_breaks(self.crm_prp)

    def test_natural_breaks(self):
        breaks = pygeoda.natural_breaks(5, self.crm_prp)
    
    def test_quantile_breaks(self):
        breaks = pygeoda.quantile_breaks(5,self.crm_prp)

    def test_percentile_breaks(self):
        breaks = pygeoda.percentile_breaks(self.crm_prp)

    def test_stddev_breaks(self):
        breaks = pygeoda.stddev_breaks(self.crm_prp)
        self.assertEqual(len(breaks), 5)
        self.assertAlmostEqual(breaks, (1784.1106064421238, 4832.725891456355, 7881.341176470588, 10929.95646148482, 13978.571746499052))
    

