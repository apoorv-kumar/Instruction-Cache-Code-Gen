# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="apoorvKumar"
__date__ ="$Jul 9, 2011 4:52:07 PM$"
import code_gen
from params.code_params import CodeParams
from distribution.__init__ import * #all distribution generators
from code_gen.__init__ import * #all code generators



def print_code(list_tup_final):
    print HEADER_DATA


    print 'int main(){'

    #for each code block tuple
    for code_tuple in list_tup_final:
	 #depending upon the type of code , call appropriate print function
        if(code_tuple[0] == 'seq'):
            print_seq_code(code_tuple[1]['length'])

        elif(code_tuple[0] == 'branch'):
            print_branch_code(code_tuple[1]['prob'], code_tuple[1]['length'])

        elif(code_tuple[0] == 'loop'):
            print_iter_code(code_tuple[1]['length'] , code_tuple[1]['iterations'] )

    print 'return 0;'
    print '}'


#cp refers to the input code params.
def generate_code_outline(cp):
    list_tup_final = []#will contain the tuples representing blocks
    #format - (a1 , d1) -
    # a1 - type of block
    # d1 - dictionary containing data about block

    #generate blocks
    #sequence -  ---------------------------------------------------

    nsb = cp.no_seq_blocks
    avsb = cp.avg_seq_size

    uniform_pattern = uniform_int(1, 2*avsb - 1, nsb)

    #generate the list
    for val in uniform_pattern:
        list_tup_final.append( ('seq' , {'length' : val} ) )
    #---------------------------------------------------------------


    #generate blocks
    #iteration-  ---------------------------------------------------

    nlb = cp.no_loop_blocks
    avlb = cp.avg_loop_size
    aviter = cp.avg_loop_iterations


    uniform_pattern_len = uniform_int(1, 2*avlb - 1, nlb)
    uniform_pattern_iter = uniform_int(1, 2*aviter -1 , nlb)

    #generate the list
    for i in range(nlb):
        list_tup_final.append( ('loop' , {'length' : uniform_pattern_len[i] , 'iterations' : uniform_pattern_iter[i] } ) )

    #---------------------------------------------------------------


    #generate blocks
    #branches-  ---------------------------------------------------

    nbb = cp.no_loop_blocks
    avbj = cp.avg_branch_jump
    avpr = cp.avg_branch_prob


    uniform_pattern_len = uniform_int(1, 2*avbj - 1, nbb)
    uniform_pattern_iter = uniform_float(0, 1, nbb)
    #generate the list
    for i in range(nbb):
        list_tup_final.append( ('branch' , {'length' : uniform_pattern_len[i] , 'prob' : uniform_pattern_iter[i] } ) )

    #---------------------------------------------------------------



    #now randomly shuffle the list - mix up blocks
    random.shuffle(list_tup_final)
    return  list_tup_final



def main():
    cp = CodeParams()



    list_tup_final = generate_code_outline(cp)
    #start printing the code
    print_code(list_tup_final)




if __name__ == "__main__":
    main()
