from threading import Thread
class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,args=(), 
    kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self._return=None


    def run(self):
        self.exc=None
        try:
            self._return=self._target(*self._args, **self._kwargs)
        except Exception as e:
            self.exc=e

    def join(self,timeout=None):
        super().join(timeout=timeout)
        if self.exc:              #start return immediately so we have to target exception handling in join
            raise self.exc
        return self._return    

           


    
