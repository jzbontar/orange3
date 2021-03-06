import unittest
import numpy as np

import Orange
from Orange.projection import MDS, Isomap, LocallyLinearEmbedding
from Orange.distance import Euclidean


class TestManifold(unittest.TestCase):
    def test_mds(self):
        data = Orange.data.Table('ionosphere')[:100]
        self.__mds_test_helper(data, n_com=1)
        self.__mds_test_helper(data, n_com=2)
        self.__mds_test_helper(data, n_com=3)

    def __mds_test_helper(self, data, n_com):
        mds_fit = MDS(n_components=n_com, dissimilarity=Euclidean, random_state=0)
        mds_fit = mds_fit(data)
        mds_dist = MDS(n_components=n_com, dissimilarity='precomputed', random_state=0)
        mds_dist = mds_dist(Euclidean(data))
        eshape = data.X.shape[0], n_com
        self.assertTrue(np.allclose(mds_fit.embedding_, mds_dist.embedding_))
        self.assertEqual(eshape, mds_fit.embedding_.shape)
        self.assertEqual(eshape, mds_dist.embedding_.shape)

    def test_isomap(self):
        data = Orange.data.Table('ionosphere')
        self.__isomap_test_helper(data, n_com=1)
        self.__isomap_test_helper(data, n_com=2)
        self.__isomap_test_helper(data, n_com=3)

    def __isomap_test_helper(self, data, n_com):
        isomap_fit = Isomap(n_neighbors=5, n_components=n_com)
        isomap_fit = isomap_fit(data)
        eshape = data.X.shape[0], n_com
        self.assertEqual(eshape, isomap_fit.embedding_.shape)

    def test_lle(self):
        data = Orange.data.Table('ionosphere')
        self.__lle_test_helper(data, n_com=1)
        self.__lle_test_helper(data, n_com=2)
        self.__lle_test_helper(data, n_com=3)

    def __lle_test_helper(self, data, n_com):
        isomap_fit = Isomap(n_neighbors=5, n_components=n_com)
        isomap_fit = isomap_fit(data)
        eshape = data.X.shape[0], n_com
        self.assertEqual(eshape, isomap_fit.embedding_.shape)
