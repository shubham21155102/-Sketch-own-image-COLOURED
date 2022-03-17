from tkinter import Canvas
from  sketchpy import canvas as cv

obj = cv.trace(img_path='sbm.jpeg',zoom=1,scale=1)
pen= cv.sketch(x_offset=370)
#obj.trace()
pen.draw_fn("hair",co=(8,10,13),mode=0)
pen.draw_fn("face_outline",co=(239, 197, 173),mode=0)
pen.draw_fn("nose",co=(232, 187, 158),mode=0)
pen.draw_fn("right_eye",co=(223, 207, 192),mode=0)
pen.draw_fn("left_eye",co=(223, 207, 192),mode=0)
pen.draw_fn("left_eyebrow",co=(7, 5, 3),mode=0)
pen.draw_fn("right_eyebrow",co=(7, 5, 3),mode=0)
pen.draw_fn("left_eye_gola",co=(67, 48, 37),mode=0)


pen.draw_fn("right_eye_gola",co=(67, 48, 37),mode=0)

pen.draw_fn("dot_left_eye",co=(45, 28, 24),mode=0)
pen.draw_fn("dot_right_eye",co=(45, 28, 24),mode=0)
pen.draw_fn("left_nose_hole",co=(33, 0, 0),mode=0)
pen.draw_fn("right_nose_hole",co=(33, 0, 0),mode=0)
pen.draw_fn("mochh",co=(8,10,13),mode=0)
pen.draw_fn("hoth",retain=True,co=(183, 137, 121),mode=0)





