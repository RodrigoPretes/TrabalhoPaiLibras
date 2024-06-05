
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
max_images_per_class = 60

while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/A")),
             'b': len(os.listdir(directory+"/B")),
             'c': len(os.listdir(directory+"/C")),
             'd': len(os.listdir(directory+"/D")),
             'e': len(os.listdir(directory+"/E")),
             'f': len(os.listdir(directory+"/F")),
             'g': len(os.listdir(directory+"/G")),
             'h': len(os.listdir(directory+"/H")),
             'i': len(os.listdir(directory+"/I")),
             'j': len(os.listdir(directory+"/J")),
             'k': len(os.listdir(directory+"/K")),
             'l': len(os.listdir(directory+"/L")),
             'm': len(os.listdir(directory+"/M")),
             'n': len(os.listdir(directory+"/N")),
             'o': len(os.listdir(directory+"/O")),
             'p': len(os.listdir(directory+"/P")),
             'q': len(os.listdir(directory+"/Q")),
             'r': len(os.listdir(directory+"/R")),
             's': len(os.listdir(directory+"/S")),
             't': len(os.listdir(directory+"/T")),
             'u': len(os.listdir(directory+"/U")),
             'v': len(os.listdir(directory+"/V")),
             'w': len(os.listdir(directory+"/W")),
             'x': len(os.listdir(directory+"/X")),
             'y': len(os.listdir(directory+"/Y")),
             'z': len(os.listdir(directory+"/Z")),
             'hello': len(os.listdir(directory+"/HELLO")),
             'love': len(os.listdir(directory+"/LOVE")),
             'no': len(os.listdir(directory+"/NO")),
             'thanks': len(os.listdir(directory+"/THANKS")),
             'yes': len(os.listdir(directory+"/YES"))
             }
    # cv2.putText(frame, "a : "+str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "b : "+str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "c : "+str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "d : "+str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "e : "+str(count['e']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "f : "+str(count['f']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "g : "+str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "h : "+str(count['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "i : "+str(count['i']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "k : "+str(count['k']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "l : "+str(count['l']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "m : "+str(count['m']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "n : "+str(count['n']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "o : "+str(count['o']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "p : "+str(count['p']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "q : "+str(count['q']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "r : "+str(count['r']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "s : "+str(count['s']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "t : "+str(count['t']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "u : "+str(count['u']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "v : "+str(count['v']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "w : "+str(count['w']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "x : "+str(count['x']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "y : "+str(count['y']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "z : "+str(count['z']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(50)
    if interrupt & 0xFF == ord('a'):
        if count['a'] < max_images_per_class:
            cv2.imwrite(directory+'A/'+str(count['a'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('b'):
        if count['b'] < max_images_per_class:
            cv2.imwrite(directory+'B/'+str(count['b'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('c'):
        if count['c'] < max_images_per_class:
            cv2.imwrite(directory+'C/'+str(count['c'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('d'):
        if count['d'] < max_images_per_class:
            cv2.imwrite(directory+'D/'+str(count['d'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('e'):
        if count['e'] < max_images_per_class:
            cv2.imwrite(directory+'E/'+str(count['e'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('f'):
        if count['f'] < max_images_per_class:
            cv2.imwrite(directory+'F/'+str(count['f'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('g'):
        if count['g'] < max_images_per_class:
            cv2.imwrite(directory+'G/'+str(count['g'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('h'):
        if count['h'] < max_images_per_class:
            cv2.imwrite(directory+'H/'+str(count['h'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('i'):
        if count['i'] < max_images_per_class:
            cv2.imwrite(directory+'I/'+str(count['i'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('j'):
        if count['j'] < max_images_per_class:
            cv2.imwrite(directory+'J/'+str(count['j'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('k'):
        if count['k'] < max_images_per_class:
            cv2.imwrite(directory+'K/'+str(count['k'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('l'):
        if count['l'] < max_images_per_class:
            cv2.imwrite(directory+'L/'+str(count['l'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('m'):
        if count['m'] < max_images_per_class:
            cv2.imwrite(directory+'M/'+str(count['m'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('n'):
        if count['n'] < max_images_per_class:
            cv2.imwrite(directory+'N/'+str(count['n'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('o'):
        if count['o'] < max_images_per_class:
            cv2.imwrite(directory+'O/'+str(count['o'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('p'):
        if count['p'] < max_images_per_class:
            cv2.imwrite(directory+'P/'+str(count['p'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('q'):
        if count['q'] < max_images_per_class:
            cv2.imwrite(directory+'Q/'+str(count['q'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('r'):
        if count['r'] < max_images_per_class:
            cv2.imwrite(directory+'R/'+str(count['r'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('s'):
        if count['s'] < max_images_per_class:
            cv2.imwrite(directory+'S/'+str(count['s'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('t'):
        if count['t'] < max_images_per_class:
            cv2.imwrite(directory+'T/'+str(count['t'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('u'):
        if count['u'] < max_images_per_class:
            cv2.imwrite(directory+'U/'+str(count['u'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('v'):
        if count['v'] < max_images_per_class:
            cv2.imwrite(directory+'V/'+str(count['v'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('w'):
        if count['w'] < max_images_per_class:
            cv2.imwrite(directory+'W/'+str(count['w'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('x'):
        if count['x'] < max_images_per_class:
            cv2.imwrite(directory+'X/'+str(count['x'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('y'):
        if count['y'] < max_images_per_class:
            cv2.imwrite(directory+'Y/'+str(count['y'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('z'):
        if count['z'] < max_images_per_class:
            cv2.imwrite(directory+'Z/'+str(count['z'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('0'):
        if count['hello'] < max_images_per_class:
            cv2.imwrite(directory+'HELLO/'+str(count['hello'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('1'):
        if count['love'] < max_images_per_class:
            cv2.imwrite(directory+'LOVE/'+str(count['love'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('2'):
        if count['no'] < max_images_per_class:
            cv2.imwrite(directory+'NO/'+str(count['no'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('3'):
        if count['thanks'] < max_images_per_class:
            cv2.imwrite(directory+'THANKS/'+str(count['thanks'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")
    if interrupt & 0xFF == ord('4'):
        if count['yes'] < max_images_per_class:
            cv2.imwrite(directory+'YES/'+str(count['yes'])+'.png',frame)
        else:
            print("Limite de imagens atingido para a classe.")


cap.release()
cv2.destroyAllWindows()