
import tkinter as tk
from ArabicSignToTextScreen import ArabicSignToTextScreen
from EnglishSignToTextScreen import EnglishSignToTextScreen
from EnglishTextToSignScreen import EnglishTextToSignScreen
from PIL import ImageTk, Image






class StartWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("+0+0")
        self.root.title("Let's Sign")
        self.root.iconbitmap("icon.ico")
        self.root.config(bg='#7fcdcd')
        self.root.minsize(1350, 690)
        self.root.maxsize(1300, 530)
        label = tk.Label(self.root, text='Choose the preferable Language:', bg='#7fcdcd', fg='#FFFFFF',
                         font='android 30')
        label.place(x=380, y=220)
        label = tk.Label(self.root, text='                         : اختر اللغة المناسبة', bg='#7fcdcd', fg='#FFFFFF',
                         font='android 30')
        label.place(x=400, y=280)
                # Load the flag images
        american_flag_img = Image.open("usa.png")
        egyptian_flag_img = Image.open("egypt.png")
                # Resize the flag images
        american_flag_img = american_flag_img.resize((100, 100))
        egyptian_flag_img = egyptian_flag_img.resize((100, 100))
        
        # Create PhotoImage objects from the flag images
        self.american_flag_photo = ImageTk.PhotoImage(american_flag_img)
        self.egyptian_flag_photo = ImageTk.PhotoImage(egyptian_flag_img)
        
        
        arabic_button = tk.Button(self.root, bg='#7fcdcd', image=self.egyptian_flag_photo)
        arabic_button.config(width=100, height=100)
        arabic_button.config(command=self.arabic_button_clicked)
        arabic_button.place(x=750, y=400)

        english_button = tk.Button(self.root, bg='#7fcdcd', image=self.american_flag_photo)
        english_button.config(width=100, height=100)
        english_button.config(command=self.english_button_clicked)
        english_button.place(x=450, y=400)
        
    def english_button_clicked(self):
        self.root.destroy()
        EnglishWindow()

    def arabic_button_clicked(self):
        self.root.destroy()
        ArabicWindow() 
        
        
class TranslationEnglishWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("+0+0")
        self.root.title("Let's Sign")
        self.root.iconbitmap("icon.ico")
        self.root.config(bg='#FBF0C8')
        self.root.minsize(1350, 690)
        self.root.maxsize(1350, 690)
        label = tk.Frame(self.root, height=700, width=270, background='#7fcdcd')
        label.grid(row=0, column=1)

        sign_to_text_button = tk.Button(self.root, text="Sign To Text", bg='white', font='android 20', fg='#0091E8')
        sign_to_text_button.config(width=10, height=2)
        sign_to_text_button.config(command=self.translation_button_clicked)
        sign_to_text_button.place(x=50, y=150)

        text_to_sign_button = tk.Button(self.root, text="Text To Sign", bg='white', font='android 20', fg='#0091E8')
        text_to_sign_button.config(width=10, height=2)
        text_to_sign_button.config(command=self.animation_button_clicked)
        text_to_sign_button.place(x=50, y=350)

        back_button = tk.Button(self.root, text="Back", bg='white', font='android 20', fg='#0091E8')
        back_button.config(width=10, height=2)
        back_button.config(command=self.back_button_clicked)
        back_button.place(x=50, y=550)
        self.root.mainloop()

    def animation_button_clicked(self):
        self.root.destroy()
        EnglishTextToSignScreen()

    def translation_button_clicked(self):
        EnglishSignToTextScreen()


    def back_button_clicked(self):
        self.root.destroy()
        EnglishWindow()


class DictionaryEnglishWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("+0+0")
        self.root.title("Let's Sign")
        self.root.iconbitmap("icon.ico")
        self.root.config(bg='#FBF0C8')
        self.root.minsize(1350, 690)
        self.root.maxsize(1350, 690)
        label = tk.Frame(self.root, height=700, width=270, background='#7fcdcd')
        label.grid(row=0, column=1)

        alphabets_button = tk.Button(self.root, text="Alphabets", bg='white', font='android 20', fg='#0091E8')
        alphabets_button.config(width=10, height=2)
        alphabets_button.config(command=self.alphabets_button_clicked)
        alphabets_button.place(x=50, y=150)
        
        numbers_button = tk.Button(self.root, text="Phrases", bg='white', font='android 20', fg='#0091E8')
        numbers_button.config(width=10, height=2)
        numbers_button.config(command=self.phrases_button_clicked)
        numbers_button.place(x=50, y=350)

        back_button = tk.Button(self.root, text="Back", bg='white', font='android 20', fg='#0091E8')
        back_button.config(width=10, height=2)
        back_button.config(command=self.back_button_clicked)
        back_button.place(x=50, y=550)
        self.root.mainloop()

    def alphabets_button_clicked(self):
        self.root.destroy()
        from EnglishSignLanguageDictionary import EnglishSignLanguageDictionary
        root = tk.Tk()
        root.geometry("800x600+420+60")
        EnglishSignLanguageDictionary(root)
        root.mainloop()

    def phrases_button_clicked(self):
        self.root.destroy()
        root = tk.Tk()
        root.geometry("600x600+420+60")
        from EnglishDictionaryPhrases import EnglishDictionaryPhrases
        EnglishDictionaryPhrases(root)
        root.mainloop()


    def back_button_clicked(self):
        self.root.destroy()
        EnglishWindow()


class TranslationArabicWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("+0+0")
        self.root.minsize(1350, 690)
        self.root.maxsize(1350, 690)
        self.root.title("Let's Sign")
        self.root.iconbitmap("icon.ico")
        self.root.config(bg='#FBF0C8')
        label = tk.Frame(self.root, height=700, width=280, background='#7fcdcd')
        label.grid(row=0, column=1)
        label.place(x=1100, y=0)

        sign_to_text_button = tk.Button(self.root, text="من اشارة الى نص", bg='white', font='android 20', fg='#0091E8')
        sign_to_text_button.config(width=10, height=2)
        sign_to_text_button.config(command=self.arabic_sign_to_text_button_clicked)
        sign_to_text_button.grid(row=0, column=1)
        sign_to_text_button.place(x=1138, y=100)

        text_to_sign_button = tk.Button(self.root, text="من نص الى اشارة", bg='white', font='android 20', fg='#0091E8')
        text_to_sign_button.config(width=10, height=2)
        text_to_sign_button.config(command=self.arabic_text_to_sign_button_clicked)
        text_to_sign_button.grid(row=0, column=1)
        text_to_sign_button.place(x=1138, y=350)

        back_button = tk.Button(self.root, text="الرجوع", bg='white', font='android 20', fg='#0091E8')
        back_button.config(width=10, height=2)
        back_button.config(command=self.back_button_clicked)
        back_button.place(x=1138, y=550)
        self.root.mainloop()

    def arabic_text_to_sign_button_clicked(self):
        self.root.destroy()
        from ArabicTextToSignScreen import ArabicTextToSignScreen
        ArabicTextToSignScreen()

    def arabic_sign_to_text_button_clicked(self):
        ArabicSignToTextScreen()

    def back_button_clicked(self):
        self.root.destroy()
        ArabicWindow()


class EnglishWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Let's Sign")
        self.root.geometry("+0+0")
        self.root.iconbitmap("icon.ico")
        self.root.config(bg='#7fcdcd')
        self.root.minsize(1350, 690)
        self.root.maxsize(1300, 530)

        label = tk.Label(self.root, text='How can i help you ?:', bg='#7fcdcd', fg='#FFFFFF', font='android 30')
        label.place(x=495, y=150)

        dict_button = tk.Button(self.root, text="Dictionary", bg='white', font='android 20')
        dict_button.config(width=10, height=2)
        dict_button.config(command=self.dictionary_button_clicked)
        dict_button.place(x=780, y=250)

        trans_button = tk.Button(self.root, text="Translation", bg='white', font='android 20')
        trans_button.config(width=10, height=2)
        trans_button.config(command=self.english_button_clicked)
        trans_button.place(x=400, y=250)

        back_button = tk.Button(self.root, text="Back to Previous Menu", bg='white', font='android 20')
        back_button.config(width=20, height=2)
        back_button.config(command=self.back_to_prev_menu)
        back_button.place(x=500, y=400)
        self.root.mainloop()
    def dictionary_button_clicked(self):
        self.root.destroy()
        DictionaryEnglishWindow()
    def english_button_clicked(self):
        self.root.destroy()
        TranslationEnglishWindow()

    def back_to_prev_menu(self):
        self.root.destroy()
        StartWindow()

class ArabicWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Let's Sign")
        self.root.geometry("+0+0")
        self.root.config(bg='#7fcdcd')
        self.root.iconbitmap("icon.ico")
        self.root.minsize(1350, 690)
        self.root.maxsize(1300, 530)

        label = tk.Label(self.root, text=': كيف أستطيع مساعدتك', bg='#7fcdcd', fg='#FFFFFF', font='android 30')
        label.place(x=495, y=150)

        back_button = tk.Button(self.root, text="رجوع الي القائمه السابقة", bg='white', font='android 20')
        back_button.config(width=20, height=2)
        back_button.config(command=self.back_to_prev_menu)
        back_button.grid(row=0, column=1)
        back_button.place(x=500, y=400)

        dict_button = tk.Button(self.root, text="القاموس", bg='white', font='android 20')
        dict_button.config(width=10, height=2)
        dict_button.config(command=self.go_to_dict_button_clicked)
        dict_button.place(x=400, y=250)


        trans_button = tk.Button(self.root, text="الترجمة", bg='white', font='android 20')
        trans_button.config(width=10, height=2)
        trans_button.config(command=self.go_to_translation_button_clicked)
        trans_button.place(x=780, y=250)

        self.root.mainloop()

    def go_to_translation_button_clicked(self):
        self.root.destroy()
        TranslationArabicWindow()
    def go_to_dict_button_clicked(self):
        self.root.destroy()
        root = tk.Tk()
        root.geometry("800x600+420+60")
        from ArabicSignLanguageDictionary import ArabicSignLanguageDictionary
        ArabicSignLanguageDictionary(root)


    def back_to_prev_menu(self):
        self.root.destroy()
        StartWindow()
