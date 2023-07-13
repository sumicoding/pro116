import cv2

img = cv2.imread("C:/Users/dell/Downloads/PRO-C116-project-image-main-main/PRO-C116-project-image-main-main/solar-system.jpg")
cv2.imshow("output",img)

cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (20,30),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5
            (255,255,255)
            )