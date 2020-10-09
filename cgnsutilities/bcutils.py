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


def setBackPressure(infileName, fam, data, outfileName=None, rotor=None)
   '''
   Set back pressure given a outflow fam name
   '''
   assert(len(data)==1)
   grid = cu.readGrid(fileName)
   nblk = len(grid.blocks)
   for blk in grid.blocks:
      nboco = len(blk.bocos)
      for boco in blk.bocos:
         famname = boco.famliy.decode('utf8').strip()
         if famname == fam:
            boco.type = cu.BC['bcoutflowsubsonic']
            boco.dataSets = []
            bp = cu.BocoDataSet('BCDataSet',boco.type)
            boco.dataSets.append(bp)
            arr_p = cu.BocoDataSetArray('Pressure', 4, 1, [1,1,1], [data[0]])
            boco.dataSets.dirichletArrays = []
            boco.dataSets.dirichletArrays.append(arr_p)

   if not outfileName:
      outfileName = infileName
   cu.writeToCGNS(outfileName)

def setInletCondition(infileName, fam, data, outfileName=None, rotor=None)
   '''
   Set total condition or mass flow condition for subsonic inlet given inflow fam name
   '''
   assert(len(data)==5)
   grid = cu.readGrid(fileName)
   nblk = len(grid.blocks)
   for blk in grid.blocks:
      nboco = len(blk.bocos)
      for boco in blk.bocos:
         famname = boco.famliy.decode('utf8').strip()
         if famname == fam:
            boco.type = cu.BC['bcinflowsubsonic']
            boco.dataSets = []
            dset = cu.BocoDataSet('BCDataSet',boco.type)
            boco.dataSets.append(dset)
            arr_pt = cu.BocoDataSetArray('PressureStagnation', 4, 1, [1,1,1], [data[0]])
            arr_tt = cu.BocoDataSetArray('TemperatureStagnation', 4, 1, [1,1,1], [data[1]])
            arr_vdirx = cu.BocoDataSetArray('VelocityUnitVectorX', 4, 1, [1,1,1], [data[2]])
            arr_vdiry = cu.BocoDataSetArray('VelocityUnitVectorY', 4, 1, [1,1,1], [data[3]])
            arr_vdirz = cu.BocoDataSetArray('VelocityUnitVectorZ', 4, 1, [1,1,1], [data[4]])
            arrlist = [arr_pt,arr_tt,arr_vdirx,arr_vdiry,arr_vdirz]
            boco.dataSets.dirichletArrays = []
            for arr in arrlist:
               boco.dataSets.dirichletArrays.append(arr)

   if not outfileName:
      outfileName = infileName
   cu.writeToCGNS(outfileName)

def setPeriodics()
   '''
   Set periodic BCs
   '''
   grid = cu.readGrid(fileName)
   nblk = len(grid.blocks)
   transform = [1,2,3]
   # find bcs and get point range
   for blk in grid.blocks:
      nboco = len(blk.bocos)
      for ib,boco in enumerate(blk.bocos):
         famname = boco.famliy.decode('utf8').strip()
         if famname == 'periodic1':
            ptrange1 = boco.ptRange
            blk.bocos.pop(ib)
         elif famname == 'periodic2':
            ptrange2 = boco.ptRange
            blk.bocos.pop(ib)

      per1 = cu.B2B('periodic1',blk.name,ptrange1,ptrange2,transform)     
      per2 = cu.B2B('periodic2',blk.name,ptrange2,ptrange1,transform)     

