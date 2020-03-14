from ..libgeoda import gda_quantilelisa

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

def quantile_lisa(w, k, q, data):
    """
    """
    
    return gda_quantilelisa(w.gda_w, k, q, data)