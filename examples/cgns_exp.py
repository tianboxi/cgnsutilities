import cgnsutilities as cu
import numpy as np

# BC type dictionary
BCdic = cu.BC
BClist = list(BCdic.keys())
BCval = list(BCdic.values())

grid = cu.readGrid('grid_absper_vis_latest.cgns')
grid.printInfo()
grid.printBlockInfo()

nblk = len(grid.blocks)
blk1 = grid.blocks[0]
nbc = len(blk1.bocos)

# bc infos
for i,boco in enumerate(blk1.bocos):
   print('BC #'+str(i)+': ')
   print('Name: ',boco.name)
   print('Type: ',boco.type)
   print(BClist[BCval.index(boco.type)])
   print('Family: ', boco.family)
   print('PtRange:',boco.ptRange)
   type(boco.family)
   if boco.family == 'inflow':
      print('This bc')
