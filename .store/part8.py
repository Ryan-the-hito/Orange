class window3(QWidget):  # 主程序的代码块
    def __init__(self):
        super().__init__()
        self.dragPosition = self.pos()
        self.initUI()

    def initUI(self):  # 设置窗口内布局
        self.setUpMainWindow()
        MOST_WEIGHT = int(self.screen().availableGeometry().width() * 0.75)
        HALF_WEIGHT = int(self.screen().availableGeometry().width() / 2)
        MINI_WEIGHT = int(self.screen().availableGeometry().width() / 4)

        DE_HEIGHT = int(self.screen().availableGeometry().height() - 30)
        HALF_HEIGHT = int(self.screen().availableGeometry().height() * 0.5)
        HEIGHT = int(self.screen().availableGeometry().height())

        self.resize(MINI_WEIGHT, DE_HEIGHT)
        self.center()
        self.setWindowTitle("News!")
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setMinimumSize(MINI_WEIGHT, HALF_HEIGHT)
        self.setMaximumSize(MOST_WEIGHT, HEIGHT)

    def setUpMainWindow(self):
        self.description_box = QWidget()

        t0 = QWidget()
        self.btn0_1 = QPushButton('', self)
        self.btn0_1.setFixedSize(25, 25)
        self.btn0_1.setStyleSheet('''
        QPushButton{
        border: transparent;
        background-color: transparent;
        border-image: url(add.png);
        }
        QPushButton:pressed{
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
        }
        ''')
        self.btn0_2 = QPushButton('', self)
        self.btn0_2.setFixedSize(25, 25)
        self.btn0_2.clicked.connect(self.News_find)
        self.btn0_2.setStyleSheet('''
        QPushButton{
        border: transparent;
        background-color: transparent;
        border-image: url(re.png);
        }
        QPushButton:pressed{
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
        }
        ''')
        b0 = QHBoxLayout()
        b0.setContentsMargins(0, 0, 0, 0)
        b0.addStretch()
        b0.addWidget(self.btn0_1)
        b0.addWidget(self.btn0_2)
        t0.setLayout(b0)

        # lbl1 = QLabel('By time:', self)
        self.checkBox1 = QCheckBox('By time:', self)

        t1 = QWidget()
        self.widget1 = QComboBox(self)
        self.widget1.setCurrentIndex(0)
        self.widget1.addItems(['Day', '01', '02', '03', '04', '05',
                               '06', '07', '08', '09', '10', '11',
                               '12', '13', '14', '15', '16',
                               '17', '18', '19', '20', '21',
                               '22', '23', '24', '25', '26',
                               '27', '28', '29', '30', '31'])
        lbl1_1 = QLabel('-', self)
        self.widget2 = QComboBox(self)
        self.widget2.setCurrentIndex(0)
        self.widget2.addItems(['Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
                               'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov',
                               'Dec'])
        lbl1_2 = QLabel('- ', self)
        self.le1 = QLineEdit(self)
        self.le1.setPlaceholderText('Year')
        self.le1.setFixedHeight(20)
        b1 = QHBoxLayout()
        b1.setContentsMargins(0, 0, 0, 0)
        b1.addWidget(self.widget1)
        b1.addWidget(lbl1_1)
        b1.addWidget(self.widget2)
        b1.addWidget(lbl1_2)
        b1.addWidget(self.le1)
        t1.setLayout(b1)

        # lbl2 = QLabel('By entity:', self)
        self.checkBox2 = QCheckBox('By entity:', self)
        self.checkBox2.stateChanged.connect(self.lock_topic)

        self.widget3 = QComboBox(self)
        self.widget3.setCurrentIndex(0)
        self.widget3.addItems(['All essential entities (default)',
                               '🇩🇿 Algeria',
                               '🇦🇺 Australia',
                               '🇦🇹 Austria',
                               '🇧🇷 Brazil',
                               '🇧🇾 Belarus',
                               '🇨🇦 Canada',
                               '🇨🇱 Chile',
                               "🇨🇳 People's Republic of China",
                               '🇫🇷 France',
                               '🇩🇪 Germany',
                               '🇮🇩 Indonesia',
                               '🇮🇱 Israel',
                               '🇮🇳 India',
                               '🇮🇷 Iran',
                               '🇯🇵 Japan',
                               "🇰🇵 Democratic People's Republic of Korea",
                               '🇰🇷 Republic of Korea',
                               '🇱🇧 Lebanon',
                               '🇲🇲 Myanmar',
                               '🇲🇾 Malaysia',
                               '🇳🇮 Nicaragua',
                               '🇵🇭 Philippines',
                               '🇵🇰 Pakistan',
                               '🇷🇺 Russian Federation',
                               '🇸🇩 Sudan',
                               '🇸🇬 Singapore',
                               '🇸🇳 Senegal',
                               '🇹🇭 Thailand',
                               '🇺🇳 UN',
                               '🇬🇧 United Kingdom of Great Britain and Northern Ireland',
                               '🇺🇸 United States of America',
                               '🇻🇳 Vietnam',
                               '🎌 Taiwan'])

        # lbl3 = QLabel('By keywords:', self)
        self.checkBox3 = QCheckBox('By keywords:', self)

        t3 = QWidget()
        self.le3 = QLineEdit(self)
        self.le3.setPlaceholderText('Use comma to seperate keywords')
        self.le3.setFixedHeight(20)
        b3 = QHBoxLayout()
        b3.setContentsMargins(0, 0, 0, 0)
        b3.addWidget(self.le3)
        t3.setLayout(b3)

        # lbl4 = QLabel('By topics:', self)
        self.checkBox4 = QCheckBox('By topics:', self)

        t4_1 = QWidget()
        lbl4 = QLabel(' ', self)
        lbl4.setFixedWidth(10)
        self.checkBox5 = QCheckBox('', self)
        self.checkBox5.setFixedWidth(20)
        self.checkBox5.stateChanged.connect(self.change_check)
        self.widget4 = QComboBox(self)
        self.widget4.setCurrentIndex(0)
        self.widget4.addItems(['Topics in Chinese'])
        self.widget4.currentIndexChanged.connect(self.topic_link)
        b4_1 = QHBoxLayout()
        b4_1.setContentsMargins(0, 0, 0, 0)
        b4_1.addWidget(lbl4)
        b4_1.addWidget(self.checkBox5)
        b4_1.addWidget(self.widget4)
        t4_1.setLayout(b4_1)

        t4_2 = QWidget()
        lbl5 = QLabel(' ', self)
        lbl5.setFixedWidth(10)
        self.checkBox6 = QCheckBox('', self)
        self.checkBox6.setFixedWidth(20)
        self.checkBox6.stateChanged.connect(self.change_check)
        self.checkBox6.stateChanged.connect(self.lock_topic)
        self.widget5 = QComboBox(self)
        self.widget5.setCurrentIndex(0)
        self.widget5.addItems(['Topics in English'])
        self.widget5.currentIndexChanged.connect(self.topic_link)
        b4_2 = QHBoxLayout()
        b4_2.setContentsMargins(0, 0, 0, 0)
        b4_2.addWidget(lbl5)
        b4_2.addWidget(self.checkBox6)
        b4_2.addWidget(self.widget5)
        t4_2.setLayout(b4_2)

        t5 = QWidget()
        self.btn5_1 = QPushButton('Search!', self)
        self.btn5_1.clicked.connect(self.Only_search)
        self.btn5_1.setStyleSheet('''
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
''')
        self.btn5_1.setMaximumHeight(20)
        b5 = QHBoxLayout()
        b5.setContentsMargins(0, 0, 0, 0)
        b5.addWidget(self.btn5_1)
        t5.setLayout(b5)

        self.t5_1 = QWidget()
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.lbl5_1 = QLabel('   ', self)
        b5_1 = QHBoxLayout()
        b5_1.setContentsMargins(0, 0, 0, 0)
        b5_1.addWidget(self.pbar)
        b5_1.addWidget(self.lbl5_1)
        self.t5_1.setLayout(b5_1)
        self.t5_1.setVisible(False)

        t6 = QWidget()
        btn5_2 = QPushButton('Clear', self)
        btn5_2.clicked.connect(self.clear_shal)
        btn5_2.setMaximumHeight(20)
        btn6_1 = QPushButton('Export to', self)
        btn6_1.clicked.connect(self.export_all)
        btn6_1.setMaximumHeight(20)
        '''btn6_2 = QPushButton('Focus mode', self)
        btn6_2.clicked.connect(self.focuson3)
        btn6_2.setMaximumHeight(20)'''
        b6 = QHBoxLayout()
        b6.setContentsMargins(0, 0, 0, 0)
        b6.addWidget(btn5_2, 1)
        b6.addWidget(btn6_1, 1)
        #b6.addWidget(btn6_2, 1)
        t6.setLayout(b6)

        font = PyQt6.QtGui.QFont()
        font.setBold(True)
        self.checkBox1.setFont(font)
        self.checkBox2.setFont(font)
        self.checkBox3.setFont(font)
        self.checkBox4.setFont(font)

        wings_h_box = QVBoxLayout()
        wings_h_box.setContentsMargins(0, 0, 0, 0)
        wings_h_box.addWidget(t0)
        wings_h_box.addWidget(self.checkBox1)
        wings_h_box.addWidget(t1)
        wings_h_box.addWidget(self.checkBox2)
        wings_h_box.addWidget(self.widget3)
        wings_h_box.addWidget(self.checkBox3)
        wings_h_box.addWidget(t3)
        wings_h_box.addWidget(self.checkBox4)
        wings_h_box.addWidget(t4_2)
        wings_h_box.addWidget(t4_1)
        wings_h_box.addWidget(self.t5_1)
        wings_h_box.addWidget(t5)
        wings_h_box.addWidget(t6)
        self.description_box.setLayout(wings_h_box)

        t8 = QWidget()
        b8 = QVBoxLayout()
        b8.setContentsMargins(0, 0, 0, 0)
        b8.addWidget(self.description_box)
        b8.addStretch()
        t8.setLayout(b8)

        self.t9 = QWidget()
        self.b9 = QVBoxLayout()
        self.b9.setContentsMargins(5, 0, 0, 25)
        self.middle_list = QListWidget(self)
        self.middle_list.itemClicked.connect(self.Item_click)
        self.b9.addWidget(self.middle_list)
        self.t9.setLayout(self.b9)
        self.t9.setVisible(False)

        self.t10 = QWidget()
        self.b10 = QVBoxLayout()
        self.b10.setContentsMargins(5, 0, 0, 25)
        self.news_window = QTextEdit(self)
        self.b10.addWidget(self.news_window)
        self.t10.setLayout(self.b10)
        self.t10.setVisible(False)

        page2_box_h = QHBoxLayout()
        page2_box_h.setContentsMargins(20, 20, 20, 20)
        page2_box_h.addWidget(t8, 1)
        page2_box_h.addWidget(self.t9, 1)
        page2_box_h.addWidget(self.t10, 1)
        self.setLayout(page2_box_h)

    def enterEvent(self, event):
        SCREEN_WEIGHT = int(self.screen().availableGeometry().width())
        WINDOW_WEIGHT = int(self.width())
        x, y = pag.position()
        if self.pos().x() + WINDOW_WEIGHT >= SCREEN_WEIGHT and x > SCREEN_WEIGHT - 2 and self.underMouse():  # 右侧显示
            self.move_window(SCREEN_WEIGHT - WINDOW_WEIGHT + 2, self.pos().y())
            event.accept()
        elif self.pos().x() <= 0 and x < 2 and self.underMouse():  # 左侧显示
            self.move_window(0, self.pos().y())
            event.accept()

    def leaveEvent(self, event):
        SCREEN_WEIGHT = int(self.screen().availableGeometry().width())
        WINDOW_WEIGHT = int(self.width())
        if self.pos().x() + WINDOW_WEIGHT >= SCREEN_WEIGHT:  # 右侧隐藏
            self.move_window(SCREEN_WEIGHT - 2, self.pos().y())
            event.accept()
        elif self.pos().x() <= 2:  # 左侧隐藏
            self.move_window(2 - WINDOW_WEIGHT, self.pos().y())
            event.accept()

    def move_window(self, width, height):
        animation = QPropertyAnimation(self, b"geometry", self)
        animation.setDuration(250)
        new_pos = QRect(width, height, self.width(), self.height())
        animation.setEndValue(new_pos)
        animation.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.dragPosition)

    def News_find(self):
        home_dir = str(Path.home())
        tarname1 = "OrangeAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "DoNotDelete.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        tarname3 = "news_ori.txt"
        fulldir3 = os.path.join(fulldir1, tarname3)
        if not os.path.exists(fulldir2):
            with open(fulldir2, 'a', encoding='utf-8') as f0:
                f0.write('')
        if not os.path.exists(fulldir3):
            with open(fulldir3, 'a', encoding='utf-8') as f00:
                f00.write('')
        exsfeeds = codecs.open(fulldir2, 'r', encoding='utf-8').read()
        pattern0 = re.compile(r'【(.*?)】')
        result0 = pattern0.findall(exsfeeds)
        for i in range(len(result0)):
            result0[i] = result0[i].replace('【', '')
            result0[i] = result0[i].replace('】', '')
        if result0 != []:
            baocuo = ''
            n = 0
            while n >= 0 and n <= len(result0) - 1:
            #for n in range(len(result0)):
                try:
                    url = result0[n]
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5128.104 Safari/537.36'}
                    urllib3.disable_warnings()
                    logging.captureWarnings(True)
                    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
                    s = requests.session()
                    s.keep_alive = False  # 关闭多余连接
                    page = s.get(url, headers=headers, verify=False)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    page.encoding = 'utf-8'
                    page_content = page.text
                    soup = BeautifulSoup(page_content, 'lxml-xml')  # 指定文件解析器为lxml
                    news = soup.select('rss > channel > item')
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    f = codecs.open(fulldir3, 'a', 'utf-8')
                    for i in range(len(news)):
                        if news[i].title.string != None:
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            f.write(u'【TITLE】' + str(news[i].title.string) + '★')
                        if news[i].title.string == None:
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            f.write(u'【TITLE】No available title' + '★')
                        if news[i].pubDate != None:
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            f.write(u'【TIME】' + str(news[i].pubDate.string) + '★')
                        if news[i].description.string != None:
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            first_txt = str(news[i].description.string)
                            pattern1 = re.compile(r'<p(.*?)>(.*?)</p>')
                            result1 = pattern1.findall(first_txt)
                            if result1!= []:
                                QApplication.processEvents()
                                QApplication.restoreOverrideCursor()
                                if len(result1) >= 2:
                                    f.write(u'【CONTENT】' + ''.join(result1[0]) + ''.join(result1[1]) + '★')
                                if len(result1) == 1:
                                    f.write(u'【CONTENT】' + ''.join(result1[0]) + '★')
                            if result1 == [] or len(result1) == 0:
                                QApplication.processEvents()
                                QApplication.restoreOverrideCursor()
                                pattern10 = re.compile(r'<br /><br />(.*?)<br /><br />')
                                result10 = pattern10.findall(first_txt)
                                if result10 != []:
                                    if len(result10) >= 2:
                                        f.write(u'【CONTENT】' + ''.join(result10[0]) + ''.join(result10[1]) + '★')
                                    if len(result10) == 1:
                                        f.write(u'【CONTENT】' + ''.join(result10[0]) + '★')
                                if result10 == [] or len(result10) == 0:
                                    pattern11 = re.compile(r'<div>(.*?)</div>')
                                    result11 = pattern11.findall(first_txt)
                                    if result11 != []:
                                        QApplication.processEvents()
                                        QApplication.restoreOverrideCursor()
                                        if len(result11) >= 5:
                                            f.write(u'【CONTENT】' + ''.join(result11[0]) + ''.join(result11[1]) + ''.join(result11[2]) + ''.join(result11[3]) + ''.join(result11[4]) + '★')
                                        if len(result11) == 4:
                                            f.write(u'【CONTENT】' + ''.join(result11[0]) + ''.join(result11[1]) + ''.join(result11[2]) + ''.join(result11[3]) + '★')
                                        if len(result11) == 3:
                                            f.write(u'【CONTENT】' + ''.join(result11[0]) + ''.join(result11[1]) + ''.join(result11[2]) + '★')
                                        if len(result11) == 2:
                                            f.write(u'【CONTENT】' + ''.join(result11[0]) + ''.join(result11[1]) + '★')
                                        if len(result11) == 1:
                                            f.write(u'【CONTENT】' + ''.join(result11[0]) + '★')
                                    if result11 == [] or len(result11) == 0:
                                        QApplication.processEvents()
                                        QApplication.restoreOverrideCursor()
                                        sec_txt = first_txt.split('\n')
                                        if sec_txt != []:
                                            if '' in sec_txt:
                                                sec_txt.remove('')
                                            if len(sec_txt) >= 5:
                                                f.write(u'【CONTENT】' + str(sec_txt[0]) + str(sec_txt[1]) + str(sec_txt[2]) + str(sec_txt[3]) + str(sec_txt[4]) + '★')
                                            if len(sec_txt) == 4:
                                                f.write(u'【CONTENT】' + str(sec_txt[0]) + str(sec_txt[1]) + str(sec_txt[2]) + str(sec_txt[3]) + '★')
                                            if len(sec_txt) == 3:
                                                f.write(u'【CONTENT】' + str(sec_txt[0]) + str(sec_txt[1]) + str(sec_txt[2]) + '★')
                                            if len(sec_txt) == 2:
                                                f.write(u'【CONTENT】' + str(sec_txt[0]) + str(sec_txt[1]) + '★')
                                            if len(sec_txt) == 1:
                                                f.write(u'【CONTENT】' + str(sec_txt[0]) + '★')
                                        if sec_txt == []:
                                            f.write(u'【CONTENT】No available content' + '★')
                        if news[i].link.string != None:
                            f.write(u'【LINK】' + str(news[i].link.string) + '★\n\n')
                    f.close()
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    change_cha_1 = codecs.open(fulldir3, 'r', encoding='utf-8').read()
                    change_cha_2 = convert(change_cha_1, 'zh-cn')
                    change_cha_2_l = change_cha_2.split('\n\n')
                    if '' in change_cha_2_l:
                        change_cha_2_l.remove('')
                    change_cha_2_l2 = {}.fromkeys(change_cha_2_l).keys()
                    change_cha_2_l2_s = '\n\n'.join(change_cha_2_l2)
                    for i in range(10):
                        change_cha_2_l2_s = change_cha_2_l2_s.replace('\n\n\n\n', '㋡')
                        change_cha_2_l2_s = change_cha_2_l2_s.replace('\n\n\n', '㋡')
                        change_cha_2_l2_s = change_cha_2_l2_s.replace('\n', '㋡')
                        change_cha_2_l2_s = change_cha_2_l2_s.replace('㋡㋡㋡', '㋡')
                        change_cha_2_l2_s = change_cha_2_l2_s.replace('㋡㋡', '㋡')
                        change_cha_2_l2_s = change_cha_2_l2_s.replace('㋡', '\n\n')
                        change_cha_2_l2_s = change_cha_2_l2_s.replace('★【TITLE】', '★\n\n【TITLE】')
                    change_cha_2_l2_s = re.sub(r'data-s="(.*?)"', '', change_cha_2_l2_s)
                    with open(fulldir3, 'w', encoding='utf-8') as f0:
                        f0.write(change_cha_2_l2_s)
                    with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                        f0.write(change_cha_2_l2_s)
                    numb = int((n + 1) / len(result0) * 100)
                    self.t5_1.setVisible(True)
                    self.pbar.setValue(numb)
                    self.lbl5_1.setText(str(numb) + '%')
                    n = n + 1
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    continue
                except Exception as e:
                    pass
                    n = n + 1
                    #print(e)
                    baocuo = baocuo + str(e)
                    continue
            if str(baocuo) != '':
                patternb = re.compile(r'url: (.*?) ')
                resultb = patternb.findall(baocuo)
                resultb_s = '\n'.join(resultb)
                message_a = QMessageBox(self)
                message_a.setWindowTitle("Feeds failed to update")
                message_a.setStandardButtons(QMessageBox.StandardButton.Ok)
                message_a.information(self, 'Feeds failed to update', resultb_s)

    def topic_link(self):
        if self.checkBox4.isChecked() and self.checkBox5.isChecked() and self.widget4.currentText() != 'Topics in Chinese':
            workbook = openpyxl.load_workbook('whichtopic_c.xlsx')
            worksheet = workbook['Sheet1']
            col3 = [item.value for item in list(worksheet.columns)[21]]
            num = str(self.widget4.currentText())
            pattern_num = re.compile(r'~(.*?)~')
            result_num = pattern_num.findall(num)
            bes_num = 1
            if result_num != []:
                bes_num = int(int(''.join(result_num)) - 1)
            dvyk_l = []
            for i in range(len(col3)):
                if col3[i] == int(bes_num):
                    dvyk_l.append(int(i - 1))
            xin_n = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
            xin_n = xin_n.split('\n\n')
            if '' in xin_n:
                xin_n.remove('')
            ttl_l = []
            for i in range(len(dvyk_l)):
                ttl_l.append(xin_n[int(dvyk_l[i])])
            ttl_s = '\n\n'.join(ttl_l)
            pattern2 = re.compile(r'【TITLE】(.*?)★')
            result2 = pattern2.findall(ttl_s)
            for i in range(len(result2)):
                result2[i] = result2[i].replace('【TITLE】', '')
                result2[i] = result2[i].replace('★', '')
            self.middle_list.clear()
            self.middle_list.addItems(result2)
            news_num = str(self.middle_list.count())
            self.news_window.setText(news_num + ' pieces of news found.')

        if self.checkBox4.isChecked() and self.checkBox6.isChecked() and self.widget5.currentText() != 'Topics in English':
            workbook = openpyxl.load_workbook('whichtopic_e.xlsx')
            worksheet = workbook['Sheet1']
            col4 = [item.value for item in list(worksheet.columns)[21]]
            num = str(self.widget5.currentText())
            pattern_num = re.compile(r'~(.*?)~')
            result_num = pattern_num.findall(num)
            bes_num = 1
            if result_num != []:
                bes_num = int(int(''.join(result_num)) - 1)
            dvyk_m = []
            for i in range(len(col4)):
                if col4[i] == int(bes_num):
                    dvyk_m.append(int(i - 1))
            xin_n = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
            xin_n = xin_n.split('\n\n')
            if '' in xin_n:
                xin_n.remove('')
            ttl_l = []
            for i in range(len(dvyk_m)):
                ttl_l.append(xin_n[int(dvyk_m[i])])
            ttl_s = '\n\n'.join(ttl_l)
            pattern2 = re.compile(r'【TITLE】(.*?)★')
            result2 = pattern2.findall(ttl_s)
            for i in range(len(result2)):
                result2[i] = result2[i].replace('【TITLE】', '')
                result2[i] = result2[i].replace('★', '')
            self.middle_list.clear()
            self.middle_list.addItems(result2)
            news_num = str(self.middle_list.count())
            self.news_window.setText(news_num + ' pieces of news found.')

    def change_check(self):
        if self.checkBox5.isChecked():
            self.checkBox6.setChecked(False)
            self.checkBox6.setCheckable(False)
            self.widget5.clear()
            self.widget5.addItems(['Topics in English'])
        if self.checkBox6.isChecked():
            self.checkBox5.setChecked(False)
            self.checkBox5.setCheckable(False)
            self.widget4.clear()
            self.widget4.addItems(['Topics in Chinese'])
        if not self.checkBox5.isChecked():
            self.checkBox6.setCheckable(True)
        if not self.checkBox6.isChecked():
            self.checkBox5.setCheckable(True)

    def lock_topic(self):
        if self.checkBox2.isChecked():
            self.checkBox6.setChecked(False)
            self.checkBox6.setCheckable(False)
        if not self.checkBox2.isChecked():
            self.checkBox6.setCheckable(True)
        if self.checkBox6.isChecked():
            self.checkBox2.setChecked(False)
            self.checkBox2.setCheckable(False)
        if not self.checkBox6.isChecked():
            self.checkBox2.setCheckable(True)

    def Only_search(self):
        if self.checkBox1.isChecked() or self.checkBox2.isChecked() or self.checkBox3.isChecked() or self.checkBox4.isChecked():
            home_dir = str(Path.home())
            tarname1 = "OrangeAppPath"
            fulldir1 = os.path.join(home_dir, tarname1)
            if not os.path.exists(fulldir1):
                os.mkdir(fulldir1)
            tarname3 = "news_ori.txt"
            fulldir3 = os.path.join(fulldir1, tarname3)
            if not os.path.exists(fulldir3):
                with open(fulldir3, 'a', encoding='utf-8') as f00:
                    f00.write('')
            copy_aga = codecs.open(fulldir3, 'r', encoding='utf-8').read()
            with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                f0.write(copy_aga)

            self.t5_1.setVisible(False)
            if self.checkBox1.isChecked() and self.widget1.currentText() != 'Day' and self.widget2.currentText() != 'Month':
                get_news = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                # 08 Jul 2022
                tar_wor = str(self.widget1.currentText()) + ' ' + str(self.widget2.currentText()) + ' ' + str(
                    self.le1.text())
                get_news_l = get_news.split('\n')
                if '' in get_news_l:
                    get_news_l.remove('')
                endtime_l = []
                i = 0
                while i >= 0 and i <= len(get_news_l) - 1:
                    if tar_wor not in get_news_l[i]:
                        i = i + 1
                        continue
                    if tar_wor in get_news_l[i]:
                        endtime_l.append(get_news_l[i])
                        i = i + 1
                        continue
                # July 8, 2022
                tar_wor2 = str(self.widget2.currentText()) + ' ' + str(self.widget1.currentText()) + ', ' + str(
                    self.le1.text())
                tar_wor2 = tar_wor2.replace('01', '1')
                tar_wor2 = tar_wor2.replace('02', '2')
                tar_wor2 = tar_wor2.replace('03', '3')
                tar_wor2 = tar_wor2.replace('04', '4')
                tar_wor2 = tar_wor2.replace('05', '5')
                tar_wor2 = tar_wor2.replace('06', '6')
                tar_wor2 = tar_wor2.replace('07', '7')
                tar_wor2 = tar_wor2.replace('08', '8')
                tar_wor2 = tar_wor2.replace('09', '9')
                tar_wor2 = tar_wor2.replace('Jan', 'January')
                tar_wor2 = tar_wor2.replace('Feb', 'February')
                tar_wor2 = tar_wor2.replace('Mar', 'March')
                tar_wor2 = tar_wor2.replace('Apr', 'April')
                tar_wor2 = tar_wor2.replace('Jun', 'June')
                tar_wor2 = tar_wor2.replace('Jul', 'July')
                tar_wor2 = tar_wor2.replace('Aug', 'August')
                tar_wor2 = tar_wor2.replace('Sept', 'September')
                tar_wor2 = tar_wor2.replace('Oct', 'October')
                tar_wor2 = tar_wor2.replace('Nov', 'November')
                tar_wor2 = tar_wor2.replace('Dec', 'December')
                i = 0
                while i >= 0 and i <= len(get_news_l) - 1:
                    if tar_wor2 not in get_news_l[i]:
                        i = i + 1
                        continue
                    if tar_wor2 in get_news_l[i]:
                        endtime_l.append(get_news_l[i])
                        i = i + 1
                        continue
                # 2022/07/15
                tar_wor3 = str(self.le1.text()) + '/' + str(self.widget2.currentText()) + '/' + str(
                    self.widget1.currentText())
                tar_wor3 = tar_wor3.replace('Jan', '01')
                tar_wor3 = tar_wor3.replace('Feb', '02')
                tar_wor3 = tar_wor3.replace('Mar', '03')
                tar_wor3 = tar_wor3.replace('Apr', '04')
                tar_wor3 = tar_wor3.replace('May', '05')
                tar_wor3 = tar_wor3.replace('Jun', '06')
                tar_wor3 = tar_wor3.replace('Jul', '07')
                tar_wor3 = tar_wor3.replace('Aug', '08')
                tar_wor3 = tar_wor3.replace('Sept', '09')
                tar_wor3 = tar_wor3.replace('Oct', '10')
                tar_wor3 = tar_wor3.replace('Nov', '11')
                tar_wor3 = tar_wor3.replace('Dec', '12')
                i = 0
                while i >= 0 and i <= len(get_news_l) - 1:
                    if tar_wor3 not in get_news_l[i]:
                        i = i + 1
                        continue
                    if tar_wor3 in get_news_l[i]:
                        endtime_l.append(get_news_l[i])
                        i = i + 1
                        continue
                #20200717
                tar_wor4 = str(self.le1.text()) + str(self.widget2.currentText()) + str(self.widget1.currentText())
                tar_wor4 = tar_wor4.replace('Jan', '01')
                tar_wor4 = tar_wor4.replace('Feb', '02')
                tar_wor4 = tar_wor4.replace('Mar', '03')
                tar_wor4 = tar_wor4.replace('Apr', '04')
                tar_wor4 = tar_wor4.replace('May', '05')
                tar_wor4 = tar_wor4.replace('Jun', '06')
                tar_wor4 = tar_wor4.replace('Jul', '07')
                tar_wor4 = tar_wor4.replace('Aug', '08')
                tar_wor4 = tar_wor4.replace('Sept', '09')
                tar_wor4 = tar_wor4.replace('Oct', '10')
                tar_wor4 = tar_wor4.replace('Nov', '11')
                tar_wor4 = tar_wor4.replace('Dec', '12')
                i = 0
                while i >= 0 and i <= len(get_news_l) - 1:
                    if tar_wor4 not in get_news_l[i]:
                        i = i + 1
                        continue
                    if tar_wor4 in get_news_l[i]:
                        endtime_l.append(get_news_l[i])
                        i = i + 1
                        continue
                #2022-07-09
                tar_wor5 = str(self.le1.text()) + '-' + str(self.widget2.currentText()) + '-' + str(self.widget1.currentText())
                tar_wor5 = tar_wor5.replace('Jan', '01')
                tar_wor5 = tar_wor5.replace('Feb', '02')
                tar_wor5 = tar_wor5.replace('Mar', '03')
                tar_wor5 = tar_wor5.replace('Apr', '04')
                tar_wor5 = tar_wor5.replace('May', '05')
                tar_wor5 = tar_wor5.replace('Jun', '06')
                tar_wor5 = tar_wor5.replace('Jul', '07')
                tar_wor5 = tar_wor5.replace('Aug', '08')
                tar_wor5 = tar_wor5.replace('Sept', '09')
                tar_wor5 = tar_wor5.replace('Oct', '10')
                tar_wor5 = tar_wor5.replace('Nov', '11')
                tar_wor5 = tar_wor5.replace('Dec', '12')
                i = 0
                while i >= 0 and i <= len(get_news_l) - 1:
                    if tar_wor5 not in get_news_l[i]:
                        i = i + 1
                        continue
                    if tar_wor5 in get_news_l[i]:
                        endtime_l.append(get_news_l[i])
                        i = i + 1
                        continue
                endtime_l = {}.fromkeys(endtime_l).keys()
                time_news = '\n\n'.join(endtime_l)
                with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                    f0.write(time_news)
                pattern2 = re.compile(r'【TITLE】(.*?)★')
                result2 = pattern2.findall(time_news)
                for i in range(len(result2)):
                    result2[i] = result2[i].replace('【TITLE】', '')
                    result2[i] = result2[i].replace('★', '')
                self.middle_list.clear()
                self.middle_list.addItems(result2)
                news_num = str(self.middle_list.count())
                self.news_window.setText(news_num + ' pieces of news found.')

            if self.checkBox2.isChecked():
                get_news = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                get_news_l = get_news.split('\n\n')
                if '' in get_news_l:
                    get_news_l.remove('')
                for q in range(len(get_news_l)):
                    if self.is_contain_english(get_news_l[q]) and self.is_contain_chinese(get_news_l[q]):
                        p_head = ','.join(loc_reg.predict(get_news_l[q]).get('国外', ['中国']))
                        p_head = p_head.replace('中华人民共和国', '中国')
                        p_head = p_head.replace('朝鲜民主主义人民共和国', '朝鲜')
                        p_head = p_head.replace('大韩民国', '韩国')
                        p_head = p_head.replace('俄罗斯联邦', '俄罗斯')
                        p_head = p_head.replace('大不列颠及北爱尔兰联合王国', '英国')
                        p_head = p_head.replace('美利坚合众国', '美国')
                        get_news_l[q] = '〔' + p_head + '〕' + get_news_l[q]
                        get_news_l[q] = ''.join(get_news_l[q])
                    if not self.is_contain_english(get_news_l[q]) and self.is_contain_chinese(get_news_l[q]):
                        p_head = ','.join(loc_reg.predict(get_news_l[q]).get('国外', ['中国']))
                        p_head = p_head.replace('中华人民共和国', '中国')
                        p_head = p_head.replace('朝鲜民主主义人民共和国', '朝鲜')
                        p_head = p_head.replace('大韩民国', '韩国')
                        p_head = p_head.replace('俄罗斯联邦', '俄罗斯')
                        p_head = p_head.replace('大不列颠及北爱尔兰联合王国', '英国')
                        p_head = p_head.replace('美利坚合众国', '美国')
                        get_news_l[q] = '〔' + p_head + '〕' + get_news_l[q]
                        get_news_l[q] = ''.join(get_news_l[q])
                find_p = {'🇩🇿 Algeria': '阿尔及利亚',
                          '🇦🇺 Australia': '澳大利亚',
                          '🇦🇹 Austria': '奥地利',
                          '🇧🇷 Brazil': '巴西',
                          '🇧🇾 Belarus': '白俄罗斯',
                          '🇨🇦 Canada': '加拿大',
                          '🇨🇱 Chile': '智利',
                          "🇨🇳 People's Republic of China": '中国',
                          '🇫🇷 France': '法国',
                          '🇩🇪 Germany': '德国',
                          '🇮🇩 Indonesia': '印度尼西亚',
                          '🇮🇱 Israel': '以色列',
                          '🇮🇳 India': '印度',
                          '🇮🇷 Iran': '伊朗',
                          '🇯🇵 Japan': '日本',
                          "🇰🇵 Democratic People's Republic of Korea": '朝鲜',
                          '🇰🇷 Republic of Korea': '韩国',
                          '🇱🇧 Lebanon': '黎巴嫩',
                          '🇲🇲 Myanmar': '缅甸',
                          '🇲🇾 Malaysia': '马来西亚',
                          '🇳🇮 Nicaragua': '尼加拉瓜',
                          '🇵🇭 Philippines': '菲律宾',
                          '🇵🇰 Pakistan': '巴基斯坦',
                          '🇷🇺 Russian Federation': '俄罗斯',
                          '🇸🇩 Sudan': '苏丹',
                          '🇸🇬 Singapore': '新加坡',
                          '🇸🇳 Senegal': '塞内加尔',
                          '🇹🇭 Thailand': '泰国',
                          '🇺🇳 UN': '联合国',
                          '🇬🇧 United Kingdom of Great Britain and Northern Ireland': '英国',
                          '🇺🇸 United States of America': '美国',
                          '🇻🇳 Vietnam': '越南',
                          '🎌 Taiwan': '台湾'}
                find_key = ''.join(find_p.get(self.widget3.currentText(), 'All'))
                if find_key != 'All':
                    tar_list = []
                    i = 0
                    while i >= 0 and i <= len(get_news_l) - 1:
                        if find_key in get_news_l[i]:
                            tar_list.append(get_news_l[i])
                            i = i + 1
                            continue
                        if not find_key in get_news_l[i]:
                            i = i + 1
                            continue
                    entity_news = '\n\n'.join(tar_list)
                    with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                        f0.write(entity_news)
                if find_key == 'All':
                    entity_news_all = '\n\n'.join(get_news_l)
                    with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                        f0.write(entity_news_all)
                list_title = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                pattern2 = re.compile(r'【TITLE】(.*?)★')
                result2 = pattern2.findall(list_title)
                for i in range(len(result2)):
                    result2[i] = result2[i].replace('【TITLE】', '')
                    result2[i] = result2[i].replace('★', '')
                self.middle_list.clear()
                self.middle_list.addItems(result2)
                news_num = str(self.middle_list.count())
                self.news_window.setText(news_num + ' pieces of news found.')

            if self.checkBox3.isChecked():
                find_word = self.le3.text().split(',')
                new_n = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                new_n_l = new_n.split('\n')
                if '' in new_n_l:
                    new_n_l.remove('')
                kw_l = []
                k = 0
                i = 0
                while i >= 0 and i <= len(new_n_l) - 1 and k >= 0 and k <= len(find_word):
                    if find_word[k] in new_n_l[i]:
                        kw_l.append(new_n_l[i])
                        i = i + 1
                        continue
                    if not find_word[k] in new_n_l[i]:
                        i = i + 1
                        continue
                    k = k + 1
                    i = 0
                    continue
                key_news = '\n\n'.join(kw_l)
                with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                    f0.write(key_news)
                list_title = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                pattern2 = re.compile(r'【TITLE】(.*?)★')
                result2 = pattern2.findall(list_title)
                for i in range(len(result2)):
                    result2[i] = result2[i].replace('【TITLE】', '')
                    result2[i] = result2[i].replace('★', '')
                self.middle_list.clear()
                self.middle_list.addItems(result2)
                news_num = str(self.middle_list.count())
                self.news_window.setText(news_num + ' pieces of news found.')

            if self.checkBox4.isChecked() and self.checkBox5.isChecked():
                # 1 清理文本
                cixing = ['x', 'zg', 'uj', 'ul', 'e', 'd', 'uz', 'y', 'eng', 'r', 'm', 'a', 'ad', 'c', 'o', 'p', 'q',
                          'r', 'w', 'v']
                with open('stopwords_c.txt', encoding='utf-8') as f:
                    stopwords = f.read().splitlines()
                norm_corpus0 = []
                text_corpus = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                text = text_corpus.split('\n\n')
                if '' in text:
                    text.remove('')
                for i in range(len(text)):
                    if self.is_contain_chinese(str(text[i])) and len(text[i]) > 150:
                        norm_corpus0.append(text[i])
                ori_news_c = []
                for i in range(len(norm_corpus0)):
                    ori_news_c.append(norm_corpus0[i])
                for i in range(len(norm_corpus0)):
                    norm_corpus0[i] = re.sub(r'【LINK】(.*?)★', '', norm_corpus0[i])
                    norm_corpus0[i] = re.sub(r'【TIME】(.*?)★', '', norm_corpus0[i])
                    norm_corpus0[i] = re.sub(r'【TITLE】', '', norm_corpus0[i])
                    norm_corpus0[i] = re.sub(r'【CONTENT】', '', norm_corpus0[i])
                    norm_corpus0[i] = re.sub(r'<(.*?)>', '', norm_corpus0[i])
                norm_corpus = []
                for line in norm_corpus0:
                    line = line.strip()
                    result = ''
                    line_cut = pseg.cut(line)
                    for w in line_cut:
                        if not w.flag in cixing:
                            seg = str(w.word)
                            if seg not in stopwords:
                                result += seg + ' '
                    if len(result) >= 0:
                        norm_corpus.append(result)
                # 2 向量化文本
                #vectorizer, tfidf_matrix = self.build_feature_matrix(norm_corpus, 'tfidf', ngram_range=(1, 1))
                vectorizer = TfidfVectorizer(ngram_range=(1, 1))
                tfidf_matrix = vectorizer.fit_transform(norm_corpus)
                # 3 主题分类
                total_topics = 20
                nmf = NMF(n_components=total_topics, random_state=42, l1_ratio=0.5)
                nmf.fit(tfidf_matrix)
                feature_names = vectorizer.get_feature_names()
                weights = nmf.components_
                feature_names = np.array(feature_names)
                sorted_indices = np.array([list(row[::-1]) for row in np.argsort(np.abs(weights))])
                sorted_weights = np.array([list(wt[index]) for wt, index in zip(weights, sorted_indices)])
                sorted_terms = np.array([list(feature_names[row]) for row in sorted_indices])
                topics = [np.vstack((terms.T, term_weights.T)).T for terms, term_weights in
                          zip(sorted_terms, sorted_weights)]
                #topics = self.get_topics_terms_weights(weights, feature_names)
                # 4 打印结果
                num_terms = 25
                weight_threshold = 0.1
                sult_l = []
                for index in range(total_topics):
                    topic = topics[index]
                    topic = [(term, float(wt)) for term, wt in topic]
                    topic = [(word, round(wt, 2)) for word, wt in topic if abs(wt) >= weight_threshold]

                    part1 = str('~' + str(index + 1) + "~")
                    tw = [term for term, wt in topic]
                    end_t = tw[:num_terms] if num_terms else tw
                    part2 = ''
                    if len(end_t) >= 3:
                        part2 = '#' + str(end_t[0]) + '#' + str(end_t[1] + '#' + str(end_t[2]))
                    if len(end_t) == 2:
                        part2 = '#' + str(end_t[0]) + '#' + str(end_t[1])
                    if len(end_t) == 1:
                        part2 = '#' + str(end_t[0])
                    all = part1 + part2
                    sult_l.append(all)
                # 5 主题矩阵
                doc_topic = nmf.fit_transform(tfidf_matrix)
                did = np.sum(doc_topic, axis=1, keepdims=True)
                for item in did:
                    for i in range(len(item)):
                        if item[i] == 0:
                            item[i] = 1
                doc_topic = doc_topic / did
                dt = [[]]
                result = []
                for i in range(total_topics):
                    dt.append([])
                for line in doc_topic:
                    val = 0.0
                    n = 0
                    for i in range(total_topics):
                        dt[i].append(line[i])
                        if line[i] > val:
                            val = line[i]
                            n = i
                    result.append(n)
                tpmat = {}
                tpname = []
                for i in range(total_topics):
                    name = 'tp' + str(i)
                    tpmat[name] = dt[i]
                tpmat['result'] = result
                tpmat['text'] = norm_corpus
                df = pd.DataFrame(tpmat, columns=tpmat.keys())
                df.to_excel('whichtopic_c.xlsx')
                self.widget4.clear()
                self.widget4.addItems(sult_l)
                topic_c_news = '\n\n'.join(ori_news_c)
                with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                    f0.write(topic_c_news)
                self.widget4.setCurrentIndex(1)
                self.widget4.setCurrentIndex(0)

            if self.checkBox4.isChecked() and self.checkBox6.isChecked():
                # 1
                text_corpus = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                toy_corpus0 = text_corpus.split('\n\n')
                if '' in toy_corpus0:
                    toy_corpus0.remove('')
                toy_corpus1 = []
                for i in range(len(toy_corpus0)):
                    if self.is_contain_english(str(toy_corpus0[i])) and not self.is_contain_chinese(str(toy_corpus0[i])) and len(toy_corpus0) > 150:
                        toy_corpus1.append(toy_corpus0[i])
                ori_news_e = []
                for i in range(len(toy_corpus1)):
                    ori_news_e.append(toy_corpus1[i])
                for i in range(len(toy_corpus1)):
                    toy_corpus1[i] = re.sub(r'【LINK】(.*?)★', '', toy_corpus1[i])
                    toy_corpus1[i] = re.sub(r'【TIME】(.*?)★', '', toy_corpus1[i])
                    toy_corpus1[i] = re.sub(r'【TITLE】', '', toy_corpus1[i])
                    toy_corpus1[i] = re.sub(r'【CONTENT】', '', toy_corpus1[i])
                    toy_corpus1[i] = re.sub(r'<(.*?)>', '', toy_corpus1[i])
                norm_corpus = []
                for item in toy_corpus1:
                    item = self.normalize_corpus(item.lower())
                    norm_corpus.append(item)
                # 2
                if norm_corpus != []:
                    vectorizer = TfidfVectorizer(ngram_range=(1, 1))
                    tfidf_matrix = vectorizer.fit_transform(norm_corpus)
                    # 3 主题分类
                    total_topics = 20
                    nmf = NMF(n_components=total_topics, random_state=42, l1_ratio=0.5)
                    nmf.fit(tfidf_matrix)
                    feature_names = vectorizer.get_feature_names()
                    weights = nmf.components_
                    feature_names = np.array(feature_names)
                    sorted_indices = np.array([list(row[::-1]) for row in np.argsort(np.abs(weights))])
                    sorted_weights = np.array([list(wt[index]) for wt, index in zip(weights, sorted_indices)])
                    sorted_terms = np.array([list(feature_names[row]) for row in sorted_indices])
                    topics = [np.vstack((terms.T, term_weights.T)).T for terms, term_weights in
                              zip(sorted_terms, sorted_weights)]
                    # 4 打印结果
                    num_terms = 25
                    weight_threshold = 0.1
                    sult_m = []
                    for index in range(total_topics):
                        topic = topics[index]
                        topic = [(term, float(wt)) for term, wt in topic]
                        topic = [(word, round(wt, 2)) for word, wt in topic if abs(wt) >= weight_threshold]

                        part1 = str('~' + str(index + 1) + "~")
                        tw = [term for term, wt in topic]
                        end_t = tw[:num_terms] if num_terms else tw
                        part2 = ''
                        if len(end_t) >= 3:
                            part2 = '#' + str(end_t[0]) + '#' + str(end_t[1] + '#' + str(end_t[2]))
                        if len(end_t) == 2:
                            part2 = '#' + str(end_t[0]) + '#' + str(end_t[1])
                        if len(end_t) == 1:
                            part2 = '#' + str(end_t[0])
                        all = part1 + part2
                        sult_m.append(all)
                    # 5 主题矩阵
                    doc_topic = nmf.fit_transform(tfidf_matrix)
                    did = np.sum(doc_topic, axis=1, keepdims=True)
                    for item in did:
                        for i in range(len(item)):
                            if item[i] == 0:
                                item[i] = 1
                    doc_topic = doc_topic / did
                    dt = [[]]
                    result = []
                    for i in range(total_topics):
                        dt.append([])
                    for line in doc_topic:
                        val = 0.0
                        n = 0
                        for i in range(total_topics):
                            dt[i].append(line[i])
                            if line[i] > val:
                                val = line[i]
                                n = i
                        result.append(n)
                    tpmat = {}
                    tpname = []
                    for i in range(total_topics):
                        name = 'tp' + str(i)
                        tpmat[name] = dt[i]
                    tpmat['result'] = result
                    tpmat['text'] = norm_corpus
                    df = pd.DataFrame(tpmat, columns=tpmat.keys())
                    df.to_excel('whichtopic_e.xlsx')
                    self.widget5.clear()
                    self.widget5.addItems(sult_m)
                    topic_e_news = '\n\n'.join(ori_news_e)
                    with open('news_fin.txt', 'w', encoding='utf-8') as f0:
                        f0.write(topic_e_news)
                    self.widget5.setCurrentIndex(1)
                    self.widget5.setCurrentIndex(0)

            self.times += 1
            MOST_WEIGHT = int(self.screen().availableGeometry().width() * 0.75)
            HEIGHT = int(self.screen().availableGeometry().height())
            if not self.t9.isVisible() or self.t10.isVisible():
                self.t9.setVisible(True)
                self.t10.setVisible(True)
            if self.width() != MOST_WEIGHT or self.height() != HEIGHT:
                self.resize(MOST_WEIGHT, HEIGHT)
            self.center()
            tall = self.middle_list.height() - 3
            if self.times == 1:
                with open('tall.txt', 'w', encoding='utf-8') as f0:
                    f0.write(str(tall))
            nowtall = int(codecs.open('tall.txt', 'r', encoding='utf-8').read())
            self.middle_list.setFixedHeight(nowtall)
            self.news_window.setFixedHeight(nowtall)
            self.b9.setContentsMargins(5, 0, 0, 28)
            self.b10.setContentsMargins(5, 0, 0, 28)

    def normalize_corpus(self, text):
        text = self.remove_characters_from_text(text)
        text = self.remove_stopwords_from_text(text)
        return text

    def remove_characters_from_text(self, text):
        text = text.strip()
        PATTERN = r'[^a-zA-Z]'
        filtered_text = re.sub(PATTERN, r' ', text)
        return filtered_text

    def remove_stopwords_from_text(self, text):
        stopwords = codecs.open('stopwords_e.txt').read().splitlines()
        tokens = nltk.word_tokenize(text)
        stopword_list = nltk.corpus.stopwords.words('english')
        filtered_tokens = []
        for token in tokens:
            if token not in stopword_list and token not in stopwords:
                filtered_tokens.append(token)
        result = ' '.join(filtered_tokens)
        return result

    def Item_click(self, item):
        fin_file = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
        ser_key = '【TITLE】' + item.text() + '★'
        fin_file_l = fin_file.split('\n')
        if '' in fin_file_l:
            fin_file_l.remove('')
        i = 0
        while i >= 0 and i <= len(fin_file_l) - 1:
            if ser_key not in fin_file_l[i]:
                fin_file_l.remove(fin_file_l[i])
                i = i
                continue
            if ser_key in fin_file_l[i]:
                i = i + 1
                continue
        fin_news2 = ''
        if fin_file_l != []:
            fin_news2 = ''.join(fin_file_l[0])
        fin_news2 = re.sub(r'【TITLE】(.*?)★', '', fin_news2)
        fin_news2 = re.sub(r'【TIME】(.*?)★', '', fin_news2)
        fin_news2 = re.sub(r'〔(.*?)〕', '', fin_news2)
        fin_news2 = fin_news2.replace('【CONTENT】', '')
        fin_news2 = fin_news2.replace('【LINK】', '')
        fin_news2 = fin_news2.replace('★', '')
        self.news_window.setHtml(fin_news2)

    def clear_shal(self):
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)
        self.checkBox5.setChecked(False)
        self.checkBox6.setChecked(False)
        self.widget1.setCurrentIndex(0)
        self.widget2.setCurrentIndex(0)
        self.widget3.setCurrentIndex(0)
        self.widget4.clear()
        self.widget4.addItems(['Topics in Chinese'])
        self.widget5.clear()
        self.widget5.addItems(['Topics in English'])
        self.le1.clear()
        self.le3.clear()
        self.middle_list.clear()
        self.news_window.clear()
        MINI_WEIGHT = int(self.screen().availableGeometry().width() / 4)
        DE_HEIGHT = int(self.screen().availableGeometry().height() - 30)
        self.resize(MINI_WEIGHT, DE_HEIGHT)
        self.center()
        self.t9.setVisible(False)
        self.t10.setVisible(False)

    def clear_tot(self):
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)
        self.checkBox5.setChecked(False)
        self.checkBox6.setChecked(False)
        self.widget1.setCurrentIndex(0)
        self.widget2.setCurrentIndex(0)
        self.widget3.setCurrentIndex(0)
        self.widget4.clear()
        self.widget4.addItems(['Topics in Chinese'])
        self.widget5.clear()
        self.widget5.addItems(['Topics in English'])
        self.le1.clear()
        self.le3.clear()
        self.middle_list.clear()
        self.news_window.clear()
        home_dir = str(Path.home())
        tarname1 = "OrangeAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname3 = "news_ori.txt"
        fulldir3 = os.path.join(fulldir1, tarname3)
        if not os.path.exists(fulldir3):
            with open(fulldir3, 'a', encoding='utf-8') as f00:
                f00.write('')
        with open(fulldir3, 'w', encoding='utf-8') as f0:
            f0.write('')
        with open('news_fin.txt', 'w', encoding='utf-8') as f0:
            f0.write('')

    def is_contain_english(self, str0):  # 判断是否包含英文字母
        import re
        return bool(re.search('[a-zA-Zａ-ｚＡ-Ｚ]', str0))

    def is_contain_chinese(self, check_str):  # 判断是否包含中文字
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def export_all(self):
        blank = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
        if self.checkBox1.isChecked() or self.checkBox2.isChecked() or self.checkBox3.isChecked() or self.checkBox4.isChecked():
            home_dir = str(Path.home())
            fj = QFileDialog.getExistingDirectory(self, "Open directory", home_dir)
            if fj != '' and blank != '':
                part1 = ''
                part2 = ''
                part3 = ''
                part4 = ''
                part5 = ''
                part6 = ''
                part7 = ''
                part8 = ''
                part9 = ''

                if self.checkBox1.isChecked():
                    gets_news = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                    part1 = 'News'
                    part2 = '\nBy time: ' + str(self.widget1.currentText()) + ' ' + str(self.widget2.currentText()) + ' ' + str(self.le1.text())
                    gets_news_l = gets_news.split('\n\n')
                    if '' in gets_news_l:
                        gets_news_l.remove('')
                    for i in range(len(gets_news_l)):
                        gets_news_l[i] = '- ' + gets_news_l[i]
                        gets_news_l[i] = ''.join(gets_news_l[i])
                    part3 = '\n' + '\n'.join(gets_news_l)

                if self.checkBox2.isChecked():
                    gets_news = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                    gets_news_l = gets_news.split('\n\n')
                    if '' in gets_news_l:
                        gets_news_l.remove('')
                    part1 = 'News'
                    part4 = '\nBy entities'
                    all_list = ['🇩🇿 Algeria',
                               '🇦🇺 Australia',
                               '🇦🇹 Austria',
                               '🇧🇷 Brazil',
                               '🇧🇾 Belarus',
                               '🇨🇦 Canada',
                               '🇨🇱 Chile',
                               "🇨🇳 People's Republic of China",
                               '🇫🇷 France',
                               '🇩🇪 Germany',
                               '🇮🇩 Indonesia',
                               '🇮🇱 Israel',
                               '🇮🇳 India',
                               '🇮🇷 Iran',
                               '🇯🇵 Japan',
                               "🇰🇵 Democratic People's Republic of Korea",
                               '🇰🇷 Republic of Korea',
                               '🇱🇧 Lebanon',
                               '🇲🇲 Myanmar',
                               '🇲🇾 Malaysia',
                               '🇳🇮 Nicaragua',
                               '🇵🇭 Philippines',
                               '🇵🇰 Pakistan',
                               '🇷🇺 Russian Federation',
                               '🇸🇩 Sudan',
                               '🇸🇬 Singapore',
                               '🇸🇳 Senegal',
                               '🇹🇭 Thailand',
                               '🇺🇳 UN',
                               '🇬🇧 United Kingdom of Great Britain and Northern Ireland',
                               '🇺🇸 United States of America',
                               '🇻🇳 Vietnam',
                               '🎌 Taiwan']
                    find_p = {'🇩🇿 Algeria': '阿尔及利亚',
                              '🇦🇺 Australia': '澳大利亚',
                              '🇦🇹 Austria': '奥地利',
                              '🇧🇷 Brazil': '巴西',
                              '🇧🇾 Belarus': '白俄罗斯',
                              '🇨🇦 Canada': '加拿大',
                              '🇨🇱 Chile': '智利',
                              "🇨🇳 People's Republic of China": '中国',
                              '🇫🇷 France': '法国',
                              '🇩🇪 Germany': '德国',
                              '🇮🇩 Indonesia': '印度尼西亚',
                              '🇮🇱 Israel': '以色列',
                              '🇮🇳 India': '印度',
                              '🇮🇷 Iran': '伊朗',
                              '🇯🇵 Japan': '日本',
                              "🇰🇵 Democratic People's Republic of Korea": '朝鲜',
                              '🇰🇷 Republic of Korea': '韩国',
                              '🇱🇧 Lebanon': '黎巴嫩',
                              '🇲🇲 Myanmar': '缅甸',
                              '🇲🇾 Malaysia': '马来西亚',
                              '🇳🇮 Nicaragua': '尼加拉瓜',
                              '🇵🇭 Philippines': '菲律宾',
                              '🇵🇰 Pakistan': '巴基斯坦',
                              '🇷🇺 Russian Federation': '俄罗斯',
                              '🇸🇩 Sudan': '苏丹',
                              '🇸🇬 Singapore': '新加坡',
                              '🇸🇳 Senegal': '塞内加尔',
                              '🇹🇭 Thailand': '泰国',
                              '🇺🇳 UN': '联合国',
                              '🇬🇧 United Kingdom of Great Britain and Northern Ireland': '英国',
                              '🇺🇸 United States of America': '美国',
                              '🇻🇳 Vietnam': '越南',
                              '🎌 Taiwan': '台湾'}
                    if self.widget3.currentText() == 'All essential entities (default)':
                        with open('export_ent.txt', 'w', encoding='utf-8') as f0:
                            f0.write('')
                        i = 0
                        while i >= 0 and i <= len(all_list) - 1:
                            find_key = ''.join(find_p.get(all_list[i], 'All'))
                            tar_list = []
                            s = 0
                            while s >= 0 and s <= len(gets_news_l) - 1:
                                if find_key in gets_news_l[s]:
                                    tar_list.append(gets_news_l[s])
                                    s = s + 1
                                    continue
                                if not find_key in gets_news_l[s]:
                                    s = s + 1
                                    continue
                            entity_news = '\n\n'.join(tar_list)
                            pattern2 = re.compile(r'【TITLE】(.*?)★')
                            result2 = pattern2.findall(entity_news)
                            for d in range(len(result2)):
                                result2[d] = result2[d].replace('【TITLE】', '')
                                result2[d] = result2[d].replace('★', '')
                            count = len(result2)
                            if count > 0:
                                piece_one = '\n- ' + str(all_list[i]) + '(' + str(count) + ')'
                                with open('export_ent.txt', 'a', encoding='utf-8') as f1:
                                    f1.write(piece_one)
                                for m in range(len(result2)):
                                    ser_key = '【TITLE】' + result2[m] + '★'
                                    tar_f = []
                                    for k in range(len(gets_news_l)):
                                        if ser_key in gets_news_l[k]:
                                            tar_f.append(gets_news_l[k])
                                    tar_s = 'None'
                                    if tar_f != []:
                                        tar_s = ''.join(tar_f[0])
                                    piece_two = '\n\t- ' + str(result2[m])
                                    piece_three = '\n\t\t- ' + str(tar_s)
                                    with open('export_ent.txt', 'a', encoding='utf-8') as f1:
                                        f1.write(piece_two + piece_three)
                            i = i + 1
                            continue
                        part5 = codecs.open('export_ent.txt', 'r', encoding='utf-8').read()
                        part5 = re.sub(r'【TITLE】(.*?)【CONTENT】', '', part5)
                        part5 = part5.replace('★【', '【')

                    if not self.widget3.currentText() == 'All essential entities (default)':
                        with open('export_ent.txt', 'w', encoding='utf-8') as f0:
                            f0.write('')
                        now_word = self.widget3.currentText()
                        find_key = ''.join(find_p.get(now_word, 'All'))
                        tar_list = []
                        s = 0
                        while s >= 0 and s <= len(gets_news_l) - 1:
                            if find_key in gets_news_l[s]:
                                tar_list.append(gets_news_l[s])
                                s = s + 1
                                continue
                            if not find_key in gets_news_l[s]:
                                s = s + 1
                                continue
                        entity_news = '\n\n'.join(tar_list)
                        pattern2 = re.compile(r'【TITLE】(.*?)★')
                        result2 = pattern2.findall(entity_news)
                        for d in range(len(result2)):
                            result2[d] = result2[d].replace('【TITLE】', '')
                            result2[d] = result2[d].replace('★', '')
                        count = len(result2)
                        piece_one = '\n- ' + str(now_word) + '(' + str(count) + ')'
                        with open('export_ent.txt', 'a', encoding='utf-8') as f1:
                            f1.write(piece_one)
                        for m in range(len(result2)):
                            ser_key = '【TITLE】' + result2[m] + '★'
                            tar_f = []
                            for k in range(len(gets_news_l)):
                                if ser_key in gets_news_l[k]:
                                    tar_f.append(gets_news_l[k])
                            tar_s = 'None'
                            if tar_f != []:
                                tar_s = ''.join(tar_f[0])
                            piece_two = '\n\t- ' + str(result2[m])
                            piece_three = '\n\t\t- ' + str(tar_s)
                            with open('export_ent.txt', 'a', encoding='utf-8') as f1:
                                f1.write(piece_two + piece_three)
                        part5 = codecs.open('export_ent.txt', 'r', encoding='utf-8').read()
                        part5 = re.sub(r'【TITLE】(.*?)【CONTENT】', '', part5)
                        part5 = part5.replace('★【', '【')

                if self.checkBox3.isChecked():
                    pass
                    gets_news = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                    gets_news_l = gets_news.split('\n\n')
                    if '' in gets_news_l:
                        gets_news_l.remove('')
                    part1 = 'News'
                    part6 = '\nBy keyword: ' + str(self.le3.text())
                    for i in range(len(gets_news_l)):
                        gets_news_l[i] = '- ' + gets_news_l[i]
                        gets_news_l[i] = ''.join(gets_news_l[i])
                    part7 = '\n' + '\n'.join(gets_news_l)

                if self.checkBox4.isChecked() and self.checkBox5.isChecked() and self.widget4.currentText() != 'Topics in Chinese':
                    pass
                    with open('export_chi.txt', 'w', encoding='utf-8') as f0:
                        f0.write('')
                    part1 = 'News'
                    part8 = '\nBy topic (Chinese)'
                    for i in range(20):
                        self.widget4.setCurrentIndex(i)
                        cont_one = '\n- ' + self.widget4.currentText()
                        with open('export_chi.txt', 'a', encoding='utf-8') as f1:
                            f1.write(cont_one)
                        workbook = openpyxl.load_workbook('whichtopic_c.xlsx')
                        worksheet = workbook['Sheet1']
                        col3 = [item.value for item in list(worksheet.columns)[21]]
                        num = str(self.widget4.currentText())
                        pattern_num = re.compile(r'~(.*?)~')
                        result_num = pattern_num.findall(num)
                        bes_num = 1
                        if result_num != []:
                            bes_num = int(int(''.join(result_num)) - 1)
                        dvyk_l = []
                        for k in range(len(col3)):
                            if col3[k] == int(bes_num):
                                dvyk_l.append(int(k - 1))
                        xin_n = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                        xin_n = xin_n.split('\n\n')
                        if '' in xin_n:
                            xin_n.remove('')
                        ttl_l = []
                        for g in range(len(dvyk_l)):
                            ttl_l.append(xin_n[int(dvyk_l[g])])
                        ttl_s = '\n\n'.join(ttl_l)
                        pattern2 = re.compile(r'【TITLE】(.*?)★')
                        result2 = pattern2.findall(ttl_s)
                        for f in range(len(result2)):
                            result2[f] = result2[f].replace('【TITLE】', '')
                            result2[f] = result2[f].replace('★', '')
                        for m in range(len(result2)):
                            ser_key = '【TITLE】' + result2[m] + '★'
                            tar_f = []
                            for k in range(len(xin_n)):
                                if ser_key in xin_n[k]:
                                    tar_f.append(xin_n[k])
                            tar_s = 'None'
                            if tar_f != []:
                                tar_s = ''.join(tar_f[0])
                            con_two = '\n\t- ' + str(result2[m])
                            con_three = '\n\t\t- ' + str(tar_s)
                            with open('export_chi.txt', 'a', encoding='utf-8') as f1:
                                f1.write(con_two + con_three)
                    part9 = codecs.open('export_chi.txt', 'r', encoding='utf-8').read()
                    part9 = re.sub(r'【TITLE】(.*?)【CONTENT】', '', part9)
                    part9 = part9.replace('★【', '【')
                    self.widget4.setCurrentIndex(0)

                if self.checkBox4.isChecked() and self.checkBox6.isChecked():
                    pass
                    with open('export_eng.txt', 'w', encoding='utf-8') as f0:
                        f0.write('')
                    part1 = 'News'
                    part8 = '\nBy topic (English)'
                    for i in range(20):
                        self.widget5.setCurrentIndex(i)
                        cont_one = '\n- ' + self.widget5.currentText()
                        with open('export_eng.txt', 'a', encoding='utf-8') as f1:
                            f1.write(cont_one)
                        workbook = openpyxl.load_workbook('whichtopic_e.xlsx')
                        worksheet = workbook['Sheet1']
                        col3 = [item.value for item in list(worksheet.columns)[21]]
                        num = str(self.widget5.currentText())
                        pattern_num = re.compile(r'~(.*?)~')
                        result_num = pattern_num.findall(num)
                        bes_num = 1
                        if result_num != []:
                            bes_num = int(int(''.join(result_num)) - 1)
                        dvyk_l = []
                        for k in range(len(col3)):
                            if col3[k] == int(bes_num):
                                dvyk_l.append(int(k - 1))
                        xin_n = codecs.open('news_fin.txt', 'r', encoding='utf-8').read()
                        xin_n = xin_n.split('\n\n')
                        if '' in xin_n:
                            xin_n.remove('')
                        ttl_l = []
                        for g in range(len(dvyk_l)):
                            ttl_l.append(xin_n[int(dvyk_l[g])])
                        ttl_s = '\n\n'.join(ttl_l)
                        pattern2 = re.compile(r'【TITLE】(.*?)★')
                        result2 = pattern2.findall(ttl_s)
                        for f in range(len(result2)):
                            result2[f] = result2[f].replace('【TITLE】', '')
                            result2[f] = result2[f].replace('★', '')
                        for m in range(len(result2)):
                            ser_key = '【TITLE】' + result2[m] + '★'
                            tar_f = []
                            for k in range(len(xin_n)):
                                if ser_key in xin_n[k]:
                                    tar_f.append(xin_n[k])
                            tar_s = 'None'
                            if tar_f != []:
                                tar_s = ''.join(tar_f[0])
                            con_two = '\n\t- ' + str(result2[m])
                            con_three = '\n\t\t- ' + str(tar_s)
                            with open('export_eng.txt', 'a', encoding='utf-8') as f1:
                                f1.write(con_two + con_three)
                    part9 = codecs.open('export_eng.txt', 'r', encoding='utf-8').read()
                    part9 = re.sub(r'【TITLE】(.*?)【CONTENT】', '', part9)
                    part9 = part9.replace('★【', '【')
                    self.widget5.setCurrentIndex(0)

                now_time = dt.datetime.now().strftime('%F %T')
                tarname1 = "ExportedNews " + str(now_time) + '.md'
                fulldir1 = os.path.join(fj, tarname1)
                with open(fulldir1, 'a', encoding='utf-8') as f0:
                    f0.write(part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9)

    def rest_siz(self):
        MINI_WEIGHT = int(self.screen().availableGeometry().width() / 4)
        DE_HEIGHT = int(self.screen().availableGeometry().height() - 30)
        self.resize(MINI_WEIGHT, DE_HEIGHT)
        self.center()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def activate(self):  # 设置窗口显示
        self.show()
        self.times = 0
        self.Only_search()

    def cancel(self):  # 设置取消键的功能
        self.close()