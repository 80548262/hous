import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget, QSplitter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import qdarkstyle
from Port import PortScanner
from SSH import SSHBruteForce
from FTP import FTPBruteForce
from xss_sql_scan import MainWindow as XSS_SQL_ScanWindow  # 导入xss_sql_scan中的MainWindow类
from IntroPage import IntroPage  # 导入IntroPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initPages()

    def initUI(self):
        self.setWindowTitle('首页')
        self.setGeometry(200, 200, 1100, 900)
        self.setWindowIcon(QIcon(r'B:\桌面\新建文件夹\pythonProject\最终版\static\1.png'))  # 设置应用程序图标

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        main_layout = QHBoxLayout(self.central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # 侧边栏布局
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(5)

        self.intro_button = QPushButton('软件介绍', self)  # 新增软件介绍按钮
        self.intro_button.setMinimumHeight(40)
        self.intro_button.clicked.connect(self.show_intro)
        sidebar_layout.addWidget(self.intro_button)

        self.port_scanner_button = QPushButton('端口扫描功能', self)
        self.port_scanner_button.setMinimumHeight(40)
        self.port_scanner_button.clicked.connect(self.show_port_scanner)
        sidebar_layout.addWidget(self.port_scanner_button)

        self.ssh_bruteforce_button = QPushButton('SSH弱口令爆破', self)
        self.ssh_bruteforce_button.setMinimumHeight(40)
        self.ssh_bruteforce_button.clicked.connect(self.show_ssh_bruteforce)
        sidebar_layout.addWidget(self.ssh_bruteforce_button)

        self.ftp_bruteforce_button = QPushButton('FTP弱口令爆破', self)
        self.ftp_bruteforce_button.setMinimumHeight(40)
        self.ftp_bruteforce_button.clicked.connect(self.show_ftp_bruteforce)
        sidebar_layout.addWidget(self.ftp_bruteforce_button)

        self.vulnerability_scan_button = QPushButton('漏洞扫描', self)  # 新增漏洞扫描按钮
        self.vulnerability_scan_button.setMinimumHeight(40)
        self.vulnerability_scan_button.clicked.connect(self.show_vulnerability_scan)
        sidebar_layout.addWidget(self.vulnerability_scan_button)

        # 添加一个占位符，确保按钮靠上
        sidebar_layout.addStretch()

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)

        # 主显示区域
        self.stacked_widget = QStackedWidget(self)

        # 使用 QSplitter 来实现可调整的侧边栏
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(sidebar_widget)
        splitter.addWidget(self.stacked_widget)
        splitter.setStretchFactor(1, 1)  # 让主显示区域占据更多空间

        # 设置侧边栏和主显示区域的初始大小
        splitter.setSizes([220, 880])  # 侧边栏初始宽度为150，主显示区域初始宽度为650

        main_layout.addWidget(splitter)

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initPages(self):
        self.intro_page = IntroPage()  # 初始化介绍页面
        self.port_scanner_page = PortScanner()
        self.ssh_bruteforce_page = SSHBruteForce()
        self.ftp_bruteforce_page = FTPBruteForce()
        self.vulnerability_scan_page = XSS_SQL_ScanWindow()  # 初始化漏洞扫描页面

        self.stacked_widget.addWidget(self.intro_page)
        self.stacked_widget.addWidget(self.port_scanner_page)
        self.stacked_widget.addWidget(self.ssh_bruteforce_page)
        self.stacked_widget.addWidget(self.ftp_bruteforce_page)
        self.stacked_widget.addWidget(self.vulnerability_scan_page)  # 添加漏洞扫描页面到stacked_widget

    def show_intro(self):
        self.stacked_widget.setCurrentWidget(self.intro_page)  # 切换到介绍页面

    def show_port_scanner(self):
        self.stacked_widget.setCurrentWidget(self.port_scanner_page)

    def show_ssh_bruteforce(self):
        self.stacked_widget.setCurrentWidget(self.ssh_bruteforce_page)

    def show_ftp_bruteforce(self):
        self.stacked_widget.setCurrentWidget(self.ftp_bruteforce_page)

    def show_vulnerability_scan(self):
        self.stacked_widget.setCurrentWidget(self.vulnerability_scan_page)  # 切换到漏洞扫描页面

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
