
from e8663d import VoltageControlledOscillator

with VoltageControlledOscillator('10.68.150.65',5025) as vco_x:
    # 0. check current status
    print('fixedfrequency is ',vco_x.fixedfrequency)
    
    # 1. run some 'static' commands
    vco_x.fix(10,unit='MHz')
    vco_x.step(10,unit='Hz')
    vco_x.step(-10,unit='Hz')
    
    # 2. run sweep, and check status continuously
    vco_x.sweep(40.0272e6-10,40.0272e6+10,1)
