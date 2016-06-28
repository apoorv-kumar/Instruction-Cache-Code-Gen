import random

__author__="apoorvKumar"

def get_type_name(name):
    if(name == 'string'):
        return 'char*'
    else:
        return name

# ------------- the itercode class -----------------
#should have used the __init__ to generate code ... not manually
class IterCode:
    iter_code_text = tuple # of strings ... size = 2 ... add padding in between
    iter_code_len = int
    non_iter_code_len = int
    comments = str
    param_count = int
    param_type_list = list #of 2-tuples (name , type)
    iter_count_param = int #starting from 1 ; index of param that controls iteration

    def get_val(self , type):
        if (type == 'int' ):
            return 131313
        elif( type == 'float' ):
            return 1313.13
        elif( type == 'string'):
            return '-- this is a test string --'

    def get_string(self , length):
        char_opts = ['a' , 'b' , 'c' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , '$' ,'#']

        list_chars = [] #will contain chars before being appended
        final_str = ''

        for i in range(length):
            sel_index = random.randint(0 , len(char_opts) - 1)
            list_chars.append(char_opts[sel_index])

        final_str = ''.join(list_chars)
        return final_str




    def print_header(self , iterations):
        #this is an abstract class fn
        #do not call
        assert False

    def print_final_code(self , str_padding , iterations):
        print '{'
        self.print_header(iterations)
        print self.iter_code_text[0]
        print str_padding
        print self.iter_code_text[1]
        print '}'


# --------------------------------------------------


#------------- the final list -----
ITER_CODE_LIST = []
#---------------------------------

# ------------------------------ iteration 1 --------------------------

class IterCode1(IterCode):
    def __init__(self):
        self.iter_code_len = 2
        self.param_count = 2
        self.iter_code_text = (

        """
        {
            int sum = 1 , var = 1;
            for (int i = 1 ; i <= terms ; i++)
            {
                var *= x/i;
                sum += var;

        """
        , #add padding here

        """
            }
        }
        """ )

        self.comments = """
            /*
             * characteristics -
             * length of iterative code - 2 lines
             * summation and mult
             * non iterative overhead - 1 line
             *
             * data access pattern
             * very close accesses
             * constant miss time
             */
        """

        self.param_type_list = [ ('x' , 'float') , ('terms' , 'int') ]

        self.iter_count_param = 2

        self.non_iter_code_len = 3

    def print_header(self , iterations):
        print get_type_name(self.param_type_list[self.iter_count_param - 1][1]), \
        self.param_type_list[self.iter_count_param - 1][0] , '=' , iterations , ';'
        #hard-coding
        print get_type_name(self.param_type_list[0][1]), \
         self.param_type_list[0][0] , '=' ,  self.get_val(self.param_type_list[0][1]) , ';'



#------ create new instance and append -----
ITER_CODE_LIST.append(IterCode1())
#---------------------------------


#- -------------------------------------------------------------------


# ------------------------------ iteration 2 --------------------------


class IterCode2(IterCode):
    def __init__(self):
        self.iter_code_len = 2
        self.param_count = 2
        self.iter_code_text = ("""

        {
           unsigned int b    = 378551;
           unsigned int a    = 63689;
           unsigned int hash = 0;
           unsigned int i    = 0;

           for(i = 0; i < len; str++, i++)
           {
              hash = hash * a + (*str);
              a    = a * b;

              """ , """

           }


        }
        /* End Of RS Hash Function */
        """)

        self.comments = """
                /*
     * an additive hash function
     *
     * input - string with it's length
     * out - hash for the string
     *
     * iterative code - 2 lines
     * seq overhead - 4 lines
     *
     * data access -
     * mostly sequential - for the string
     * some persistent data like defined variables
     *
     */
        """

        self.param_type_list = [ ('str' , 'string') , ('len' , 'int') ]

        self.iter_count_param = 2

        self.non_iter_code_len = 5

    def print_header(self , iterations):
        print get_type_name(self.param_type_list[self.iter_count_param - 1][1]), \
        self.param_type_list[self.iter_count_param - 1][0] , '=' , iterations , ';'
        #hard-coding
        print get_type_name(self.param_type_list[0][1]), \
        self.param_type_list[0][0] , '=' , '\"' +  self.get_string(iterations) + '\";'



