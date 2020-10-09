import cgnsutilities as cu
import numpy as np

# BC type dictionary
BCdic = cu.BC
BClist = list(BCdic.keys())
BCval = list(BCdic.values())
print(BCdic)

# Read a grid
grid = cu.readGrid('./inputFiles/grid_absper_vis_latest_output.cgns')
#grid = cu.readGrid('./inputFiles/naca0012.cgns')
# Print some info
grid.printInfo()
grid.printBlockInfo()

nblk = len(grid.blocks)
blk1 = grid.blocks[0]
nbc = len(blk1.bocos)

print(' =========== BCs ===============')
# bc infos
for i,boco in enumerate(blk1.bocos):
   print(' =================')
   print('BC #'+str(i)+': ')
   print('Name: ',boco.name.decode('utf8').strip())
   print('Type: ',boco.type)
   print(BClist[BCval.index(boco.type)])
   print('Family: ', boco.family.decode('utf8').strip())
   ndset = len(boco.dataSets)
   print('Ndatasets: ', ndset)
#   print('PtRange:',boco.ptRange)
   if ndset >= 1:
      dset = boco.dataSets[0]
      print('Dname: ',dset.name.decode('utf8').strip())
      print('Dtype: ',dset.type)
      nddirch = len(dset.dirichletArrays)
      ndneuma = len(dset.neumannArrays)
      print('nDirichlet: ',nddirch)
      print('nNeumann: ',ndneuma)
      if nddirch>=1:
         print(' +++ Data Set 1 +++')
         dirchdata = dset.dirichletArrays[0]
         dataname = dirchdata.name.decode('utf8').strip()
         print('ArrayName: ', dirchdata.name.decode('utf8').strip())
         if dataname == 'Pressure':
            dirchdata.dataArr =np.array([101325])
         print('ArrayNDim: ', dirchdata.nDimensions)
         print('ArrayDtype: ', dirchdata.dataType)
         print('ArrayDDim: ', dirchdata.dataDimensions)
         print('Array: ', dirchdata.dataArr)
         print('NP arrary shp', dirchdata.dataArr.shape)

print(' =========== B2B ===============')
nb2b = len(blk1.B2Bs)
print('# Block to Block connection: ', nb2b)
for b2b in blk1.B2Bs:
   print('name: ',b2b.name.decode('utf8').strip())
   print('donor name:', b2b.donorName.decode('utf8').strip())
#  print('range:',  b2b.ptRange)
#   print('donor range: ', b2b.donorRange)
   print('transform: ', b2b.transform)

#grid.writeToCGNS('./inputFiles/grid_absper_vis_latest_output.cgns')

