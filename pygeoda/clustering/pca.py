from ..libgeoda import gda_pca
from ..libgeoda import PCAResult
def pca(data):
    ''' Principal component analysis
    By means of an orthogonal transformation, it transforms the original random vector of its component correlation into a new random vector of 
    its component uncorrelation, which is algebraically represented by transforming the covariance matrix of the original random vector into a 
    diagonal matrix, geometrically represented by transforming the original coordinate system into a new orthogonal coordinate system, so that it 
    points to the p-coordinate with the widest spread of sample points Then, the multi-dimensional variable system can be transformed into a low-dimensional
    variable system with a high precision, and then the low-dimensional system can be further transformed into a one-dimensional system by constructing 
    a proper value function. In GeoDa and pygeoda,this function is based on the abnormal operation of 'SVD' method:

    Arguments:
        data: A 2d numeric list with values of selected variables

    Returns:
        A PCA object that wrappers the c++ PCAResult object containing the details of PCA computation
    '''
    return gda_pca(data)
class PCA(object):#Do we set PCA as a subclass of PCAResult ?
    '''Wrapper of Princinple Components Analysis results
    A python wrapper of PCA results for easy access
    
    Arguments:    
        A PCA object that wrappers the c++ PCAResult object containing the details of PCA computation

    Returns:
        A PCA object that wrappers the c++ PCAResult object containing the details of PCA computation    
    '''
    def __init__(self,pca):
        self.pca_r = pca
    def getMethod(self):
        return self.pca_r.getMethod()
    def getStandarDev(self):                
        return self.pca_r.getStandardDev()
    def getPropOfVar(self):
        return self.pca_r.getPropOfVar()
    def getCumProp(self):
        return self.pca_r.getCumProp()
    def getKaiser(self):
        return self.pca_r.getKaiser()
    def getThresh95(self):
        return self.pca_r.getThresh95()
    def getEigenValues(self):
        return self.pca_r.getEigenValues()
    def getLoadings(self):
        return self.pca_r.getLoadings()
    def getSqCorrelations(self):
        return self.pca_r.getSqCorrelations()



    