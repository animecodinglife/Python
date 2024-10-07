# Global and local variable
'''
A variables scope refers to the particular places it is accessible within the code of a given program 



Global variable exits outside of functions. 

Local variables exist within functions.
'''

glb_var="global"

def var_function():
    lc_var ="local"
    print(lc_var)
    print(glb_var)

    var_function()

    print(glb_var)