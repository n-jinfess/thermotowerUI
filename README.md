
  
Functions:
def prepareframe(frame): 
•	Returns a grayscale any frame. 
def detecteyes(frame_VL): 
•	runs a haar cascade classifier on grayscale visible light camera frame. 
•	Returns ‘eyes’, which will have the dimensions in x,y,w,h format.  
def drawrect(frame,eyes):
•	based on ‘eyes’ detected in def detect(frame) a rectangle is drawn on frame.  
•	Returns a frame with rectangles drawn surrounding the eyes. 
def transferdimen(frame_ir ,eyes):  
•	transfers dimensions of rectangle to the frames from thermal camera.  
•	Returns eyes_IR, which is the proportional rectangle coordinates of the eyes on the thermal frame.
def drawrectIR(frame_ir_eyes):  
•	draws rectangle on thermal frame. 
•	Returns a thermal frame with rectangle drawn. 
 def gettemp(frame_ir,eyes):  
•	Pixels within rectangle are averaged calculated to represent an accurate temperature.
•	 Returns temperature in Fahrenheit. 

def puttext(frame,frame_ir,eyes,temperature): 
•	Temperature is placed above surrounding rectangle. 
•	Returns the two frame types with temperature placed above the rectangles.
