import tkinter as tk
from tkinter import ttk


def load_themes():
    style = ttk.Style()
    style.theme_create("light_theme", parent="clam", settings={
        "TButton": {
            "configure": {
                "background": "#ffffff", 
                "foreground": "white", 
                "font": ('Century Gothic', 12), 
                "relief": "flat", 
                "padding": 0, 
                "border": 0
                }
        },

        "Gray.TButton": {
            "configure": {
                "background": "#fd546b", 
                "foreground": "#212121"
                }
        },

        "TFrame": {
            "configure": {"background": "#FFFFFF"}
        },

        "Custom.TFrame": {
            "configure": {"background": "#fd546b"}
        },

        "TText": {
            "configure": {"background": "#3f3f3f"}
        },

        "TLabel": {
            "configure": {
                "font": ('Century Gothic', 12), 
                "foreground": "#212121", 
                "background" : "white"
                }
        },

        "TCheckbutton": {
            "configure": {
                "background": "#fd546b", 
                "font": ('Century Gothic', 12)
                }
        },

        "Bg.TFrame": {
            "configure": {
                "background": "#dcdcdc"    
            }
        }
    })

    style.theme_create("dark_theme", parent="clam", settings={
        "TButton": {
            "configure": {
                "background": "#24293d", 
                "foreground": 
                "white", 
                "font": ('Century Gothic', 12),
                "relief": "flat", 
                "padding": 0, 
                "border": 0
                }
        },

        "Gray.TButton": {
            "configure": {
                "background": "#fd546b", 
                "foreground": "#24293d"
                }
        },

        "TFrame": {
            "configure": {"background": "#24293d"}
        },

        "Custom.TFrame": {
            "configure": {"background": "#fd546b"}
        },

        "TText": {
            "configure": {"background": "#24293d"}
        },

        "TLabel": {
            "configure": {
                "font": ('Century Gothic', 12),
                "foreground": "white", 
                "background": "#24293d"
                }
        },

        "TCheckbutton": {
            "configure": {
                "background": "#fd546b", 
                "font": ('Century Gothic', 12)
                }
        },

        "Bg.TFrame": {
            "configure": {
                "background": "#303548"    
            }
        }
    })