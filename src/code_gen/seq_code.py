     # ----------------------------------
     # --- pure returns - no direct IO --
     # ----------------------------------

__author__="apoorvKumar"

# --------- the seq code class -----------------

class SeqCode:
    code_text = list
    code_length = int

    def copy(self):
        _seq_code = SeqCode()
        _seq_code.code_length = self.code_length
        _seq_code.code_text = self.code_text
        return  _seq_code

    #returns a string
    def get_part_code(self , lines):
        split_code_text = self.code_text.split('\n')

        if(lines > self.code_length):
            return self.code_text
        else:
            #return merged string with sliced no of lines
            return '\n'.join(split_code_text[0:lines-1])

# ----------------------------------------------


#------------- the final list -----
SEQ_CODE_LIST = []
#---------------------------------


# ------------------------------ iteration 1 --------------------------

#----------------- set values ----------
code_text ="""int dummy1 = 10 , dummy2 = 100;
int TimeUsed = 100;
int* my_int_ptr_1 = &dummy1;
int* my_int_ptr_2 = &dummy2;
(*my_int_ptr_1) ++ ;
(*my_int_ptr_2) ++ ;
dummy1 = TRUE ;
dummy1 = dummy1 + (dummy1 - dummy2) / CLK_TCK  ;
double Accuracy = *my_int_ptr_1* 100 / *my_int_ptr_2 ;
double Speed = *my_int_ptr_1/ 5 / (TimeUsed / 60) ;
int WrongInput = *my_int_ptr_2 - *my_int_ptr_1;
size_t ratio = sizeof(Accuracy)/sizeof(WrongInput);"""

code_length = 12
#--------------------------------------------

seq_code = SeqCode()


# -------- assign values --------------------
seq_code.code_length = code_length
seq_code.code_text =  code_text
# --------------------------------------------

#CAVEAT -
#YOU CANNOT USE THE SAME VARIABLE TO APPEND EACH OF CODE
#BECAUSE IT'S THE POINTER THAT GETS APPENDED.
#YOU NEED TO CREATE A (DEEP/shallow)COPY IF YOU WANT TO ALTER THE VARIABLE
# ------------- append code set to final  -----------------
copy_seq_code = seq_code.copy()
SEQ_CODE_LIST.append(copy_seq_code)
#----------------------------------------------------------




# ------------------------------ iteration 2 --------------------------

#----------------- set values ----------
code_text ="""int to_be_swapped1 , to_be_swapped2 , interm;
interm = to_be_swapped1;
to_be_swapped1 = to_be_swapped2;
to_be_swapped2 = interm;"""

code_length = 4
#--------------------------------------------

# -------- assign values --------------------
seq_code.code_length = code_length
seq_code.code_text =  code_text
# --------------------------------------------


# ------------- append code set to final  -----------------
copy_seq_code = seq_code.copy()
SEQ_CODE_LIST.append(copy_seq_code)
#----------------------------------------------------------





# ------------------------------ iteration 3 --------------------------

#----------------- set values ----------
code_text ="""struct DummyStruct ds1 , ds2;
ds1.st_var_char = 'a';
ds1.st_var_db = 667.8;
ds1.st_var_flt = 234.33;
ds1.st_var_int = 345;
ds2.st_var_char = ds1.st_var_char;
ds2.st_var_int = ds1.st_var_int;
ds2.st_var_flt = ds1.st_var_flt;
ds2.st_var_db = ds1.st_var_db;"""

code_length = 9
#--------------------------------------------

# -------- assign values --------------------
seq_code.code_length = code_length
seq_code.code_text =  code_text
# --------------------------------------------


# ------------- append code set to final  -----------------
copy_seq_code = seq_code.copy()
SEQ_CODE_LIST.append(copy_seq_code)
#----------------------------------------------------------



# --------------- test stuff ---------------------
if __name__ == '__main__':
    main()

def main():
    print SEQ_CODE_LIST



