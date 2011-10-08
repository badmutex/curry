
import types
import marshal

class curry(object):
    def __init__(self, fn, *args, **kws):
        if not type(self) == curry:
            raise TypeError, "To ensure sanity, 'curry' cannot be subclassed"

        if not type(fn) == types.FunctionType:
            raise TypeError, "The function must be %s, not %s" % (types,FunctionType, type(fn))

        self.fn        = fn
        self.args      = args
        self.kws       = kws

        self.func_name = 'curry(%s, *%s, **%s)' % (self.fn.func_name, self.args, self.kws)

    def __str__(self): return '<function %s>' % self.func_name

    def __call__(self, *args, **kws):
        args0 = self.args + args
        kws0  = self.kws.copy()
        kws0.update(kws)
        return self.fn(*args0, **kws0)

    def __getstate__(self):
        odict       = self.__dict__.copy()
        code        = self.fn.func_code
        odict['fn'] = marshal.dumps(code)
        return odict

    def __setstate__(self, idict):
        code        = marshal.loads(idict['fn'])
        func        = types.FunctionType(code, globals())
        idict['fn'] = func
        self.__dict__.update(idict)
