import re, base64  
   
filename = "./test.eml"  

num_lines = sum(1 for line in open(filename))  

S = ""  
with open(filename, "r") as f:  
    for i in range(0, num_lines-1):  
        if (re.findall("Content-Type: ", f.readline())):  
            i = i + 2  
            f.readline()  
            if(re.findall("Content-Transfer-Encoding: base64", f.readline())):  
                f.readline()  
                while(1):  
                    tmp = f.readline()+f.readline()  
                    if (re.findall("\n\n", tmp)):  
                        break  
                    S = S+tmp  

data = base64.b64decode(S)
html_content = str(data.decode("utf-8"))

with open(filename+"_convert.html", "w", encoding="utf-8") as con_f:  
    con_f.write(html_content)  

print(html_content)