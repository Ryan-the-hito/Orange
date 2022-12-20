class window4(QWidget):  # Customization settings
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 设置窗口内布局
        self.setUpMainWindow()
        self.resize(640, 400)
        self.center()
        self.setWindowTitle('Customization settings')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def setUpMainWindow(self):
        wid0 = QWidget()
        lbl0 = QLabel("Set your feeds", self)
        font = PyQt6.QtGui.QFont()
        font.setBold(True)
        lbl0.setFont(font)
        b40 = QHBoxLayout()
        b40.setContentsMargins(10, 10, 10, 10)
        b40.addStretch()
        b40.addWidget(lbl0)
        b40.addStretch()
        wid0.setLayout(b40)

        wid1 = QWidget()
        self.text_feed = QTextEdit(self)
        self.text_feed.setFixedWidth(550)
        self.text_feed.setFixedHeight(340)
        self.text_feed.setPlaceholderText('Please enter the title and the xml Url in【】, or open a .opml file.\nE.g.: BBC News【http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/uk_politics/rss.xml】')
        b41 = QHBoxLayout()
        b41.setContentsMargins(10, 10, 10, 10)
        b41.addWidget(self.text_feed)
        wid1.setLayout(b41)

        wid11 = QWidget()
        btn4_1 = QPushButton('Import from OPML files', self)
        btn4_1.setMaximumHeight(20)
        btn4_1.setFixedWidth(250)
        btn4_1.clicked.connect(self.OpenFeed)
        btn4_11 = QPushButton('Save feeds!', self)
        btn4_11.clicked.connect(self.SaveFeed)
        btn4_11.setMaximumHeight(20)
        btn4_11.setFixedWidth(250)
        b411 = QHBoxLayout()
        b411.setContentsMargins(10, 10, 10, 10)
        b411.addStretch()
        b411.addWidget(btn4_1)
        b411.addWidget(btn4_11)
        b411.addStretch()
        wid11.setLayout(b411)

        main_h_box = QVBoxLayout()
        main_h_box.addWidget(wid0)
        main_h_box.addWidget(wid1)
        main_h_box.addWidget(wid11)
        main_h_box.addStretch()
        self.setLayout(main_h_box)

        home_dir = str(Path.home())
        tarname1 = "OrangeAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "DoNotDelete.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        if not os.path.exists(fulldir2):
            with open(fulldir2, 'a', encoding='utf-8') as f0:
                f0.write('')
        exsfeeds = codecs.open(fulldir2, 'r', encoding='utf-8').read()
        self.text_feed.setText(exsfeeds)

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def cancel(self):  # 设置取消键的功能
        self.close()

    def activate(self):  # 设置窗口显示
        self.show()
        home_dir = str(Path.home())
        tarname1 = "OrangeAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "DoNotDelete.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        if not os.path.exists(fulldir2):
            with open(fulldir2, 'a', encoding='utf-8') as f0:
                f0.write('')
        exsfeeds = codecs.open(fulldir2, 'r', encoding='utf-8').read()
        self.text_feed.setText(exsfeeds)

    def SaveFeed(self):
        home_dir = str(Path.home())
        tarname1 = "OrangeAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "DoNotDelete.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        part1 = self.text_feed.toPlainText()
        with open(fulldir2, 'w', encoding='utf-8') as f0:
            f0.write(part1)
        self.close()

    def OpenFeed(self):
        home_dir = str(Path.home())
        fj, ok = QFileDialog.getOpenFileName(self, "Open File", home_dir, "OPML Files (*.opml)")
        if fj != '':
            feedfile = codecs.open(fj, 'r', encoding='utf-8').read()
            if feedfile == '':
                self.text_feed.setText('The file is empty. Please check!')
                self.text_feed.setStyleSheet('color:red')
            else:
                pattern0 = re.compile(r'<outline (.*?)/>')
                result0 = pattern0.findall(feedfile)
                for i in range(len(result0)):
                    pattern1 = re.compile(r'title="(.*?)"')
                    result1 = pattern1.findall(result0[i])
                    result1 = ''.join(result1)
                    result1 = result1.replace('title=', '')
                    result1 = result1.replace('"', '')
                    pattern2 = re.compile(r'xmlUrl="(.*?)"')
                    result2 = pattern2.findall(result0[i])
                    result2 = ''.join(result2)
                    result2 = result2.replace('xmlUrl=', '')
                    result2 = result2.replace('"', '')
                    result0[i] = result1 + '【' + result2 + '】'
                    result0[i] = ''.join(result0[i])
                    i = i + 1
                    continue
                FeedText = '\n'.join(result0)
                self.text_feed.setText(FeedText)
                self.text_feed.setStyleSheet('color:black')