# Shinchan

Shinchan (llama3) -- ollama model llama3 is used for all text generation task and llava is used for Image related tasks

### Quickstart      

Download Ollama -- https://www.ollama.com/      

To run ollama models :-                  
**open cmd and type --**                   
###### ollama run llama3                     
###### ollama run llava         
<br> </br> 
Now Create a file named **Modelfile**, and type below Instrctions to the file, adjust temeperature and system according to your need

FROM llama3

#set the temperature to 1 [higher is more creative, lower is more coherent]                                   
PARAMETER temperature 1

#set the system message                
SYSTEM """                          
You are Shinchan Nohara. Answer as Shinchan, the assistant, only.                        
"""

**Again open Cmd and type --**               
###### ollama create [your model name] -f ./Modelfile          

**Example --** ollama create shinchan -f ./Modelfile

You can use this model in your code 

###### from langchain_community.llms import ollama                              
###### llm = ollama(model = "shinchan")
<br> </br>
### More Examples

For code generator Create a model file 

FROM llama3

#set the temperature to 1 [higher is more creative, lower is more coherent]                                   
PARAMETER temperature 1

#set the system message                
SYSTEM """                          
You are a code teaching teaching assisatnt named as CodeGuru. Answer all the code related questions being asked and generate code for the user.                  
"""

CMD command -- ollama create codeguru -f ./modelfile


              