#------ create new instance and append -----
ITER_CODE_LIST.append(IterCode2())
#---------------------------------

#- -----------------------------------------------------------------------


# ------------------------------ iteration 3 --------------------------


class IterCode3(IterCode):
    def __init__(self):
        self.iter_code_len = 1
        self.param_count = 2
        self.iter_code_text = ("""
        {


           unsigned int hash = 1315423911;
           unsigned int i    = 0;

           for(i = 0; i < len; str++, i++)
           {
              hash ^= ((hash << 5) + (*str) + (hash >> 2));

              """ , """

           }


        }
        /* End Of JS Hash Function */
        """)

        self.comments = """
        /*
         * an rotative  hash function
         *
         * input - string with it's length
         * out - hash for the string
         *
         * iterative code - 1 lines
         * seq overhead - 2 lines
         *
         * data access -
         * mostly sequential - for the string
         * some persistent data like defined variables
         *
         */
    """

        self.param_type_list = [ ('str' , 'string') , ('len' , 'int') ]

        self.iter_count_param = 2

        self.non_iter_code_len = 4

    def print_header(self , iterations):
        print get_type_name(self.param_type_list[self.iter_count_param - 1][1]), \
        self.param_type_list[self.iter_count_param - 1][0] , '=' , iterations , ';'
        #hard-coding
        print get_type_name(self.param_type_list[0][1]), \
        self.param_type_list[0][0] , '=' , '\"' +  self.get_string(iterations) + '\";'



#------ create new instance and append -----
ITER_CODE_LIST.append(IterCode3())
#---------------------------------

#- -------------------------------------------------------------------


# ------------------------------ iteration 4  --------------------------

class IterCode4(IterCode):
    def __init__(self):
        self.iter_code_len = 1
        self.param_count = 2
        self.iter_code_text = ("""
        {

           const unsigned int BitsInUnsignedInt = (unsigned int)(sizeof(unsigned int) * 8);
           const unsigned int ThreeQuarters     = (unsigned int)((BitsInUnsignedInt  * 3) / 4);
           const unsigned int OneEighth         = (unsigned int)(BitsInUnsignedInt / 8);
           const unsigned int HighBits          = (unsigned int)(0xFFFFFFFF) << (BitsInUnsignedInt - OneEighth);
           unsigned int hash              = 0;
           unsigned int test              = 0;
           unsigned int i                 = 0;

           for(i = 0; i < len; str++, i++)
           {
              hash = (hash << OneEighth) + (*str);

              if((test = hash & HighBits)  != 0)
              {
                 hash = (( hash ^ (test >> ThreeQuarters)) & (~HighBits));
              }

              """ , """
           }

        }
        /* End Of  P. J. Weinberger Hash Function */
        """)

        self.comments = """
        /*
         * a rotative  hash function
         *
         * input - string with it's length
         * out - hash for the string
         *
         * iterative code - 2 lines
         * seq overhead - 7 lines
         * branches taken - no of iterations
         * branch size - 1 line
         *
         * data access -
         * mostly sequential - for the string
         * some persistent data like defined variables
         *
         */

    """

        self.param_type_list = [ ('str' , 'string') , ('len' , 'int') ]

        self.iter_count_param = 2

        self.non_iter_code_len = 9

    def print_header(self , iterations):
        print get_type_name(self.param_type_list[self.iter_count_param - 1][1]), \
        self.param_type_list[self.iter_count_param - 1][0] , '=' , iterations , ';'
        #hard-coding
        print get_type_name(self.param_type_list[0][1]), \
        self.param_type_list[0][0] , '=' , '\"' +  self.get_string(iterations) + '\";'



#------ create new instance and append -----
ITER_CODE_LIST.append(IterCode4())
#---------------------------------

# ------------------------------ iteration 5  --------------------------

