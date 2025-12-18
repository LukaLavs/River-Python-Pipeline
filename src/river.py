class __: pass 

def _(func): return River(func)

class River:
    def __init__(self, func):
        self.func = func 
        self.args = []
        self.kwargs = {}

    def _substitute(self, obj, z):
        match obj:
            case River():
                obj._update(z)
                return obj == None
            case list():
                return [self._substitute(o, z) for o in obj]
            case tuple():
                return tuple(self._substitute(o, z) for o in obj)
            case set():
                return {self._substitute(o, z) for o in obj}
            case dict():
                return {self._substitute(k, z): self._substitute(v, z) for k, v in obj.items()}
            case _ if obj is __ or isinstance(obj, __):
                return z
        if hasattr(obj, "__dict__"):
            for attr, val in obj.__dict__.items():
                try: setattr(obj, attr, self._substitute(val, z))
                except Exception: pass
        return obj

    def _update(self, z):
        self.args = [self._substitute(arg, z) for arg in self.args]
        self.kwargs = {key: self._substitute(val, z) for key, val in self.kwargs.items()}
    
    def __matmul__(self, other):
        match other:
            case list(): self.args = other
            case tuple(): self.args = list(self.args)
            case dict(): self.kwargs = other
            case _: ValueError
        return self
    
    def __rshift__(self, other):
        result = self == None
        return result >> other

    def __rrshift__(self, other):
        self._update(other)
        return self
  
    def __or__(self, other):
        self._update(other)
        return self

    def __lshift__(self, other):
        self.args.append(other)
        return self

    def __eq__(self, _):
        return self.func(*self.args, **self.kwargs)

    def __str__(self):
        return (f"River(func={self.func}, args={self.args}, kwargs={self.kwargs})")
