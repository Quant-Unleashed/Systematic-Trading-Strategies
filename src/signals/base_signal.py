class BaseSignal:

    def generate(self, prices):
        raise NotImplementedError("Signal must implement generate()")