class IterCode5(IterCode):
    def __init__(self):
        self.iter_code_len = 1
        self.param_count = 2
        self.iter_code_text = ("""
        {

           unsigned int seed = 131; /* 31 131 1313 13131 131313 etc.. */
           unsigned int hash = 0;
           unsigned int i    = 0;

           for(i = 0; i < len; str++, i++)
           {
              hash = (hash * seed) + (*str);

              """ , """
           }

        }
        /* End Of BKDR Hash Function */
        """)

        self.comments = """

        /*
         * charateristics -
         * length of iterative code - 1 line
         * summation and mult
         * non iterative overhead - 3 line
         *
         * data access pattern
         * linear string traversal
         * very close accesses
         * constant miss time
         */


    """

        self.param_type_list = [ ('str' , 'string') , ('len' , 'int') ]

        self.iter_count_param = 2

        self.non_iter_code_len = 5

    def print_header(self , iterations):
        print get_type_name(self.param_type_list[self.iter_count_param - 1][1]), \
        self.param_type_list[self.iter_count_param - 1][0] , '=' , iterations , ';'
        #hard-coding
        print get_type_name(self.param_type_list[0][1]), \
        self.param_type_list[0][0] , '=' , '\"' +  self.get_string(iterations) + '\";'



#------ create new instance and append -----
ITER_CODE_LIST.append(IterCode5())
#---------------------------------

#- -------------------------------------------------------------------


# ------------------------------ iteration 6  --------------------------


class IterCode6(IterCode):
    def __init__(self):
        self.iter_code_len = 1
        self.param_count = 2
        self.iter_code_text = ("""
        {



           unsigned int hash = 0;
           unsigned int i    = 0;

           for(i = 0; i < len; str++, i++)
           {
              hash = (*str) + (hash << 6) + (hash << 16) - hash;

              """ , """

           }


        }
        /* End Of SDBM Hash Function */



        """)

        self.comments = """

        /*
         * charateristics -
         * length of iterative code - 1 lines
         * summation and mult
         * non iterative overhead - 2 line
         *
         * data access pattern
         * very close accesses
         * constant miss time
         */

    """

        self.param_type_list = [ ('str' , 'string') , ('len' , 'int') ]

        self.iter_count_param = 2

        self.non_iter_code_len = 4


    def print_header(self , iterations):
        print get_type_name(self.param_type_list[self.iter_count_param - 1][1]), \
        self.param_type_list[self.iter_count_param - 1][0] , '=' , iterations , ';'
        #hard-coding
        print get_type_name(self.param_type_list[0][1]), \
        self.param_type_list[0][0] , '=' , '\"' +  self.get_string(iterations) + '\";'



#------ create new instance and append -----
ITER_CODE_LIST.append(IterCode6())
#---------------------------------

#- -------------------------------------------------------------------




# ------------------------------ iteration 7  --------------------------

class IterCode7(IterCode):
    def __init__(self):
        self.iter_code_len = 1
        self.param_count = 2
        self.iter_code_text = ("""

        {



           const unsigned int fnv_prime = 0x811C9DC5;
           unsigned int hash      = 0;
           unsigned int i         = 0;

           for(i = 0; i < len; str++, i++)
           {
              hash *= fnv_prime;
              hash ^= (*str);

              """ , """

           }

        }
        /* End Of FNV Hash Function */

        """)

        self.comments = """

        /*
         * charateristics -
         * length of iterative code - 2 lines
         * summation and mult
         * non iterative overhead - 3 line
         *
         * data access pattern
         * very close accesses
         * constant miss time
         */

    """


        self.param_type_list = [ ('str' , 'string') , ('len' , 'int') ]

        self.iter_count_param = 2

        self.non_iter_code_len = 4

    def print_header(self , iterations):
        print get_type_name(self.param_type_list[self.iter_count_param - 1][1]), \
        self.param_type_list[self.iter_count_param - 1][0] , '=' , iterations , ';'
        #hard-coding
        print get_type_name(self.param_type_list[0][1]), \
        self.param_type_list[0][0] , '=' , '\"' +  self.get_string(iterations) + '\";'


#------ create new instance and append -----
ITER_CODE_LIST.append(IterCode7())
#---------------------------------

#- -------------------------------------------------------------------


# --------------- testing stuff ---------------------


def main():
    print ITER_CODE_LIST
    code = IterCode1()
    code.print_final_code('', 6)

    code = IterCode2()
    code.print_final_code('//padding here', 21)


if __name__ == '__main__':
    main()

