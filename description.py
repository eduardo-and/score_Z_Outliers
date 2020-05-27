import score_Z_Outliers

out = score_Z_Outliers

#1. out.treat_input(list)
#    Input: Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set
#    Return: List with trated data

#2. out.calcule_outliers(list)
#    Input: Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set
#    Return: Float number with a outliers presents in data envitated in input
         
#3. out.clear_outliers(list)     
#    Input: Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set
#    Return: New List with out outliers
#   
#    Description: The function remove outliers using recursive form of the function calculate_outliers. 
#    There is no limit to removals   

#4. out.recursive_outliers(list)     
#    Input: Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set
#    Return: List with outliers extracted of recursive form
#   
#    Description: The function extract outliers using recursive form of the function calculate_outliers. 
#    There is no limit to extractions  

# Note: 
#   It is not necessary to use function (1)out.treat_input before using the other functions, they already perform the treatment in input.

#EXEMPLES:

x= [12,26,64,12,3,45,12250,1,22,42,32,46,25,14,36] #Just 1 outlier
y= ["1a",1,"232.q1","15","125","1aasd.5","23",13] # Erroneous Input and with out outliers
z= [-12566,56, 16, 6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49,122363] # 2 outliers


print(f'\nThe original arrays are:\n x={x}\n y={y}\n z={z}')

print(f'\nAfter tratament with treat_input()):\n x= {out.treat_input(x)}\n y= {out.treat_input(y)}\n z= {out.treat_input(z)}')

print(f'\nThe outliers present in arrys are(out.calcule_outliers()):\n x = {out.calcule_outliers(x)}\n y = {out.calcule_outliers(y)}\n z = {out.calcule_outliers(z)}')

print(f'\nThe lists with ou outliers are(out.clear_outliers()):\n x = {out.clear_outliers(x)}\n y = {out.clear_outliers(y)}\n z = {out.clear_outliers(z)}')

print(f'\nThe new lists with all the outliers are(out.recursive_outliers()):\n x = {out.recursive_outliers(x)}\n y = {out.recursive_outliers(y)}\n z = {out.recursive_outliers(z)}\n')

