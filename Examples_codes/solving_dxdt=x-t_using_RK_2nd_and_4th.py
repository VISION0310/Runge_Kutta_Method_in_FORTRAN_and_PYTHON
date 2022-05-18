###############################################################################
######                                                                   ######
######  METHOD OF SOLVING ORDINARY DIFFERETIAL EQUATION IN TWO VARIABLE  ######
######                                                                   ######
###############################################################################

'''
    Defining the function dx/dt = f(t,x) as a input function, where

    t : float or integer [independent_variable]
    x : float or integer [dependent variable]

    There are two ways for defining f(t,x) function:
    a) using "def function_name(parameter[s])".
    b) using inbuild "lambda" function in python.

    Both of which is shown below-

    ###########################################################################
    # The expression in below two function can be change as per the requirement #
    ###########################################################################

'''
'''
    First method: a) Using "def function_name(parameter[s])"
'''
################################################################################
def input_function(independent_variable_t, dependent_variable_x):               # defining f(t,x), where (x) and (t) are parameters.
  dxdt = dependent_variable_x - independent_variable_t                          # f(t,x) = experssion or equation that are required 
  return dxdt                                                                   # to solve for a given (t) and (x). For example here "dxdt = x-t"    
################################################################################

'''
    Second method: b) Using inbuild "lambda" function in python as-
    function_name = lambda variable[1], variable[2]: expression 
    for example, here, expression = f(t,x) = dx/dt = x-t

'''
################################################################################
input_function_lambda = lambda independent_variable_t, dependent_variable_x: (
                                  dependent_variable_x - independent_variable_t)
################################################################################
'''
    for example- as our f(t,x) = x-t,
    both are giving same result
'''
print("using 'def' function    :", input_function(87,8))
print("using 'lambda' function :", input_function_lambda(87,8))


################################################################################
################################################################################
'''
    R-K 2nd and 4th Order Method of Solving ODE
  
    sol_time_t        : float or integer  ---> time at which solution needed (t)
    initial_time_t0   : float or integer  ---> initial time (t0)
    initial_value_x0  : float or integer  ---> initial value (x0), at initial time (t0)
    time_step_h       : float or integer  ---> time steps of iteration (h)
  
'''
###################  R-K 2nd Order Method of Solving ODE  ######################
def rk2(sol_time_t, initial_time_t0, initial_value_x0, time_step_h):                
               
  if time_step_h > sol_time_t:                                                                      #
    raise Exception("ERROR...! time_step_h should be smaller than or equal to sol_time_t")          #
                                                                                                    #
  for number_of_iteration in range(round((sol_time_t - initial_time_t0)/ time_step_h)):             # 
    k1 = time_step_h * input_function( initial_time_t0, initial_value_x0 )                          #
    k2 = time_step_h * input_function( initial_time_t0 + time_step_h, initial_value_x0 + k1 )       #
    solution = initial_value_x0 + (1./2.) * ( k1 + k2 )                                             #
    initial_value_x0 = solution                                                                     #
    initial_time_t0 += time_step_h                                                                  #
  return solution, number_of_iteration+1                                                            #
################################################################################


###################  R-K 4th Order Method of Solving ODE  ######################
def rk4(sol_time_t, initial_time_t0, initial_value_x0, time_step_h):                
               
  if time_step_h > sol_time_t:                                                                            #
    raise Exception("ERROR...! time_step_h should be smaller than or equal to sol_time_t")                #
                                                                                                          #
  for number_of_iteration in range(round((sol_time_t - initial_time_t0)/ time_step_h)):                   # 
    k1 = time_step_h * input_function( initial_time_t0, initial_value_x0 )                                #
    k2 = time_step_h * input_function( initial_time_t0 + (time_step_h / 2), initial_value_x0 + (k1 / 2) ) #
    k3 = time_step_h * input_function( initial_time_t0 + (time_step_h / 2), initial_value_x0 + (k2 / 2) ) #
    k4 = time_step_h * input_function( initial_time_t0 + time_step_h, initial_value_x0 + k3 )             #
    solution = initial_value_x0 + (1./6.) * ( k1 + 2*k2 + 2*k3 + k4 )                                     #
    initial_value_x0 = solution                                                                           #
    initial_time_t0 += time_step_h                                                                        #
  return solution, number_of_iteration+1
################################################################################


sol_time_t        = 0.2
initial_time_t0   = 0
initial_value_x0  = 2
time_step_h       = 0.1

RK_2 = rk2(sol_time_t, initial_time_t0, initial_value_x0, time_step_h)
RK_4 = rk4(sol_time_t, initial_time_t0, initial_value_x0, time_step_h)

print('solution by RK2 : ',RK_2[0], ', with no. of iteration ',RK_2[1])           ## index 0 in RK_2[0] and RK_4[0] represent solution
print('solution by RK4 : ',RK_2[0], ', with no. of iteration ',RK_4[1])           ## index 1 in RK_2[1] and RK_4[1] represent number of iteration
