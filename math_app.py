from fractions import Fraction
from functools import reduce
math_dictionary={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9',
'ten':'10','eleven':'11','twelve':'12','thirteen':'13','fourteen':'14','fifteen':'15','sixteen':'16','seventeen':'17',
'eighteen':'18','nineteen':'19','twenty':'20','divide':'/','multiply by':'*','plus':'+','minus':'+-','next':'\n','equals':'=',
'times':'*','over':'/','on':'(','off':')','x':'x','y':'y','z':'z'}
variable_dictionary={'x':'x','y':'y','z':'z'}
bracket_dictionary={'a':'a'}
def solve_for_brackets(outsdie_bracket_eqn,inside_bracket_eqn):
    inside_bracket_eqn_simplified=simplify_equation(inside_bracket_eqn)
    outsdie_bracket_eqn_multiplication=outsdie_bracket_eqn.split('*')
    num_list=[]
    variable_list=[]
    multiply_num_list=[]
    inside_bracket_eqn_simplified_plus_multiplied_by_other_things=[]
    for j in outsdie_bracket_eqn_multiplication:
        try:
            num_list.append(int(j))
        except:
            variable_list.append(j)
    multiply_num_list=reduce((lambda x, y: x * y),num_list)
    if len(variable_list)==1:
        inside_bracket_eqn_simplified_plus=inside_bracket_eqn_simplified.split('+')
        if len(inside_bracket_eqn_simplified_plus)==1:
            if inside_bracket_eqn_simplified_plus[0] in variable_dictionary or len(inside_bracket_eqn_simplified_plus[0].split('*'))==2:
                if inside_bracket_eqn_simplified_plus[0] in variable_dictionary:
                    return str(multiply_num_list)+'*'+inside_bracket_eqn_simplified_plus[0]
                elif len(inside_bracket_eqn_simplified_plus[0].split('*'))==2:
                    return str(multiply_num_list*int(inside_bracket_eqn_simplified_plus.split('*')[0])+'*'+inside_bracket_eqn_simplified_plus.split('*')[1])
            else:
                return str(multiply_num_list*int(inside_bracket_eqn_simplified_plus[0]))
        elif len(inside_bracket_eqn_simplified_plus)>1:
            for k in inside_bracket_eqn_simplified_plus:
                inside_bracket_eqn_simplified_plus_multiplied_by_other_things.append(str(multiply_num_list)+'*'+k)
            print(inside_bracket_eqn_simplified_plus_multiplied_by_other_things[0]+'+'+inside_bracket_eqn_simplified_plus_multiplied_by_other_things[1])
            return simplify_equation(inside_bracket_eqn_simplified_plus_multiplied_by_other_things[0]+'+'+inside_bracket_eqn_simplified_plus_multiplied_by_other_things[1])
    else:
        return str(multiply_num_list*int(inside_bracket_eqn_simplified))
    
    
