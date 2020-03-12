from ..libgeoda import gda_hinge15breaks
from ..libgeoda import gda_stddevbreaks
from ..libgeoda import gda_naturalbreaks
from ..libgeoda import gda_quantilebreaks
from ..libgeoda import gda_hinge30breaks
from ..libgeoda import gda_percentilebreaks

__author__ = "Hang Zhang <zhanghanggis@163.com>"

def hinge15_breaks(k,data,**kwargs):
    """
    """
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge15breaks(k,data)

def natural_breaks(k,data,**kwargs):
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_naturalbreaks(k,data)

def quantile_breaks(k,data,**kwargs):
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_quantilebreaks(k,data)

def hinge30_breaks(k,data,**kwargs):
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge30breaks(k,data)

def percentile_breaks(k,data,**kwargs):
    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_percentilebreaks(k,data)

def stddev_breaks(k,data,**kwargs):
    """
    """
    return gda_stddevbreaks(k,data)

