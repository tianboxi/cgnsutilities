import os
import copy
import tempfile
import numpy
import .cgnsutilities as cu
from . import libcgns_utils

BCdict = cu.BC

def setBCFromFam(infileName, fam, bc, outfileName=None)
   '''
   Set given familiy to be certain type of BC (no data set)
   '''
   grid = cu.readGrid(fileName)
   nblk = len(grid.blocks)
   for blk in grid.blocks:
      nboco = len(blk.bocos)
      for boco in blk.bocos:
         famname = boco.famliy.decode('utf8').strip()
         if famname == fam:
            boco.type = cu.BC[bc.lower()]
   if not outfileName:
      outfileName = infileName
   cu.writeToCGNS(outfileName)


def setBackPressure(infileName, fam, pressure, outfileName=None, rotor=None)
   '''
   Set back pressure given a outflow fam name
   '''
   grid = cu.readGrid(fileName)
   nblk = len(grid.blocks)
   for blk in grid.blocks:
      nboco = len(blk.bocos)
      for boco in blk.bocos:
         famname = boco.famliy.decode('utf8').strip()
         if famname == fam:
            boco.type = cu.BC['bcinflowsubsonic']
            boco.dataSets = []
            bp = cu.BocoDataSet('BCDataSet',boco.type)
            boco.dataSets.append(bp)
            arr_p = cu.BocoDataSetArray('Pressure', 4, 1, [1,1,1], [pressure])
            boco.dataSets.dirichletArrays = []
            boco.dataSets.dirichletArrays.append(arr_p)

   if not outfileName:
      outfileName = infileName
   cu.writeToCGNS(outfileName)

def setInletCondition()
   '''
   Set total condition or mass flow condition for subsonic inlet given inflow fam name
   '''
   pass

def setPeriodics()
   '''
   Set periodic BCs
   '''
   pass

