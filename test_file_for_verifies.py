class Inspect:
    def __init__(self, instance):
        self._inspect(instance.__class__)
 
    def _inspect(self, instance, indent=1):
        attrs = filter(lambda key: not key.startswith('_'), instance.__dict__)
        print "%s|- %s %r" % (' '*indent, instance.__name__, attrs)
        for super_class in instance.__bases__:
            self._inspect(super_class, indent+3)
 
 
class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass
class E(D): pass
 
e = E()
 
Inspect(e)