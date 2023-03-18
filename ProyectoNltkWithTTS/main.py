import pyttsx3
from Clase import *
                                 
converter = pyttsx3.init()          
                    
converter.setProperty('rate', 150)    
                    
converter.setProperty('volume', 0.6)
                          
converter.say(summary)
                       
converter.runAndWait()


                    

                    

                     
                    



                    



                    



