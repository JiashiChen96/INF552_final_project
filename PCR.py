
import pandas as pd
import numpy as np



class pcr:
    def __init__(self, data, default = True, components = None, intercept = None, coef = None):
        self.data = data
        if default:
            self.coef = np.array([3.901439382801425, 1.01767600e-04, 5.32912417e-02, -2.48452602e-01, -2.45966805e-01, -1.47640559e-01])
            self.components = np.array([[ 9.99999868e-01,  1.65804341e-04,  2.99819885e-04,
         2.57028082e-04,  1.59549600e-04,  8.09182302e-05,
         1.06733899e-04,  1.57734044e-04,  1.08588425e-04],
       [-2.13723523e-04,  1.65693473e-02,  5.44757589e-02,
         6.08367211e-02,  9.92516427e-01,  4.02729437e-02,
         4.36476488e-02,  5.22751689e-02,  4.13293786e-02],
       [ 4.59185344e-04, -3.77923983e-01, -4.85679278e-01,
        -5.34623494e-01,  1.16309411e-01, -2.36148487e-01,
        -2.38908736e-01, -3.89861524e-01, -2.38962825e-01],
       [-2.13622908e-05, -7.43981112e-02, -1.19202344e-01,
         7.87775583e-01,  1.10436205e-02, -2.93238353e-01,
        -1.96337441e-01, -4.53595998e-01, -1.71046600e-01],
       [-5.33984890e-05,  5.91790953e-01,  4.96735738e-01,
        -2.93791803e-01,  2.70601803e-02, -2.54384263e-01,
        -1.43673877e-01, -4.64392331e-01, -1.22382276e-01]])
        else:
           self.coef = np.append(intercept, coef)
           self.components = components

    def predict(self):
        pcrMat = self.data @ self.components.T
        pcrMat = np.hstack((np.array([[1] for i in range(pcrMat.shape[0])]), pcrMat))
        self.res = pcrMat @ self.coef.T
        return self.res

        



        


