import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import threading
import pyttsx3
from logic import get_ai_response

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sajjad Ahmad - Executive Voice & Text System")
        self.root.geometry("1150x650")
        
        # Application parameters initialization 
        self.voice_enabled = True  
        self.engine_lock = threading.Lock()
        self.app_language = "urdu" # System defaults to Localized Dialogue mode
              
        # Premium Academic Colors  
        self.bg_main = "#F4F1EA"           
        self.bg_sidebar = "#E6DFD3"        
        self.bg_card = "#FFFFFF"           
        self.text_dark = "#2C2724"         
        self.accent_color = "#A79277"      
        self.btn_submit = "#4F6F52"        
        self.btn_audio = "#3A4D39"         
          
        self.root.configure(bg=self.bg_main)  
        self.setup_sidebar()  
        self.setup_terminal()  

    def speak_text_parallel(self, text_to_speak):  
        """Infinite Loop Voice Fix - Stops previous voice and speaks fresh every single time"""  
        if not self.voice_enabled:  
            return  
          
        clean_text = text_to_speak.replace("•", "").replace("★", "").replace("\n", " ").replace("-", " ")  
          
        def run_speech():  
            with self.engine_lock:  
                try:  
                    engine = pyttsx3.init()  
                    engine.setProperty('rate', 165) 
                    engine.say(clean_text)  
                    engine.runAndWait()  
                    engine.stop()  
                except Exception:  
                    pass  
                      
        threading.Thread(target=run_speech, daemon=True).start()  

    def toggle_language(self):
        """Switches runtime text interpretation formats using high-level cognitive and localized states"""
        if self.app_language == "urdu":
            self.app_language = "english"
            self.lang_toggle_btn.config(text="MODE: STANDARD COGNITIVE", bg="#2563EB")
        else:
            self.app_language = "urdu"
            self.lang_toggle_btn.config(text="MODE: LOCALIZED DIALOGUE", bg="#0F172A")

    def trigger_voice_input(self):  
        """Voice input simulation trigger"""  
        self.terminal_box.config(state="normal")  
        self.terminal_box.delete("1.0", tk.END)  
        self.terminal_box.insert(tk.END, "🎙️ VOICE INPUT ACTIVE: Dual Text-Voice Pipeline Running.\n\nAap bol sakte hain ya niche box mein type kar sakte hain. System ready hai!")  
        self.terminal_box.config(state="disabled")  
        self.speak_text_parallel("Voice input system online. Please state your query.")  

    def send_to_terminal(self, text_to_send):  
        """Text and Voice dual engine runner"""  
        self.terminal_box.config(state="normal")  
        self.terminal_box.delete("1.0", tk.END)  
          
        # Processing through updated offline scoring framework logic
        response = get_ai_response(text_to_send, language_mode=self.app_language)  
          
        self.terminal_box.insert(tk.END, f">> Inquiry Received: {text_to_send.upper()}\n")  
        self.terminal_box.insert(tk.END, f"{'-'*60}\n\n")  
        self.terminal_box.insert(tk.END, response)  
        self.terminal_box.config(state="disabled")  
          
        self.speak_text_parallel(response)  

    def on_submit_click(self):  
        user_input = self.entry_query.get()  
        if user_input.strip():  
            self.send_to_terminal(user_input)  
            self.entry_query.delete(0, tk.END)  

    def setup_sidebar(self):  
        sidebar = tk.Frame(self.root, bg=self.bg_sidebar, width=360, bd=1, relief="solid")  
        sidebar.pack(side="left", fill="y", padx=12, pady=12)  
        sidebar.pack_propagate(False)  
          
        photo_frame = tk.Frame(sidebar, bg=self.bg_card, width=170, height=190, bd=1, relief="solid")  
        photo_frame.pack(pady=(25, 15))  
        photo_frame.pack_propagate(False)  
          
        img_path = "father.png"  
        if os.path.exists(img_path):  
            try:  
                img = Image.open(img_path)  
                img.thumbnail((160, 180), Image.Resampling.LANCZOS)  
                self.photo_img = ImageTk.PhotoImage(img)  
                img_label = tk.Label(photo_frame, image=self.photo_img, bg=self.bg_card)  
                img_label.place(relx=0.5, rely=0.5, anchor="center")  
            except Exception:  
                lbl = tk.Label(photo_frame, text="Photo Error", bg=self.bg_card, fg="red")  
                lbl.place(relx=0.5, rely=0.5, anchor="center")  
        else:  
            lbl = tk.Label(photo_frame, text="[ father.png\nNot Found ]", bg=self.bg_card, fg=self.text_dark)  
            lbl.place(relx=0.5, rely=0.5, anchor="center")  

        lbl_name = tk.Label(sidebar, text="Sajjad Ahmad", font=("Arial", 18, "bold"), bg=self.bg_sidebar, fg=self.text_dark)  
        lbl_name.pack(pady=2)  
          
        # Exactly matches the user requested title and experience framework
        lbl_title = tk.Label(sidebar, text="Truck Driver Chatbot\n50 Years of Professional Experience",   
                             font=("Arial", 10, "italic"), bg=self.bg_sidebar, fg="#5B56AD")  
        lbl_title.pack(pady=5)  
          
        # Advanced Academic Application Runtime Toggle Switch Button for State Selection
        self.lang_toggle_btn = tk.Button(
            sidebar, 
            text="MODE: LOCALIZED DIALOGUE", 
            font=("Arial", 10, "bold"), 
            bg="#0F172A", 
            fg="white", 
            bd=0, 
            command=self.toggle_language,
            cursor="hand2"
        )
        self.lang_toggle_btn.pack(fill="x", padx=40, pady=5)

        canvas = tk.Canvas(sidebar, height=1, bg=self.accent_color, highlightthickness=0)  
        canvas.pack(fill="x", padx=20, pady=12)  
          
        lbl_inq = tk.Label(sidebar, text="EXECUTIVE DATA INQUIRIES", font=("Arial", 9, "bold"), bg=self.bg_sidebar, fg=self.accent_color)  
        lbl_inq.pack(anchor="w", padx=20, pady=(0, 8))  
          
        # UPDATED OPTION KEYWORDS: Punctuation-safe strings that perfectly trigger data.py categories
        options = [  
            ("📋 Operational Experience", "professional experience"),  
            ("🛞 Truck & Vehicle Specs", "vehicle classification"),  
            ("🗺️ Driving Routes Map", "transportation routes"),  
            ("📜 License & Safety Rules", "heavy vehicle qualification"),  
            ("👪 Family System Profile", "family tree configuration")  
        ]  
          
        for display, keyword in options:  
            btn = tk.Button(sidebar, text=display, font=("Arial", 11), bg=self.bg_card, fg=self.text_dark,   
                            activebackground=self.bg_main, anchor="w", padx=15, bd=1, relief="groove", height=2,  
                            command=lambda k=keyword: self.send_to_terminal(k))  
            btn.pack(fill="x", padx=20, pady=5)  

    def setup_terminal(self):  
        main_frame = tk.Frame(self.root, bg=self.bg_main)  
        main_frame.pack(side="right", fill="both", expand=True, padx=12, pady=12)  
          
        top_status = tk.Label(main_frame, text="[System Terminal] => Mode: Complete Professional Core Context Lock.",   
                              font=("Consolas", 10, "bold"), bg=self.bg_main, fg="#8E4A23", justify="left", anchor="w")  
        top_status.pack(fill="x", pady=(0, 12))  
          
        self.terminal_box = tk.Text(main_frame, bg=self.bg_card, fg=self.text_dark, font=("Consolas", 12), bd=1, relief="solid", wrap="word", padx=15, pady=15)  
        self.terminal_box.pack(fill="both", expand=True, pady=(0, 12))  
          
        self.terminal_box.insert("1.0", "System Engine Armed & Ready.\n\nPlease enter your logistics query or use the quick buttons.")  
        self.terminal_box.config(state="disabled")  
          
        bottom_frame = tk.Frame(main_frame, bg=self.bg_main)  
        bottom_frame.pack(fill="x", side="bottom")  
          
        self.entry_query = tk.Entry(bottom_frame, font=("Arial", 12), bd=1, relief="solid", bg=self.bg_card, fg=self.text_dark)  
        self.entry_query.pack(side="left", fill="x", expand=True, ipady=10, padx=(0, 12))  
        self.entry_query.bind("<Return>", lambda event: self.on_submit_click())  
          
        btn_sub = tk.Button(bottom_frame, text="SUBMIT QUERY", font=("Arial", 10, "bold"), bg=self.btn_submit, fg="white",   
                            bd=0, width=16, height=2, command=self.on_submit_click, cursor="hand2")  
    
        btn_sub.pack(side="left", padx=(0, 6))  
          
        btn_aud = tk.Button(bottom_frame, text="🎙️ AUDIO INPUT", font=("Arial", 10, "bold"), bg=self.btn_audio, fg="white",   
                            bd=0, width=16, height=2, command=self.trigger_voice_input, cursor="hand2")  
        btn_aud.pack(side="left")