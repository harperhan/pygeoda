from ..libgeoda import gda_mds
'''Multi dimensional scale analysis chart

Note:
    Multi dimensional scale analysis chart, which reflects the similarity (dissimilarity) of many research objects in the way of graph (mainly two-dimensional). Laoganma, laoganda and spicy sauce are more similar to each other in the hearts of consumers.

Arguments:

    data: A 2d numeric list of selected variables
    k: The number of dimensions that mds returns. Value range [1,k: the number of selected variables]
return:
    A 2d numeric list of mds results (top k components),which contains the position of each geographical unit in the rectangular coordinate system of the chart
    e.g. [(1,3.4,5,7...X),(2,3,-4,1,5,4...Y)]
'''
def mds(data,k):
    return gda_mds(data,k)