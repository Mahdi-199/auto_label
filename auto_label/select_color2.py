import cv2

def click_data(event, x, y, flags, param):

    if (event == cv2.EVENT_LBUTTONDOWN):
        # print(x,' , ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX;
        blue = img[x,y,0];
        green = img[x,y,1];
        red = img[x,y,2];
        text = str(red) + ',' + str(green) + ',' + str(blue);
        font = cv2.FONT_HERSHEY_SIMPLEX;
        cv2.putText(img,text,(x,y),font,1,(0,255,255),1,cv2.LINE_AA);
        cv2.imshow('imagename',img);
        print('color of selected pixel in RGB space = ', red, green, blue)
    # return red, green, blue


if __name__ == '__main__':

    path = 'test.png';
    img = cv2.imread(path); 
    cv2.imshow('imagename',img); 
    cv2.setMouseCallback('imagename',click_data);
    cv2.waitKey(0);
    cv2.destroyAllWindows();
