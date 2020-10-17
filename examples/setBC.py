import cgnsutilities as cu
import numpy as np

# Read a grid
gridFile = './inputFiles/grid_absper_vis_latest_output.cgns'
grid = cu.readGrid(gridFile)
# Print grid infos
#grid.printInfo()
#grid.printBlockInfo(detail=True)

grid.setBackPressure('outflow',[118000])
grid.setInletCondition('inflow',[101325, 288.15, 1.0, 0.0, 0.0])

#angle = 24.0 #deg
#grid.setPeriodics(rotAngles=[angle/180*np.pi, 0.0, 0.0])
grid.writeToCGNS('./inputFiles/grid_absper_vis_latest.cgns')
