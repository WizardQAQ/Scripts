import numpy as np
import re

class vasp_file:
    def __init__(self, Filename, pattern=['[Ss]elective|s|S', u'[Cc]artesian|[Dd]irect', '😊']):
        self.Filename = Filename
        self.pattern = pattern
    def find_pattern(self, private_pattern):
        with open('./{}'.format(self.Filename), mode='r') as f:
            num_line = 0
            for i in f.readlines():
                a = re.findall(pattern=private_pattern, string=i)
                if a:
                    break
                else:
                    num_line = num_line + 1
        f.close()
        return num_line
    def get_elem_inf(self):
        elements = np.loadtxt('./{}'.format(self.Filename), skiprows=5, max_rows=1, dtype=str)
        quantities_element = np.loadtxt('./{}'.format(self.Filename), skiprows=6, max_rows=1, dtype=int)
        num = np.sum(quantities_element)
        return elements, quantities_element, num
    def get_line_DC_num(self):
        if vasp_file(self.Filename).find_pattern(self.pattern[2]) \
            == vasp_file(self.Filename).find_pattern(self.pattern[0]):
            #print('there is not Selective in {POS|CONT}CAR.\n Return the line number of Direct or Car')
            return [vasp_file(self.Filename).find_pattern(self.pattern[1])]
        else:
            return vasp_file(self.Filename).find_pattern(self.pattern[0]), \
                vasp_file(self.Filename).find_pattern(self.pattern[1])
    def get_apnd_labl(self):
        elements = self.get_elem_inf()[0]
        quantities_element = self.get_elem_inf()[1]
        if elements.size == 1:
            append_row = np.tile(elements[0], quantities_element[0])
        else:
            i = 1
            append_row = np.tile(elements[0], quantities_element[0])
            while i < elements.size:
                append_row = np.concatenate((append_row, np.tile(elements[i], quantities_element[i])))
                i +=1
        return append_row
    def get_op_matrix(self):
        matrx = np.loadtxt(
                            './{}'.format(self.Filename), 
                            skiprows=self.get_line_DC_num()[-1] + 1,
                            dtype=float,
                            max_rows=self.get_elem_inf()[2],
                            usecols=(0,1,2)
                            )
        return matrx
    def get_cell_matrix(self):
        cell_matrix = np.loadtxt(
            './{}'.format(self.Filename),skiprows=2, max_rows=3
        )
        return cell_matrix
    def get_title(self):
        title = np.loadtxt(self.Filename, max_rows=1, dtype=str)
        return title

pos = vasp_file('POSCAR')
con = vasp_file('CONTCAR')
print('diff between end and beginning is\n {}'.format(con.get_op_matrix()-pos.get_op_matrix()))
