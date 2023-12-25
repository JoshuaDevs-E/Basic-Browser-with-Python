import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.add_new_tab()
        self.setWindowIcon(QIcon('https://i.postimg.cc/y8vDdh47/logo.png'))

        # Barra de navegación
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Botones de navegación
        back_btn = QAction('↩️', self)
        back_btn.setStatusTip('↩️')
        back_btn.triggered.connect(self.current_tab().back)
        navbar.addAction(back_btn)

        forward_btn = QAction('↪️', self)
        forward_btn.setStatusTip('↪️')
        forward_btn.triggered.connect(self.current_tab().forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('↻', self)
        reload_btn.setStatusTip('↻')
        reload_btn.triggered.connect(self.current_tab().reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('🏠', self)
        home_btn.setStatusTip('🏠')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab_btn = QAction('➕', self)
        new_tab_btn.setStatusTip('New Tab')
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)

        # Barra de direcciones
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Actualizar la barra de direcciones al cargar una página
        self.current_tab().urlChanged.connect(self.update_urlbar)


        # Abrir la página de inicio por defecto
        self.navigate_home()

    def add_new_tab(self):
        tab = QWebEngineView()
        tab.setUrl(QUrl("http://www.google.com"))
        self.tabs.addTab(tab, "New Tab")

    def current_tab(self):
        return self.tabs.currentWidget()

    def navigate_home(self):
        self.current_tab().setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.current_tab().setUrl(q)

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

app = QApplication(sys.argv)
QApplication.setApplicationName("Joshua Browser")
window = Browser()
window.show()
sys.exit(app.exec_())
