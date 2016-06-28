# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="apoorvKumar"
__date__ ="$Jul 9, 2011 6:05:43 PM$"

class CodeParams:
    no_seq_blocks = int
    no_branches = int
    no_loop_blocks = int

    #avg_loop_complx = int
    avg_seq_size = int
    avg_loop_size = int
    avg_branch_prob = float
    avg_loop_iterations = int
    avg_branch_jump = int

    def __init__(self):
        self.no_seq_blocks = 30
        self.no_branches = 5
        self.no_loop_blocks = 10

        #self.avg_loop_complx = 2
        self.avg_seq_size = 10
        self.avg_loop_size = 30
        self.avg_branch_prob = .5

        self.avg_loop_iterations = 10
        self.avg_branch_jump = 20




if __name__ == "__main__":
    print "The params module"
