import cgnsutilities as cu
import numpy as np

#print(cu.BC)
# Read a grid
#gridFile = 'reservoir_3D_24deg.cgns'
gridFile = 'grid_absper_vis_latest.cgns'
grid = cu.readGrid(gridFile)
# Print grid infos
#grid.printInfo()
#grid.printBlockInfo(detail=True)

grid.setBackPressure('outflow',[115000])
grid.setInletCondition('inflow',[101325, 288.15, 1.0, 0.0, 0.0])

#grid.setInletCondition('inflow',[1.225 , 188.0, 0.0, 0.0],mdot=True)
#grid.setBCFromFam('far','bcfarfield')
#grid.setBCFromFam('wall_viscous','bcwallviscous')
grid.setBCFromFam('wall','bcwallviscous')
#grid.setBCFromFam('wall_euler','bcwallinviscid')
##
#angle = 24.0 #deg
#grid.setPeriodics(rotAngles=[angle/180*np.pi, 0.0, 0.0])
grid.writeToCGNS('./outputFiles/'+gridFile)
##
### verify output grid
#gridFile = './outputFiles/reservoir_3D_24deg.cgns'
gridFile = './outputFiles/grid_absper_vis_latest.cgns'
gridout = cu.readGrid(gridFile)
gridout.printBlockInfo(detail=True)



