# # import win32
# import win32api

# win32api.MessageBox(0, 'Hello, World!, i am learning python', 'Sample_Dialog', 0x00000040)
import win32com.client
# Define the list of names to pronounce
l = ["Biswajit", "Ashish", "Dilip"]
# Initialize the speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")
j=0
for name in l:
    add_shout= "shoutout to"+ l[j]
    j+=1
    speaker.Speak(add_shout)
