#!/usr/bin/env bash

set -o errexit

pytestA=.test_curry_testa.py
pytestB=.test_curry_testb.py
pkl=.test_curry.pkl

cat <<EOF>$pytestA
import curry
import cPickle as pickle

def foo(x,y, **kws):
    z = kws.pop('z', 1)
    return x * y * z

f = curry.curry(foo, 3, z=9)
with open("$pkl", 'w') as fd:
    pickle.dump(f, fd)
EOF


cat <<EOF>$pytestB
import cPickle as pickle

with open("$pkl") as fd:
    fn = pickle.load(fd)

import sys
if fn(6) == 162:
    print 'Test passes'
    sys.exit(0)
else:
    print 'Test failes:', fn(6)
    sys.exit(1)
EOF


python $pytestA
python $pytestB

for f in $pytestA $pytestB $pkl; do
	rm -v $f
done