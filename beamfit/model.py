


class BMXModelSignal:
    def __init__ (self, obs, target, gain, signal, diode, noise):
        """"
        bmxobs is of type bmxobs
        target is which signal from bmxobs are we predicting. Could generalize later
        gain, signal, diode, noise are models for these components
        """
        self.obs = bmxobs
        self.target = target
        self.Nt = len(obs.mjd)
        self.Nf = len(obs.freq[target])

        self.gain = gain
        self.signal = signal
        self.diode = diode
        self.noise = noise

    def parameters(self):
        """ returns a dictionary of
            {parameter_name : parameter_value}
        """
        toret = {}
        toret.update (self.gain.parameters())
        toret.update (self.signal.parameters())
        toret.update (self.diode.parameters())
        toret.update (self.noise.parameters())
        return toret
        
    def set_parameters (self, params):
        """ params is a dictionary like the one returned by parameters """
        gain_params = self.gain.parameters()
        signal_params = self.signal.parameters()
        diode_params = self.diode.parameters()
        noise_params = self.noise.parameters()

        for p,v in params.items:
            if p in gain_params:
                gain_params[p]=v
            elif p in signal_params:
                signal_params[p]=v
            elif p in diode_params:
                diode_params[p]=v
            elif p in noise_params:
                noise_params[p]=v
            else:
                print ("Parameter %s not recognized!"%p)
                stop()

        gain_params.set_parameters(gain_params)
        signal_params.set_parameters(signal_params)
        diode_params.set_parameters(diode_params)
        noise_params.set_parameters(noise_params)

    def __call__ (self):
        pred = self.gain()*(self.signal() + self.diode() + self.noise())
        assert (pred.shape = (self.Nt,self.Nf))
        return pred
                
                
        
        
                      
                      
        

