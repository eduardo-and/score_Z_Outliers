# Score Z Outliers

**Author:** Eduardo de Andrade;

**Languages/Tools/Frameworks:** Python
 
**Date:** 27/05/2020

**Description:**
Library that calculate outliers values with Score-Z

### **Run:**
  - #### 1. Move the file score_Z_Outliers.py for inside of your python project and import the library in the file you want to use the library:<br>
              
              import score_Z_Outliers<br>
              
              out= score_Z_Outliers
              
  - #### 2.Use as desired functions. The library contains 4 functions:
    -  ###  **out.treat_input(list)**
    
          **Input:** Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set.<br>
          **Return:** List with trated and ordered data<br>

        
    - ### **out.calcule_outliers(list)**
    
        **Input:** Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set<br>

        **Return:** Float number with a outliers presents in data envitated in input<br>

         
    - ###  **out.clear_outliers(list)**     
    
        **Input:** Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set<br>
        
        **Return:** New List with out outliers <br>

        **Description:** The function remove outliers using recursive form of the function calculate_outliers. <br>

        There is no limit to removals   

     - ###  **out.recursive_outliers(list)**    
        **Input**: Receive a sequence of numbers(float/integer) Types accepted: list,string,tuple,set<br>

        **Return:** List with outliers extracted of recursive form<br>

        **Description:** The function extract outliers using recursive form of the function calculate_outliers. 

        There is no limit to extractions <br> 
        
      - #### **Note:** 
        It is not necessary to use function out.treat_input before using the other functions, they already perform the treatment in input.<br>
### **Exemples:**
        
  &nbsp;&nbsp; **Import and define arrays:**
               
              import score_Z_Outliers

              out = score_Z_Outliers              
                
              x= [12,26,64,12,3,45,12250,1,22,42,32,46,25,14,36] #Just 1 outlier
              y= ["1a",1,"232.q1","15","125","1aasd.5","23",13] # Erroneous Input and with out outliers
              z= [-12566,56, 16, 6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49,122363] # 2 outliers
              
              
 &nbsp;&nbsp;  **treat_input:**
                  
               print('After tratament with treat_input()):')
               print(f'x= {out.treat_input(x)}')
               print(f'y= {out.treat_input(y)}')
               print(f'z= {out.treat_input(z)}')
      
&nbsp;&nbsp;Output:
   
            After tratament with treat_input()):
            x= [1, 3, 12, 12, 14, 22, 25, 26, 32, 36, 42, 45, 46, 64, 12250]
            y= [1.0, 1.0, 1.5, 13.0, 15.0, 23.0, 125.0, 232.1]
            z= [-12566, 6, 7, 15, 16, 36, 39, 40, 41, 42, 43, 47, 49, 56, 122363]
  
&nbsp;&nbsp;  **calcule_outliers:**
  
            print('The outliers present in arrys are(out.calcule_outliers()):')
            print(f'x = {out.calcule_outliers(x)}')
            print(f'y = {out.calcule_outliers(y)}')
            print(f'z = {out.calcule_outliers(z)}')
    
   &nbsp;&nbsp;Output:
   
            The outliers present in arrys are(out.calcule_outliers()):
            x = 12250.0
            y = False
            z = 122363.0
   
   &nbsp;&nbsp;**clear_outliers:**
   
            print(f'\nThe lists with ou outliers are(out.clear_outliers()):') 
            print(f'x = {out.clear_outliers(x)}')
            print(f'y = {out.clear_outliers(y)}')
            print(f'z = {out.clear_outliers(z)}')
      
  &nbsp;&nbsp;Output:
              
            The lists with ou outliers are(out.clear_outliers()):
            x = [1, 3, 12, 12, 14, 22, 25, 26, 32, 36, 42, 45, 46, 64]
            y = [1.0, 1.0, 1.5, 13.0, 15.0, 23.0, 125.0, 232.1]
            z = [6, 7, 15, 16, 36, 39, 40, 41, 42, 43, 47, 49, 56]
            
  &nbsp;&nbsp; **recursive_outliers:**
            
              print('The new lists with all the outliers are(out.recursive_outliers()):')
              print(f'x = {out.recursive_outliers(x)}')
              print(f'y = {out.recursive_outliers(y)}')
              print(f'z = {out.recursive_outliers(z)}')
              
   &nbsp;&nbsp;output:     
                
              The new lists with all the outliers are(out.recursive_outliers()):
              x = [12250.0]
              y = []
              z = [122363.0, -12566.0]
             

**To run the examples on your machine, move the example.py file into your project and run.**
