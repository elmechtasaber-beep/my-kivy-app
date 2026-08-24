from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

# الشاشة الأولى: تسجيل الدخول الوهمي
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="تسجيل الدخول", font_size=24))
        
        self.username = TextInput(hint_text="اسم المستخدم", multiline=False)
        self.password = TextInput(hint_text="كلمة السر", password=True, multiline=False)
        
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        
        btn_login = Button(text="دخول", size_hint_y=None, height=50)
        btn_login.bind(on_press=self.go_to_main)
        layout.add_widget(btn_login)
        
        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main_room'

# الشاشة الثانية: الغرف الصوتية والرصيد
class MainRoomScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.coins = 1000000000000000  # رصيد تجريبي ضخم
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.lbl_coins = Label(text=f"الرصيد: {self.coins:,}", font_size=18)
        layout.add_widget(self.lbl_coins)
        
        layout.add_widget(Label(text="غرفة الصوت رقم 1 (2/2 مقاعد)", font_size=20))
        
        btn_game = Button(text="لعبة الفواكه والجاك بوت (قريباً)", size_hint_y=None, height=60)
        btn_gift = Button(text="إرسال هدية (100 مليون)", size_hint_y=None, height=60)
        btn_gift.bind(on_press=self.send_gift)
        
        layout.add_widget(btn_game)
        layout.add_widget(btn_gift)
        
        self.add_widget(layout)

    def send_gift(self, instance):
        if self.coins >= 100000000:
            self.coins -= 100000000
            self.lbl_coins.text = f"الرصيد: {self.coins:,}"

class ChatApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainRoomScreen(name='main_room'))
        return sm

if __name__ == '__main__':
    ChatApp().run()