def simplify_equation(eqn):
    left_side=eqn
     
    left_side_plus=left_side.split('+')
    left_side_plus_operator=[]
    last_eqn_list=[]
    last_eqn=''
    coef_list=[]
    if len(left_side_plus)>1:
        if left_side_plus[0]=='+':
            left_side_plus=left_side_plus[1:]
            print(left_side_plus)
        for k in range(len(left_side_plus)-1):
            left_side_plus_operator.append('+')
        for j in left_side_plus:
            last_eqn_list.append(simplify_equation(j))
        final_last_eqn_list=[]
        for w in last_eqn_list:
            if 'a' in w:
                for z in solve_for_brackets(w,a).split('+'):
                    final_last_eqn_list.append(z)
                    if len(solve_for_brackets(w,a).split('+'))>1:
                        left_side_plus_operator.append('+')
                        
            else:
                final_last_eqn_list.append(w)
        print(final_last_eqn_list)
        num_list=[]
        variable_list=[]
        for i in final_last_eqn_list:
            try:
                num_list.append(int(i))
            except:
                variable_list.append(i)
        if left_side[0]=='+':
            variable_list=variable_list[1:]
        print(variable_list)
        print(num_list)
        if (len(variable_list)>1):
            for i in range(len(variable_list)):
                if variable_list[i][0] in variable_dictionary:
                    coef_list.append(1)
                elif variable_list[i][0]=='-' and len(variable_list[i])==2:
                    coef_list.append(-1)
                elif variable_list[i][0]=='-' and len(variable_list[i].split('*'))==2:
                    coef_list.append(int(variable_list[i][0:2]))
                else:
                    coef_list.append(int(variable_list[i].split('*')[0]))

            print(coef_list)
            last_eqn_list=(str(sum(num_list))+'+'+str(sum(coef_list))+'*'+variable_list[-1][-1]).split('+')
            left_side_plus_operator=left_side_plus_operator[:len(last_eqn_list)-1]
            print(last_eqn_list)
            print(left_side_plus_operator)
        else:
            last_eqn_list=(str(sum(num_list))+'+'+variable_list[-1]).split('+')
            left_side_plus_operator=left_side_plus_operator[:len(last_eqn_list)-1]
        if len(last_eqn_list)==len(left_side_plus_operator):
            for w in range(len(last_eqn_list)):
                last_eqn=left_side_plus_operator[w]+last_eqn_list[w]
            return last_eqn
        else:
            for z in range(len(left_side_plus_operator)):
                last_eqn=last_eqn_list[z]+left_side_plus_operator[z]
            return last_eqn+last_eqn_list[-1]
            
    left_side_multiply=left_side.split('*')
    left_side_multiply_operator=[]
    left_side_multiply_variable=''
    left_side_multiply_total=1
    if len(left_side_multiply)==2:
        if left_side_multiply[0][0]=='-':
            if left_side_multiply[0][1] in variable_dictionary:
                return '-'+left_side_multiply[1]+'*'+left_side_multiply[0][1]
            elif left_side_multiply[0][1] not in variable_dictionary:
                return '-'+left_side_multiply[0][1]+'*'+left_side_multiply[1]
            elif left_side_multiply[0][1] not in variable_dictionary and left_side_multiply[1] not in variable_dictionary:
                return '-'+str(eval(left_side_multiply[0][1]+'*'+left_side_multiply[1]))
        else:
            if left_side_multiply[0] in variable_dictionary:
                return left_side_multiply[1]+'*'+left_side_multiply[0]
            elif left_side_multiply[1] in variable_dictionary:
                return left_side_multiply[0]+'*'+left_side_multiply[1]
            elif (left_side_multiply[0] not in variable_dictionary) and (left_side_multiply[1] not in variable_dictionary):
                return str(eval(left_side_multiply[0]+'*'+left_side_multiply[1]))
    elif len(left_side_multiply)>2:
        for k in left_side_multiply:
            if k in variable_dictionary or k in bracket_dictionary:
                left_side_multiply_variable=k
                continue
            else:
                left_side_multiply_total*=int(k)
        if len(left_side_multiply_variable)==1:
            return str(left_side_multiply_total)+'*'+left_side_multiply_variable
        else:
            return str(left_side_multiply_total)
    return left_side
text="start three plus two plus three times on five plus two times x off plus five equals two next"
def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True
def find_answer(eqn1,eqn2):
    for i in eqn1.split('+'):
        try:
            a=int(i)
        except:
            b=int(i.split('*')[0])
    for j in eqn2.split('+'):
        try:
            c=int(j)
        except:
            d=int(j.split('*')[0])
    return((c-a)/(b-0))
    
eqn=''

w= text.split()

if w[0]=='start':
    for i in range(1,len(w)-1):
        if w[i] in math_dictionary:
            eqn+=math_dictionary[w[i]]

print(eqn)
t=eqn.split('=')
left_side = t[0]
right_side = t[1]
left_side_simplified=simplify_equation(left_side)
right_side_simplified=simplify_equation(right_side)
simplified_eqn=left_side_simplified+"="+right_side_simplified
final_answer=find_answer(left_side_simplified,right_side_simplified)
simplify_equation(right_side)
eqn_list=[]
eqn_list.append(left_side)      #eqtn list has both left and right sides (appended together)
eqn_list.append(right_side)


