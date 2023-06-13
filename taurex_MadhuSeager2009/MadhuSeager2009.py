from taurex.temperature import TemperatureProfile
import numpy as np
from taurex.data.fittable import fitparam
import scipy as sp


class RandomTemperatureProfile(TemperatureProfile):
    """

    TP profile from Madhusudhan and Seager 2009, arXiv:0910.147v2

    Parameters
    -----------
        T_top: float
            temperature at the top of the atmosphere in Kelvin
        T_1: float
            temperature at Layer 1 of the atmosphere in Kelvin
        T_2: float
            temperature at Layer 2 of the atmosphere in Kelvin
        T_3: float
            temperature at Layer 3 (deepest layer) of the atmosphere in Kelvin
        P_1: float
            pressure at Layer 1 of the atmosphere in bar
        P_2: float
            pressure at Layer 2 of the atmosphere in bar
        P_3: float
            pressure at Layer 3 (deepest layer) of the atmosphere in bar
        alpha_1: float
            multiplicative factor
        alpha_2: float
            multiplicative factor
    """

    ### Initializing the new class
    def __init__(self, T_top = 1000, T_1 = 500, T_2 = 200, T_3 = 100, P_1 = 1e-2, P_2 = 1e-1, P_3 = 1e0, alpha_1 = 50, alpha_2 =50):
        super().__init__('Equilibrium')

        self.info('MadhuSeager2009 temperature profile initialised')
        self._T_top = T_top
        self._T_1 = T_1
        self._T_2 = T_2 
        self._T_3 = T_3
        self._P_1 = P_1 
        self._P_2 = P_2 
        self._P_3 = P_3 
        self._alpha_1 = alpha_1
        self._alpha_2 = alpha_2 
    
    ### Defining the get and set function for the fitting parameter 'mean'
    @fitparam(param_name='T_top',
              param_latex='$T_top$',
              default_fit=False,
              default_bounds=[300.0, 2000.0])
    def topTemperature(self):
        return self._T_top
    
    @topTemperature.setter
    def topTemperature(self, value):
        self._T_top = value
    
    ### The key of this class, this provides the temperature profile.
    ### This 'profile()' function is mandatory for all classes inheriting from the TemperatureProfile class.
    @property
    def profile(self):
        """Returns stratified pressure-temperature layer with two constraints of continuity at the two layer boundaries, i.e., Layers 1–2 and Layers 2–3
        """
        # self.T = np.maximum(np.random.normal(self._mean, self._std), 10.0)
        # T = np.zeros((self.nlayers))
        # creating an array of temp with the number of layers that taurex sets (i guess from the rad tran)
        # T[:] = self.T
        # then have T be that function filling that array (i guess)
        # return T
        # this is then the result 

        p_top = 1e-5 
        # as set within the paper. bar
        beta = 0.5 
        # both beta_1 and beta_2 in the paper are set to be 0.5 based on experimental factor 

        self.P_3 = 100 
        # because three zonal layers set in paper from 10-5 to 100 bar

        self.P_2 = 

        T = np.zeros((self.nlayers))

    

        T_1 = self.T_top + (1/(self.alpha_1**2))(np.log(self.p_top/self.P_1))**2 
        T_2 = self.T_top + (1/(self.alpha_1**2))(np.log(self.P_1/self.p_top))**2 - (1/(self.alpha_2**2))(np.log(self.P_1/self.P_2))**2
        T_3 = self.T_2 + (1/(self.alpha_2**2))(np.log(self.P_3/self.P_2))**2

        # implementation in Madhu & Seager 2009 uses a Levenberg-Marquardt fitting 

        sp.optimize.least_squares(fun,x0,method='lm')

    ### This is to tell TauREx what outputs to save
    def write(self, output):
        temperature = super().write(output)
        temperature.write_scalar('T_top', self._T_top)
        temperature.write_scalar('T_1', self._T_1)
        temperature.write_scalar('T_2', self._T_2)
        temperature.write_scalar('T_3', self._T_3)
        temperature.write_scalar('P_1', self._P_1)
        temperature.write_scalar('P_2', self._P_2)
        temperature.write_scalar('P_3', self._P_3)
        return temperature

    ### This is the keyword to use in the parfile
    @classmethod
    def input_keywords(cls):
        return ['MadhuSeager2009', ]
