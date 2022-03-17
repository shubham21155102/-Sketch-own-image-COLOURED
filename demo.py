from sketchpy import canvas
obj = canvas.trace(img_path='shubham.jpg',zoom=5,scale=1)
#obj.trace()
pen= canvas.sketch(x_offset=370)
pen.draw_fn("hair",co=(27, 26, 29),mode=0)
pen.draw_fn("face_outline",co=(230, 162, 114),mode=0)

pen.draw_fn("right_ear",co=(141, 88, 57),mode=0)
pen.draw_fn("eye_brow",co=(32, 27, 26),mode=0)
pen.draw_fn("left_eye",co=(149, 136, 135),mode=0)
pen.draw_fn("right_eye",co=(149, 136, 135),mode=0)
pen.draw_fn("right_eye_middle",co=(13, 10, 12),mode=0)
pen.draw_fn("left_eye_middle",retain=True,co=(13, 10, 12),mode=0)
