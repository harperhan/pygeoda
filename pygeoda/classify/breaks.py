from ..libgeoda import gda_hinge15breaks
from ..libgeoda import gda_hinge30breaks
from ..libgeoda import gda_naturalbreaks
from ..libgeoda import gda_quantilebreaks
from ..libgeoda import gda_percentilebreaks
from ..libgeoda import gda_stddevbreaks
__author__ = "Hang Zhang <zhanghanggis@163.com>"

def hinge15_breaks(data,**kwargs):
    """
    """
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge15breaks(data)
def hinge30_breaks(data,**kwargs):
    """
    """
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge30breaks(data)

def natural_breaks(k,data,**kwargs):
    """
    """
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_naturalbreaks(k,data)

def quantile_breaks(k,data,**kwargs):
    """
    """
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_quantilebreaks(k,data)

def percentile_breaks(data,**kwargs):
    """
    """
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_percentilebreaks(data)

def stddev_breaks(data,**kwargs):
    """
    """
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_stddevbreaks(data)

