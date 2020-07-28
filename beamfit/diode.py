import numpy as np

class DiodeModel:
    def __init__ (bmxobs, target, Nbins):
        """"
        bmxobs is of type bmxobs
        target is which signal from bmxobs are we predicting. Could generalize later
        Nbins is the number of frequency bins
        """

        self.freq = bmxobs.freq[target%100]  ## this might not work all the time
        assert (len(self.freq)%Nbins ==0 ) ## let's demand things are divisible, say 64 bins with 256 bins total
        self.Nbins = Nbins
        self.bin_size = len(self.freq)//self.Nbins
        self.response = np.zeros(Nbins)

    def _paramname (self,i):
        return "diode_%04d"%i

    def _index_from_param(self,name):
        return int(name[-4:])
    
    def parameters(self):
        toret={}
        for i in range(self.Nbins):
            toret[self._paramname(i)] = self.response[i]
        return toret

    def set_parameters(self,pars):
        for p,v in pars:
            self.response[self._index_from_param(p)]=v

    def __call__ (self):
        ## first build a frequency shape
        freq_resp = np.hstack([np.ones(self.bin_size)*v for v in self.response])
        return np.outer (bmxobs.diode, freq_resp)
    
        
            
            
        
