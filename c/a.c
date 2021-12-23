#include <stdio.h>
#include <stdlib.h>

unsigned int unsigned_global = 0xFFFFFFFF;
void function_1(int parameter_1, int *parameter_2, int **parameter_3)
{								             
    parameter_1 += 1; 
    *parameter_2 = 0x2;  
    *parameter_3 = &parameter_1;  
  	(**parameter_3)++;      
    *parameter_3 = parameter_2;
    (**parameter_3)++; 

    printf("function_1: %x, %x, %x\n", parameter_1, *parameter_2, **parameter_3); 
}

int main()
{
    int local_variable = 0xDEADBEEF; 
    static int *local_pointer = NULL;
    local_pointer = &local_variable;

    function_1((int)unsigned_global, &local_variable, &local_pointer);
	
    printf("main: %x, %x, %x\n", local_variable, unsigned_global, *local_pointer);
    return 0;
}