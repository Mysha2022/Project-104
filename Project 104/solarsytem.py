import cv2

img=cv2.imread("solar-system.jpg")

sun="Sun"
cv2.putText(
    img,
    sun,
    (100,150),
    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=2,
    color=(0,0,255)
)

mercury="Mercury"
cv2.putText(
    img,
    mercury,
    (110,250),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

venus="Venus"
cv2.putText(
    img,
    venus,
    (190,250),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

earth="Earth"
cv2.putText(
    img,
    earth,
    (290,258),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

mars="Mars"
cv2.putText(
    img,
    mars,
    (380,250),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

jupiter="Jupiter"
cv2.putText(
    img,
    jupiter,
    (500,360),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

saturn="Saturn"
cv2.putText(
    img,
    saturn,
    (750,300),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

uranus="Uranus"
cv2.putText(
    img,
    uranus,
    (950,290),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

neptune="Neptune"
cv2.putText(
    img,
    neptune,
    (1100,290),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=0.5,
    color=(255,255,255)
)

cv2.imwrite("solar-system_with_names.jpg",img)
cv2.imshow("display image",img)
cv2.waitKey(0)