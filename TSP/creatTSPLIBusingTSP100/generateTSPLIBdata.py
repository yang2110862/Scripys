# Program:
#   generate data in TSPLIB format using TSP100
# History:
#   2022/1/11   yxl   First release
# Reference
#   ../data_generator.py

import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

def convert_tsplib(tspinstance, num_node = 20, num_instance = 0):
    derivate = tspinstance.split(' ')
    opt_sol = np.array(derivate[2*num_node+1:-1], dtype = np.int32) - 1 
    buff = np.zeros(shape=(num_node, 2), dtype = np.float64)
    buff[:, 0] = np.array(derivate[0:2*num_node:2], dtype = np.float64)
    buff[:, 1] = np.array(derivate[1:2*num_node:2], dtype = np.float64)
    with open('/home/seanyang/Desktop/git/LKH3/LKH-3.0.7/data/tsp{}/uniform{}.tsp'.format(num_node, num_instance), 'w') as f1:
        f1.write('NAME : uniform{}\n'.format(num_node))
        f1.write('COMMENT : {}-city problem\n'.format(num_node))
        f1.write('TYPE : TSP\n')
        f1.write('DIMENSION : {}\n'.format(num_node))
        f1.write('EDGE_WEIGHT_TYPE : EUC_2D\n')
        f1.write('NODE_COORD_SECTION\n')
        for i, (x, y) in enumerate(buff):
            f1.write('{} {} {}\n'.format(i+1, x, y))
        f1.write('EOF\n')
    with open('/home/seanyang/Desktop/git/LKH3/LKH-3.0.7/data/tsp{}/uniform{}.par'.format(num_node, num_instance), 'w') as f2:
        f2.write('PROBLEM_FILE = /home/seanyang/Desktop/git/LKH3/LKH-3.0.7/data/tsp{}/uniform{}.tsp\n'.format(num_node, num_instance))
        #f2.write('OPTIMUM = {}\n'.format(opt_value))
        f2.write('MOVE_TYPE = 5\n')
        f2.write('PATCHING_C = 3\n')
        f2.write('PATCHING_A = 2\n')
        f2.write('OUTPUT_TOUR_FILE = /home/seanyang/Desktop/git/LKH3/LKH-3.0.7/results/tsp{}/uniform{}.opt\n'.format(num_node, num_instance))
if __name__ == "__main__":
    num_node = 100
    filename = f"tsp{num_node}_test_concorde.txt"
    f = open(filename)
    for num_instance in range(1,10001):
        tspinstance = f.readline()
        convert_tsplib(tspinstance, num_node, num_instance)
        print('complete th%d instance' %(num_instance))
