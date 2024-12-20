def f(a,b):
    if a > 0: 
       return a+b
    else: 
        return a-b

def g(a,b):
      if b < 0: 
        return f(a,-b)
      else: 
         return f(a,b)