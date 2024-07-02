#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  artikel_bernardi.py
#  
#  Copyright 2024 Stefan Born <born@math.tu-berlin.de>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#   MA 02110-1301, USA.
# 
#  This program only consists of snippets to be used in a project
# by students on bee swarm models. It implements elements of an 
# article:
#
# Sara Bernardi et al.: A discrete particle model reproducing collective
#                       dynamics of  a bee swarm.
# Computers in Biology and Medicine 93 (2018), 158-174


import numpy as np
from collections import namedtuple


V_MAX = 9.4  #  m/s**2
N_BEES = 100
R_REP = 0.3
R_ATTR = 10
R_ALIGN = 2.5

F_REP = 1.4e4
F_ATTR = 1

X_TARGET = np.array([7,7])


Bee = namedtuple('Bee', ['x','v'])


swarm = []
for i in range(N_BEES):
    swarm.append(Bee(x=np.random.rand(2)*1-0.5, v= np.random.rand(2)*10-5))
    
    





def normalize_speed(v):
    '''setzt Geschwindigkeiten größer als V_MAX auf V_MAX,
    tut sonst nichts.
    Args:
        v:  np.ndarray
    '''
    v_abs = np.linalg.norm(v)
    return min(V_MAX, v_abs)/v_abs*v
    

def v_target(x, x_target):
    '''
    wunschgeschwindigkeit auf Ziel
    (x, x_target):  np.ndarray
    
    Formel (21)
    '''
    return V_MAX/np.linalg.norm(x_target-x)*(x_target -x)
    
    
def v_soc(i, swarm):
    return v_rep(i, swarm) + v_attr(i, swarm) + v_align(i, swarm)
    
    
def h_rep(r):
    '''Gleichung (15)'''
    if r<R_REP:
        return F_REP*(1/R_REP-1/r)
    else:
        return 0.
    
    
def v_rep(i, swarm):
    '''Gleichung (7) mit Minuszeichen'''
    
    swarm_rep = [ bee for j, bee in enumerate(swarm) if np.linalg.norm(bee.x - swarm[i].x)<R_REP and j != i]
    n_bees = len(swarm_rep)
    if n_bees>0:
        cumulated = np.zeros(2)
        for bee in swarm_rep:
            vektor = bee.x-swarm[i].x
            abstand = np.linalg.norm(vektor)
            #print(vektor, abstand, h_rep(abstand))
            cumulated += -h_rep(abstand)/abstand*vektor
        return 1/len(swarm_rep)*cumulated
    else:
        return np.zeros(2)
    

def h_attr(r):
    '''Gleichung (16)'''
    if R_align<r<=R_attr:
        return 4*F_attr*(r-R_attr)(r-R_align)/(R_attr-R_align)**2
    else:
        return 0
    

def v_attr(i, swarm):
    '''Gleichung (7) mit Minuszeichen'''
    
    swarm_attr = [ bee for j, bee in enumerate(swarm) if R_ALIGN<=np.linalg.norm(bee.x - swarm[i].x)<R_ATTR and j != i]
    n_bees = len(swarm_attr)
    if n_bees>0:
        cumulated = np.zeros(2)
        
        for bee in swarm_attr:
            vektor = bee.x-swarm[i].x
            abstand = np.linalg.norm(vektor)
            cumulated += -h_attr(abstand)/abstand*vektor
        return 1/len(swarm_attr)*cumulated
    else:
        return np.zeros(2)

def v_align(i, swarm):
    ''' Gleichung (11)'''
    swarm_align = [ bee for j, bee in enumerate(swarm) if R_REP<=np.linalg.norm(bee.x - swarm[i].x)<R_ALIGN and j != i]
    n_bees = len(swarm_align)
    if n_bees == 0:
        return np.zeros(2)
    else:
        v_mean = sum([bee.v for bee in swarm_align])/n_bees
        return v_mean

def v_wunsch(i, swarm):
    return v_soc(i,swarm)+v_target(swarm[i].x, X_TARGET)

if __name__ == '__main__':
    pass
