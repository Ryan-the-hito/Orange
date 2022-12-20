w1 = window_about()  # about
w2 = window_update()  # update
w3 = window3()  # main1
w3.setAutoFillBackground(True)
p = w3.palette()
p.setColor(w3.backgroundRole(), QColor('#ECECEC'))
w3.setPalette(p)
w4 = window4()  # main2
action1.triggered.connect(w1.activate)
action2.triggered.connect(w2.activate)
action3.triggered.connect(w3.activate)
action4.triggered.connect(w4.activate)
action6.triggered.connect(w3.News_find)
action8.triggered.connect(w3.rest_siz)
action9.triggered.connect(w3.clear_tot)
button_action.triggered.connect(w3.activate)
w3.btn0_1.clicked.connect(w4.activate)
app.setStyleSheet(style_sheet_ori)
app.exec()
