import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer

class PomodoroTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таймер-помидорка")
        
        self.pomodoro_duration = 25 * 60  # 25 минут
        self.remaining_time = self.pomodoro_duration
        
        self.layout = QVBoxLayout()
        
        self.timer_label = QLabel(self.format_time(self.remaining_time))
        self.timer_label.setStyleSheet("font-size: 48px;")
        
        self.start_button = QPushButton("Начать")
        self.stop_button = QPushButton("Пауза")
        self.reset_button = QPushButton("Сбросить")
        
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.reset_button)
        
        self.setLayout(self.layout)
        
        self.q_timer = QTimer(self)
        self.q_timer.setInterval(1000)  # Обновляем каждую секунду
        self.q_timer.timeout.connect(self.update_timer)
        
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        
    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
        
    def start_timer(self):
        self.q_timer.start()

    def stop_timer(self):
        self.q_timer.stop()

    def reset_timer(self):
        self.stop_timer()
        self.remaining_time = self.pomodoro_duration
        self.timer_label.setText(self.format_time(self.remaining_time))

    def update_timer(self):
        self.remaining_time -= 1
        self.timer_label.setText(self.format_time(self.remaining_time))
        if self.remaining_time <= 0:
            self.stop_timer()
            print("Время вышло!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer_app = PomodoroTimer()
    timer_app.show()
    sys.exit(app.exec())
