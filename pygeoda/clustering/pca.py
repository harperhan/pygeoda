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
        '''Constructor of PCAResult object
        
        Args:
            PCA_obj (PACResult_obj):An object/pointer of PCAResult class
        '''
        self.pca_r = pca
    def getMethod(self):
        '''get the PCA calculation method

        Return:
            a string of method description
            e.g. 'svd'
        '''
        return self.pca_r.getMethod()               

    def getStandarDev(self):
        '''get the standard deviation of PCAResult
        
        Rerurn:
            :obj:'tuple' of float:a list of float values of standard deviation of PCAResult
            e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''                
        return self.pca_r.getStandardDev()

    def getPropOfVar(self):
        '''get the Proportion of variance of PCAResult
        
        Return:
             :obj:'tuple' of float:a list of float values of Proportion of variance of PCAResult
            e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''
        return self.pca_r.getPropOfVar()

    def getCumProp(self):
        '''get the Cumulative proportion of PCAResult

        Return:
            :obj:'tuple' of float:a list of float values of the Cumulative proportion of PCAResult
            e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''
        return self.pca_r.getCumProp()

    def getKaiser(self):
        '''get the value 0f Kaiser in PCAResult

        Return:
            :obj:'a float number:value 0f Kaiser in PCAResult
            e.g. 3.000
        '''
        return self.pca_r.getKaiser()
    
    def getThresh95(self):
        '''get the value 0f  threshold criteria for contribution up to 95% in PCAResult

        Return:
            :obj:'a float number:value 0f threshold criteria for contribution up to 95% in PCAResult
            e.g. 5.0000
        '''
        return self.pca_r.getThresh95()
    
    def getEigenValues(self):
        '''get the Eigenvalues of PCAResult of PCAResult

        Return:
            :obj:'tuple' of float:a list of float values of the Eigenvalues of PCAResult
            e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''    
        return self.pca_r.getEigenValues()
    
    def getLoadings(self):
        '''get a 2d numeric list with values of  PCAResult base selected variables

        Return:
            :obj:'a 2d numeric list' of float:a 2d numeric list with values of selected variables of PCAResult
            e.g. [[1.463034,1.095819,1.049785,0.816680,0.740726,0.583971],[0.8791, 0.0937, 0.0188, 0.006, 0.0016, 1.425]]
        '''
        return self.pca_r.getLoadings()
    
    def getSqCorrelations(self):
        '''get a 2d numeric list with values of squared correlations of PCAResult base selected variables

        Return:
            :obj:'a 2d numeric list' of float:a 2d numeric list with values of selected variables of PCAResult
            e.g. [[1.463034,1.095819,1.049785,0.816680,0.740726,0.583971],[0.8791, 0.0937, 0.0188, 0.006, 0.0016, 1.425]]
        '''
        return self.pca_r.getSqCorrelations()


    