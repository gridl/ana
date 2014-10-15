import ana
import nose
import pickle

import logging
l = logging.getLogger("ana.test")

class A(ana.Storable):
    def __init__(self, n):
        self.n = n
        l.debug("Initialized %s", self)

    def __repr__(self):
        return "<A %s %d>" % (id(self), self.n)

    def _ana_getstate(self):
        return self.n

    def _ana_setstate(self, s):
        self.n = s

def test_ana():
    l.debug("Initializing 1")
    one = A(1)
    l.debug("Initializing 2")
    two = A(2)

    one.make_uuid()

    l.debug("Copying 1")
    one_p = pickle.dumps(one, pickle.HIGHEST_PROTOCOL)
    one_copy = pickle.loads(one_p)
    l.debug("Copying 2")
    two_p = pickle.dumps(two, pickle.HIGHEST_PROTOCOL)
    two_copy = pickle.loads(two_p)

    nose.tools.assert_equal(str(one_copy), str(one))
    nose.tools.assert_not_equal(str(two_copy), str(two))

if __name__ == '__main__':
    import sys
    logging.getLogger("ana.test").setLevel(logging.DEBUG)
    logging.getLogger("ana.storable").setLevel(logging.DEBUG)
    logging.getLogger("ana.datalayer").setLevel(logging.DEBUG)

    if len(sys.argv) > 1:
        getattr('test_%s' % sys.argv[1])()
    else:
        test_ana()
