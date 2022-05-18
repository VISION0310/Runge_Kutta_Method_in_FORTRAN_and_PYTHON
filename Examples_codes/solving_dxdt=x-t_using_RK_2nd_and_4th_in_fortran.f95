!###############################################################################
!######                                                                   ######
!######  METHOD OF SOLVING ORDINARY DIFFERETIAL EQUATION IN TWO VARIABLE  ######
!######                                                                   ######
!###############################################################################

program RUNGE_KUTTA_METHOD
      IMPLICIT NONE      
      
      ! vaiable declaration

      REAL, external ::  input_function
      REAL :: sol_time_t, initial_time_t0, initial_value_x0, time_step_h, k1, k2, k3, k4, rk2_solution, rk4_solution
      INTEGER :: number_of_iteration , iteration
      
      !initializing some variables
      
      sol_time_t = 0.2      
      initial_time_t0 = 0.0 
      initial_value_x0 = 2.0
      time_step_h = 0.1 

!*****************       R-K 2nd and 4th Order Method of Solving ODE     ********************
!
!     sol_time_t        : float or integer  ---> time at which solution needed (t)
!     initial_time_t0   : float or integer  ---> initial time (t0)
!     initial_value_x0  : float or integer  ---> initial value (x0), at initial time (t0)
!     time_step_h       : float or integer  ---> time steps of iteration (h)
!********************************************************************************************

      number_of_iteration = int((sol_time_t - initial_time_t0) / time_step_h)
      print*, 'Number_of_iteration : ',number_of_iteration

! R-K 2nd Order Method of Solving ODE
!
!      DO iteration=1, number_of_iteration
!              k1 = time_step_h * input_function( initial_time_t0 , initial_value_x0)
!              k2 = time_step_h * input_function( initial_time_t0 + time_step_h , initial_value_x0 + k1 )
!              initial_value_x0 = initial_value_x0 + (1./2.)*(k1 + k2)                           
!              initial_time_t0 = initial_time_t0 + time_step_h
!      END DO
!      rk2_solution = initial_value_x0
!      print*, '"Solution at time : "f10.6, " with RK4 is: " f10.6', sol_time_t, rk2_solution

! R-K 4th Order Method of Solving ODE

      DO iteration=1, number_of_iteration
              k1 = time_step_h * input_function( initial_time_t0, initial_value_x0 )                               
              k2 = time_step_h * input_function( initial_time_t0 + (time_step_h / 2.), initial_value_x0 + (k1 / 2.) ) 
              k3 = time_step_h * input_function( initial_time_t0 + (time_step_h / 2.), initial_value_x0 + (k2 / 2.) ) 
              k4 = time_step_h * input_function( initial_time_t0 + time_step_h, initial_value_x0 + k3 )             
              initial_value_x0 = initial_value_x0 + (1./6.) * ( k1 + 2*k2 + 2*k3 + k4 )                                                                                                                
              initial_time_t0  = initial_time_t0 + time_step_h 
              
      END DO
      rk4_solution = initial_value_x0
      print*, "Solution at time : " , sol_time_t
      print*, "Solution with RK4 is: ", rk4_solution
end program RUNGE_KUTTA_METHOD
!*******************************************************************
!    Defining the function dx/dt = f(t,x) as a input function, where
!
!    t : float [independent_variable]
!    x : float [dependent variable]
!
!    Here, f(t,x) = x - t
!
!********************************************************************

real FUNCTION input_function(independent_variable_t, dependent_variable_x) result(expression_dxdt)

        REAL :: independent_variable_t, dependent_variable_x

        expression_dxdt = dependent_variable_x-independent_variable_t
        
END FUNCTION
