from django.shortcuts import render,HttpResponse,redirect

def home(request):
 with open("phonebook.txt" , "a+") as f:
     f.seek(0)
     text = f.read()
     return HttpResponse(f"<h2>phone book :</h2>{text}<hr>")
 
 
def add_name(request,name,number):
   with open("phonebook.txt" , "a") as f: 
      f.write(f"{name} : {number}<hr>")
   return HttpResponse(f"shomare {name} sabt shod.")
     
     
     
def remove_name(request,name):
 with open("phonebook.txt" , "a+") as f: 
      f.seek(0)
      lines = f.readlines()
      
 new_lines = []
 for line in lines:
    if not line.startswith(name):
        new_lines.append(line)
 with open("phonebook.txt","w") as f: 
  f.writelines(new_lines)
            
 return HttpResponse(f"shomare {name} pak shod.") 
         
                
     
     
     