import touchio
import board

touch_L = touchio.TouchIn(board.TOUCH_EL)
touch_L.threshold += 5000
touch_R = touchio.TouchIn(board.TOUCH_ER)
touch_R.threshold += 5000
touch_1 = touchio.TouchIn(board.TOUCH_T1)
touch_1.threshold += 5000
touch_2 = touchio.TouchIn(board.TOUCH_T2)
touch_2.threshold += 5000
touch_3 = touchio.TouchIn(board.TOUCH_T3)
touch_3.threshold += 5000
touch_4 = touchio.TouchIn(board.TOUCH_T4)
touch_4.threshold += 5000
touch_5 = touchio.TouchIn(board.TOUCH_T5)
touch_5.threshold += 5000
touch_6 = touchio.TouchIn(board.TOUCH_T6)
touch_6.threshold += 5000
