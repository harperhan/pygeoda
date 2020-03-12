import unittest
import pygeoda
__author__ = "Xun Li <lixun910@gmail.com>, "

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]
        self.Crm_prs = self.guerry.GetRealCol('Crm_prs')
        self.Crm_prp = self.guerry.GetRealCol('Crm_prp')

    def test_dada_mds(self):
        Rt_Nc = pygeoda.mds(self.data,6)
        a = [39472.2,-11260,-16469,33335]
        b = [14855,4591,6700,6079.67]
        for d in Rt_Nc[0]:
            for i in range(0,4):
                if int(a[i]) == int(d):
                    print(1)
        for d in Rt_Nc[1]:
            for i in range(0,4):
                if int(b[i]) == int(d):
                    print(1)
        print(Rt_Nc[1])
    def test_PCA(self):
        #data=[self.Crm_prs,self.Crm_prp]
        pca_r = pygeoda.PCA(self.data)
        
        #self.assertEqual(pca_r.getCumProp(),tuple((0.8791688084602356, 0.9729388952255249, 0.9917565584182739, 0.9983601570129395, 0.9999998807907104, 1.0)))
        
        b1 = pca_r.getEigenValues()
        b2 = pca_r.getKaiser()
        b3 = pca_r.getMethod()
        b4 = pca_r.getPropOfVar()
        b5 = pca_r.getStandardDev()
        b6 = pca_r.getThresh95()
        b7 = pca_r.getLoadings()
        b8 = pca_r.getSqCorrelations()
        b9 = pca_r.getCumProp()
        #self.assertAlmostEqual(p.getmm(),tuple((0.8791688084602356, 0.9729388952255249, 0.9917565584182739, 0.9983601570129395, 0.9999998807907104, 1.0)))

        #result = pygeoda.pca(self.data)

        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_STRCASEEQ(result->getMethod().c_str(), "svd");
        EXPECT_THAT(result->getStandardDev(),
                ElementsAre(1.46303403, 1.09581947, 1.04978454, 0.816680014, 0.740725815, 0.583970726));
        EXPECT_THAT(result->getPropOfVar(),
                    ElementsAre(0.356744826, 0.200136751, 0.183674619, 0.111161061, 0.0914457887, 0.0568369664));
        EXPECT_THAT(result->getCumProp(),
                    ElementsAre(0.356744826, 0.556881547, 0.74055618, 0.851717234, 0.943163037, 1.000000));
        EXPECT_FLOAT_EQ(result->getKaiser(), 3.0);
        EXPECT_FLOAT_EQ(result->getThresh95(), 5.0);
        EXPECT_THAT(result->getEigenValues(),
                    ElementsAre(2.1404686, 1.20082033, 1.10204756, 0.666966259, 0.548674762, 0.341021806));
        """