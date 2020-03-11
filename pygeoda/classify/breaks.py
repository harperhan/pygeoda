from ..libgeoda import gda_hinge15breaks
from ..libgeoda import gda_stddevbreaks
from ..libgeoda import gda_naturalbreaks
def hinge15breaks(k,data,**kwargs):
    undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge15breaks(k,data,undefs)
def stddev_breaks(k,data,**kwargs):
    undefs = tuple([False]*len(data)) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_stddevbreaks(k,data,undefs)
def naturalbreaks(k,data,**kwargs):
    undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_naturalbreaks(k,data,undefs)
