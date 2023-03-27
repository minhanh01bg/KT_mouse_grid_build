import speech_recognition
import pyttsx3
from datetime import datatime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True: # cái này để mình và robot giao tiếp liên tục thay vì nói 1 câu chương trình đã kết thúc.
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    
    print("Robot:...")
 
    try:
        you = robot_ear.recognizer_google(audio)
    except:
        you = ""

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "Hello" in you: # in you này thay vì chúng ta nói Hello sẽ trả ra 
    #"Hello python thì nó sẽ kiểm tra là trong câu mà bạn nói có từ Hello hay không ?
        robot_brain = "Hello Python"
    elif "Today" in you:
        today = datetime.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "Time" in you:
        now = datetime.today()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "goodbye" in you: ## đoạn này khi nói goodbye thì chương trình sẽ tắt thay vì mở liên tục khi ở phía trên
        robot_brain = "Good Bye"
        break
    else:
        robot_brain = "I'm fine thank you and you"

print("Robot:" + robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

