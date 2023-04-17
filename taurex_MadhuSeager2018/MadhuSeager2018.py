from taurex.temperature import TemperatureProfile
import numpy as np
from taurex.data.fittable import fitparam


class RandomTemperatureProfile(TemperatureProfile):
    """A random isothermal temperature-pressure profile
    """

    ### Initializing the new class
    def __init__(self, mean = 1000, std = 200):
        super().__init__('Equilibrium')
        self._mean = mean
        self._std = std
    
    ### Defining the get and set function for the fitting parameter 'mean'
    @fitparam(param_name='Tmean',
              param_latex='$Tmean$',
              default_fit=False,
              default_bounds=[300.0, 2000.0])
    def meanTemperature(self):
        return self._mean
    
    @meanTemperature.setter
    def meanTemperature(self, value):
        self._mean = value
    
    ### The key of this class, this provides the temperature profile.
    ### This 'profile()' function is mandatory for all classes inheriting from the TemperatureProfile class.
    @property
    def profile(self):
        """Returns a random temperature profile
        """
        self.T = np.maximum(np.random.normal(self._mean, self._std), 10.0)
        T = np.zeros((self.nlayers))
        T[:] = self.T

        return T

    ### This is to tell TauREx what outputs to save
    def write(self, output):
        temperature = super().write(output)
        temperature.write_scalar('mean', self._mean)
        temperature.write_scalar('std', self._std)
        temperature.write_scalar('T', self.T)
        return temperature

    ### This is the keyword to use in the parfile
    @classmethod
    def input_keywords(cls):
        return ['random_tp', ]
