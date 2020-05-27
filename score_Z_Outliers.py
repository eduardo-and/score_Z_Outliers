# Function that calculate outliers values with Score-Z
import math
import re

# Treats the inputs whether they are passed as a parameter or through the keyboard
# Return a float list
def treat_input(inpt=""):  # Types accepted: list,string,tuple,set
    # Clear empty values in list
    def clear_empty(sqc):
        for val in sqc:
            if(val==""):
                sqc.remove(val)
                clear_empty(sqc)
        return sqc
   
    # Function that performs the treatment of strings and vectors, removing unwanted elements
    def split_str(sqc):
        if(type(sqc) == str):
            sqc = sqc.split(",")
        else:
            sqc = [str(val) for val in sqc]
        
        sqc= clear_empty(sqc)
        sqc = [re.sub(r"[^0-9 | \.]", "", val) for val in sqc]
        data = [float(val) for val in sqc]

        return sorted(data)
    
    # Verifica se algum componente da lista é um string
    def str_vrfy(sqc):
        flag = True
        for x in sqc:
            if(type(x) == str):
                flag = False
        return flag

    # Verifiy if exist a entrace in parameter and if the entrace is a valid type
    if(not inpt == ""):
        flag = str_vrfy(inpt)
        if((type(inpt) == list or type(inpt) == tuple or type(inpt) == set) and flag == True):
            return sorted(inpt)
        else: return split_str(inpt)
    else:
      inpt = input("Enter your data set separated by comma: ")
      return split_str(inpt)

# Calculate the outliers with the list received in treat_input()
# Return false if the list not contain outliers, and a list of outliers if there is
def calcule_outliers(inpt=""): 
    data = treat_input(inpt)
   
    # Calculate average of list
    def average(data):
        av = 0
        for x in data:
            av += x

        av = av/len(data)
        return av
   
    # Calculate Standart Deviation of list
    def dP(data, avg):
        # Calculate the variance of list
        def variance(data, avg):
            sum_uni = 0
            for val in data:
                sum_uni += (val-avg)**2

            V = sum_uni/len(data)
            return V

        return math.sqrt(variance(data, avg))
   
    #search the outliers of list
    def outliers(data,dp,avg):
        otl= False
               
        for val in data:
            
            if((val-avg)/dp < -3 or (val-avg)/dp > 3):
                otl=float(val)
                
        return otl
  
    avg = average(data)
    data= outliers(data,dP(data, avg),avg)
      
    if(not data):
        return False
   
    return data

def clear_outliers(inpt):
    out=calcule_outliers(inpt)
    inpt=treat_input(inpt)
    
    if(type(out)==float):
        inpt.remove(out)
        inpt = clear_outliers(inpt)

    return inpt

def recursive_outliers(inpt):
    temp=[]
    
    def recurse(inpt,temp): 
        ret=calcule_outliers(inpt)
        inpt=treat_input(inpt)
        if(ret):
            temp.append(ret)
            inpt.remove(ret)
            temp = recurse(inpt,temp)
        
        return temp
    
    out=recurse(inpt,temp)
    return out
    