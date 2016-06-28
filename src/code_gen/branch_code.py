import random
__author__="apoorvKumar"

# --------- the branch code class -----------------
#ABSTRACT

#this will be inherited by all branch codes
#this is implemented using inheritance because
#every bcode has a different generator
class BranchCode:
    count_params = int
    branch_param_list = list
    branch_select_code = str
    seq_overhead = int

    def generate_branch(self):
        print "this is an abstract function: to be implemented in child"
        assert False

    def print_output_code(self , internal_code  , prob_of_branch):
        print '{'
        self.generate_branch(prob_of_branch)
        print '    {'
        print internal_code
        print '    }'
        print '}'

# ----------------------------------------------


# --------- branch code 1 ------------------------
class BranchCode1(BranchCode):


    def __init__(self):
        self.branch_select_code = "if((button&1)==1)"
        self.count_params = 1
        self.branch_param_list = ["button"]
        self.seq_overhead = 1

    def generate_branch(self , prob_of_branch):
        prob_of_branch = int(100*prob_of_branch) #rounded percent
        rand_var = random.randint(1 , 100)
        even_val = 224
        odd_val = 17

        #get the val
        final_val = int
        if (rand_var < prob_of_branch):
            final_val = even_val
        else:
            final_val = odd_val

        print "int" , "button = " , final_val , ";"
        print self.branch_select_code

# --------------------------------------------------

# --------- branch code 2 ------------------------
class BranchCode2(BranchCode):


    def __init__(self):
        self.branch_select_code = "if((corx>0&&corx<var_x)&&(cory>0&&cory<var_y))"
        self.count_params = 2
        self.branch_param_list = ['corx' , 'cory']
        self.seq_overhead = 4

    def generate_branch(self , prob_of_branch):
        prob_of_branch = int(100*prob_of_branch) #rounded percent

        rand_var = int(random.random()*100)
        rand_var = 100 - rand_var%prob_of_branch
        corx_prob = rand_var

        #once corx_prob is found ... we use corx_prob*cory_prob = prob(x,y)
        cory_prob = (prob_of_branch*100)/corx_prob

        #get branch probs
        var_x = 100 - corx_prob
        var_y = 100 - cory_prob

        #gen rands in 0 to 100 ... so percent values hold
        corx = random.randint(0 , 100)
        cory = random.randint(0 , 100)

        #corx in 0 to var_x -> prob = var_x/100
        #cory in 0 to var_y -> prob = var_y/100

        print 'int' , "var_x = "  , var_x , ';'
        print 'int' ,'var_y = ' , var_y , ';'
        print 'int' ,'cory = ' , cory, ';'
        print 'int' ,'corx = ' , corx , ';'
        print self.branch_select_code



# --------------------------------------------------

# --------- branch code 3 ------------------------
class BranchCode3(BranchCode):


    def __init__(self):
        self.branch_select_code = "if((x!=x1)&&(x!=x2))"
        self.count_params = 1
        self.branch_param_list = ['x']
        self.seq_overhead = 3

    def generate_branch(self , prob_of_branch):
        prob_of_branch = int(100*prob_of_branch) #rounded percent

        range_amp = int(1/prob_of_branch)
        x= random.randint(1 , 1313)

        r_max = x - range_amp
        r_min = x - range_amp

        x1 = random.randint(r_min , r_max)
        x2 = random.randint(r_min , r_max)

        #print the stuff
        print 'int' , 'x = ' , x , ';'
        print 'int' , 'x1 = ' , x1 , ';'
        print 'int' , 'x2 = ' , x2 , ';'
        print self.branch_select_code
# --------------------------------------------------

# ================================= testing stuff ================================

def main():
    bc1 = BranchCode1()
    bc2 = BranchCode2()

    bc1.print_output_code('', .2)
    bc2.print_output_code('', .5)

if( __name__ == '__main__'):
    main()
