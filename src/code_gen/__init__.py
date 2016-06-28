from branch_code import *
from seq_code import *
from iter_code import *
from headers import *

__author__="apoorvKumar"

#generate seq_code --------------------------------------------------------------------------------
#select the best seq code (or combinations of them)
def generate_seq_code(code_length):
    sorted_seq_code = sorted(SEQ_CODE_LIST , key= lambda _seq_code: _seq_code.code_length )

    sequence = []#sequence of tuples of code to be inserted to generate code of desired length
    done  = False
    remaining_lines = code_length
    current_code_index = 0

    while not done:
        #reset condition
        if(current_code_index >= len(sorted_seq_code) ):
            current_code_index = 0


        #see if suff lines
        if(remaining_lines > sorted_seq_code[current_code_index].code_length):
            lines = sorted_seq_code[current_code_index].code_length
        else:
            lines = remaining_lines

        sequence.append( (sorted_seq_code[current_code_index] , lines) )
        remaining_lines = remaining_lines - lines

        if(remaining_lines <= 0):
            done = True
        else:
            current_code_index = current_code_index +1


    #sequence now contains all information about what and
    #how and how much of lines are to be arranged

    #final_code_str will contain the final code merging all
    final_code_str = str

    #all codes are dumped in this list
    list_final_code = []

    for tuple_code_len in sequence:
        str_of_code = tuple_code_len[0].get_part_code(tuple_code_len[1]) # [0] - is code , [1] is the required length
        list_final_code.append('\n{')#mark start of a block
        list_final_code.append(str_of_code)
        list_final_code.append('}\n')#end of block


    final_code_str = ''.join(list_final_code)

    return  final_code_str


#--------------------------------------------------------------------------------------------------



#print seq_code --------------------------------------------------------------------------------
#just a wrapper for seq_generate
#select the best seq code (or combinations of them)
def print_seq_code(code_length):
    code = generate_seq_code(code_length)
    print code

#--------------------------------------------------------------------------------------------------



#print branch code ----------------------------------------------------------------------------
#inputs - br_prb , internal_code , seq_lim (if any)
#selects the br_prb code as per seq code overhead allowance
#

#TODO - this function is not scalable - generalize it.
def print_branch_code(branch_probability , branch_code_len , seq_limit = 10000):
    #get samples of each class
    c1 = BranchCode1()
    c2 = BranchCode2()
    c3 = BranchCode3()

    list_tup_code_ovh = [(c1 , c1.seq_overhead) , (c2 , c2.seq_overhead) , (c3 , c3.seq_overhead)]

    sorted_list = sorted(list_tup_code_ovh , key=lambda this_tuple: this_tuple[1] )

    limit_pos = -1 #all are greater than limit

    for overhead_tuple in sorted_list:
        if ( overhead_tuple[1] < seq_limit):
            limit_pos = limit_pos+1
        else:
            break

    #now we know where our limit lies in list.
    #all elements at and to left of limit_pos are valid

    if limit_pos == -1 :
        limit_pos = 0 #no option but to choose it

    chosen_code_pos = random.randint(0 , limit_pos)

    chosen_code = sorted_list[chosen_code_pos][0]

    internal_code = generate_seq_code(branch_code_len)

    chosen_code.print_output_code(internal_code , branch_probability)

    return {'seq_overhead' : chosen_code.seq_overhead}

#--------------------------------------------------------------------------------------------------


#generate iter_code -------------------------------------------------------------------------------
#selects the best iter code
#inserts padding of seq code to reach iter_code_length
#scalable code - gets list of iter codes

def print_iter_code(iter_code_length , iterations):
    ic_list = ITER_CODE_LIST

    #sort - key is iter_code_len
    sorted_ic_list = sorted(ic_list , key=lambda in_iter_code: in_iter_code.iter_code_len)

    #find max pos : ic_list[pos].length < iter_code_len
    #all on and to the left of it are acceptable
    #TODO - linear search ... can do better
    limit_pos = -1 #none qualify
    for ic in sorted_ic_list:
        if ic.iter_code_len < iter_code_length:
            limit_pos = limit_pos + 1
        else:
            break

    #see if no codes are valid
    if (limit_pos == -1):
        limit_pos = 0

    #choose at random
    choice_index = random.randint(0 , limit_pos)
    choice_code = sorted_ic_list[choice_index]

    pad_line_count = iter_code_length - choice_code.iter_code_len

    if pad_line_count > 0:
        pad_str = generate_seq_code(pad_line_count)
    else:
        pad_str = ''

    #print final code
    choice_code.print_final_code(pad_str , iterations)


#--------------------------------------------------------------------------------------------------



# ========================== testing stuff ===========================
def main():
    #generate_branch_code(.5, '', 40)
    print_iter_code(33 , 33)
    print '-----------------------------------------------'
    print_branch_code(.1, 21, 43)
    print '-----------------------------------------------'
    print_seq_code(22)


if(__name__ == '__main__'):
    main()
