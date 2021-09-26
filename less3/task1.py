import math

first_val=input('enter first var: ')
sec_val=input('enter second var: ')

########################################################

def check_type(inpu_val):
    try:
        int(inpu_val)
    except Exception:
            try:
                float(inpu_val)
            except Exception:
                var=inpu_val
            else:
                if math.trunc(float(inpu_val)) in range(3,21):
                    var=float(inpu_val)
                else:
                   var=inpu_val
    else:
        if int(inpu_val) in range(3,21):
            var=int(inpu_val)
        else:
            var=inpu_val
        
    return(var)



########################################################

var_f=check_type(first_val)
var_s=check_type(sec_val)

if str in (type(var_f),type(var_s)):
    print(str(var_f)+str(var_s))
else:
    print(var_f+var_s)
