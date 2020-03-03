from ..libgeoda import gda_hinge15breaks
def hinge15breaks(k,data,**kwargs):
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge15breaks(k,data,undefs)
    