checker= True
while checker:
    user_input=input("Enter the operation:")    #input is taken from user
    user_input_split=user_input.split() #input is taken and put into a list (split along spaces)
    eqn1 = ''
    for i in range(len(user_input_split)-1):              #loop to convert words to math symbols
        if user_input_split[i] in math_dictionary:
            eqn1+=math_dictionary[user_input_split[i]]
          
    if user_input_split[-1] == "stop":
        checker = False
        break
        
    if user_input_split[-1] == "show":
        checker == False  #the loop stops asking for input when the user gives one of the two keywords
        index_w = left_side.index('w')
        left_side_3 = left_side[:index_w] + wl + left_side[index_w+1:]
        
        break
       
    left_side = left_side + eqn1                       #the left and right side are appended by adding the users operaation
    right_side= right_side + eqn1
    temp_append = left_side+'='+ right_side   #a temp append variable is created to keep track of the right and left side 
    
    if (eqn1[0] == '+' and eqn1[1] == '-'):     #the if statement is executed when the operation to perform is subtraction
        for i in range(len(left_side)):
            if(left_side[i] == '+' and left_side[i+1] == '-'):
                index_plus_left = i    #subtraction is performed if the equation includes a consecutive +-
                break
            
        for j in range(len(right_side)):   #the if statement is executed when the operation to perform is addition
            if(right_side[j] == '+' and right_side[j+1] == '-'):
                index_plus_right = j   #addition is performed of the equation includes a + sign
                break
            
        left_side_2 = left_side[:i] + left_side[i+1:]
        right_side_2 = right_side[:j] + right_side[j+1:]
        print(left_side + '=' + right_side)   #after the extra signs are omitted from the equations, the left and right side of the equation are printed
        
    if(eqn1[0] == '+' and eqn1[1] !='-'):    #the total appened equation is only printed when the user asks to subtract a value
           
    

    #the following two if statements perform variable substitution for the brackets in the equation
    if left_side.find('(',0,len(left_side)) !=-1:
        op_brac_left = left_side.index('(')
        cl_brac_left=left_side.index(')')
        wl= left_side[op_brac_left:cl_brac_left+1]
        if cl_brac_left== len(left_side)-1:
            left_side = left_side[:op_brac_left] + 'w'
            
            
        else:
            left_side = left_side[:op_brac_left] + 'w'+ left_side[cl_brac_left+1:]
    
        
    if right_side.find('(',0,len(right_side))!=-1:
        op_brac_right=right_side.index('(')
        cl_brac_right=right_side.index(')')
        wr= right_side[op_brac_right: cl_brac_right+1]
        if cl_brac_right== len(right_side)-1:
            right_side = right_side[:op_brac_right] + '*a'
            
        else:
            right_side = right_side[:op_brac_right] + '*a'+ right_side[cl_brac_right+1:]
    
            
    #once the parenthesis in the function is dealt with, the function is then split along + and placed into a linked list
    left_num_list = []
    left_var_list = []
    variable_eqn=''
    for i in left_side.split('+'):
        try:
            left_num_list.append(int(i))
            
        except:
            left_var_list.append(i)

    variable_eqn="+".join(left_var_list)
    temp_eqn=sum(left_num_list)
    if temp_eqn==0:
        left_side=variable_eqn
    else:
        left_side=str(temp_eqn)+"+"+variable_eqn
    if (is_empty(left_num_list)):    
        coef_list=[]
        for i in range(len(left_var_list)):
            if left_var_list[i][0] in variable_dictionary:
                coef_list.append(1)
            elif variable_list[i][0]=='-' and len(variable_list[i])==2:
                coef_list.append(-1)
            elif variable_list[i][0]=='-' and len(variable_list[i].split('*'))==2:
                coef_list.append(int(variable_list[i][0:2]))
            else:
                coef_list.append(int(variable_list[i].split('*')[0]))
    
    

    #once the parenthesis in the function is dealt with, the function is then split along + and placed into a linked list
    right_num_list = []
    right_var_list = []
    variable_eqn=''
    for i in right_side.split('+'):
        try:
            right_num_list.append(int(i))
            
        except:
            right_var_list.append(i)
            

    variable_eqn="+".join(right_var_list)
    temp_eqn=sum(right_num_list)
    if temp_eqn==0:
        right_side=variable_eqn
    else:
        right_side=str(temp_eqn)+"+"+variable_eqn
    if (is_empty(right_num_list)):    
        coef_2_list=[]
        for i in range(len(right_var_list)):
            if right_var_list[i][0] in variable_dictionary:
                coef_2_list.append(1)
            elif variable_list[i][0]=='-' and len(variable_list[i])==2:
                coef_2_list.append(-1)
            elif variable_list[i][0]=='-' and len(variable_list[i].split('*'))==2:
                coef_2_list.append(int(variable_list[i][0:2]))
            else:
                coef_2_list.append(int(variable_list[i].split('*')[0]))
    print(right_side)
    
    print(left_side + '='+ right_side[:-1])
