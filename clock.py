import tkinter as tk
from tkinter import ttk
from time import strftime
import math

class EnhancedDigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Elegant Digital Clock")
        self.root.geometry("500x300")
        self.root.minsize(500, 300)
        
        # Create style object
        self.style = ttk.Style()
        
        # Initialize variables
        self.current_theme = "dark"
        self.animation_frame = 0
        self.max_frames = 100
        
        # Create main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header with app title
        self.header_frame = tk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        self.title_label = tk.Label(self.header_frame, text="ELEGANT TIMEKEEPER", font=("Helvetica", 14))
        self.title_label.pack(side=tk.LEFT)
        
        # Create container for the clock
        self.clock_container = tk.Frame(self.main_frame)
        self.clock_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Date label
        self.date_label = tk.Label(self.clock_container, font=("Helvetica", 14))
        self.date_label.pack(pady=(0, 10))
        
        # Time label
        self.time_label = tk.Label(self.clock_container, font=("Helvetica", 48, "bold"))
        self.time_label.pack()
        
        # Seconds progress bar
        self.progress_frame = tk.Frame(self.clock_container)
        self.progress_frame.pack(fill=tk.X, padx=50, pady=(10, 20))
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress_bar.pack(fill=tk.X)
        
        # Create bottom control panel
        self.control_panel = tk.Frame(self.main_frame)
        self.control_panel.pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=20)
        
        # Theme buttons with improved styling
        self.light_btn = tk.Button(self.control_panel, text="Light Theme", 
                                   command=self.light_theme, width=15, 
                                   relief=tk.RIDGE, borderwidth=2)
        self.light_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.dark_btn = tk.Button(self.control_panel, text="Dark Theme", 
                                  command=self.dark_theme, width=15, 
                                  relief=tk.RIDGE, borderwidth=2)
        self.dark_btn.pack(side=tk.LEFT)
        
        self.galaxy_btn = tk.Button(self.control_panel, text="Galaxy Theme", 
                                   command=self.galaxy_theme, width=15, 
                                   relief=tk.RIDGE, borderwidth=2)
        self.galaxy_btn.pack(side=tk.LEFT, padx=(10, 0))
        
        # Set initial theme
        self.dark_theme()
        
        # Start clock update
        self.update_time()
        self.animate_clock()
    
    def update_time(self):
        # Update time
        time_string = strftime('%I:%M:%S %p')
        self.time_label.config(text=time_string)
        
        # Update date
        date_string = strftime('%A, %B %d, %Y')
        self.date_label.config(text=date_string)
        
        # Update progress bar based on seconds
        seconds = int(strftime('%S'))
        self.progress_bar['value'] = (seconds / 60) * 100
        
        # Schedule next update
        self.root.after(1000, self.update_time)
    
    def animate_clock(self):
        # Simple breathing animation for the clock
        self.animation_frame = (self.animation_frame + 1) % self.max_frames
        scale = 1.0 + 0.03 * math.sin(2 * math.pi * self.animation_frame / self.max_frames)
        
        font_size = int(48 * scale)
        self.time_label.config(font=("Helvetica", font_size, "bold"))
        
        # Continue animation
        self.root.after(50, self.animate_clock)
    
    def light_theme(self):
        self.current_theme = "light"
        
        # Configure main window and frames
        self.root.configure(bg="#f0f0f0")
        self.main_frame.configure(bg="#f0f0f0")
        self.header_frame.configure(bg="#f0f0f0")
        self.clock_container.configure(bg="#f0f0f0")
        self.progress_frame.configure(bg="#f0f0f0")
        self.control_panel.configure(bg="#f0f0f0")
        
        # Configure labels
        self.title_label.configure(bg="#f0f0f0", fg="#333333")
        self.time_label.configure(bg="#f0f0f0", fg="#333333")
        self.date_label.configure(bg="#f0f0f0", fg="#555555")
        
        # Configure buttons
        self.light_btn.configure(bg="#e0e0e0", fg="#333333", relief=tk.SUNKEN)
        self.dark_btn.configure(bg="#f0f0f0", fg="#333333", relief=tk.RAISED)
        self.galaxy_btn.configure(bg="#f0f0f0", fg="#333333", relief=tk.RAISED)
        
        # Configure progress bar style
        self.style.configure("TProgressbar", background='#4CAF50', troughcolor='#e0e0e0')
    
    def dark_theme(self):
        self.current_theme = "dark"
        
        # Configure main window and frames
        self.root.configure(bg="#222222")
        self.main_frame.configure(bg="#222222")
        self.header_frame.configure(bg="#222222")
        self.clock_container.configure(bg="#222222")
        self.progress_frame.configure(bg="#222222")
        self.control_panel.configure(bg="#222222")
        
        # Configure labels
        self.title_label.configure(bg="#222222", fg="#4CAF50")
        self.time_label.configure(bg="#222222", fg="#ffffff")
        self.date_label.configure(bg="#222222", fg="#aaaaaa")
        
        # Configure buttons
        self.light_btn.configure(bg="#333333", fg="#ffffff", relief=tk.RAISED)
        self.dark_btn.configure(bg="#333333", fg="#4CAF50", relief=tk.SUNKEN)
        self.galaxy_btn.configure(bg="#333333", fg="#ffffff", relief=tk.RAISED)
        
        # Configure progress bar style
        self.style.configure("TProgressbar", background='#4CAF50', troughcolor='#333333')
    
    def galaxy_theme(self):
        self.current_theme = "galaxy"
        
        # Configure main window and frames
        self.root.configure(bg="#0a0a2a")
        self.main_frame.configure(bg="#0a0a2a")
        self.header_frame.configure(bg="#0a0a2a")
        self.clock_container.configure(bg="#0a0a2a")
        self.progress_frame.configure(bg="#0a0a2a")
        self.control_panel.configure(bg="#0a0a2a")
        
        # Configure labels
        self.title_label.configure(bg="#0a0a2a", fg="#bb9af7")
        self.time_label.configure(bg="#0a0a2a", fg="#7aa2f7")
        self.date_label.configure(bg="#0a0a2a", fg="#7dcfff")
        
        # Configure buttons
        self.light_btn.configure(bg="#1a1b26", fg="#c0caf5", relief=tk.RAISED)
        self.dark_btn.configure(bg="#1a1b26", fg="#c0caf5", relief=tk.RAISED)
        self.galaxy_btn.configure(bg="#1a1b26", fg="#bb9af7", relief=tk.SUNKEN)
        
        # Configure progress bar style
        self.style.configure("TProgressbar", background='#bb9af7', troughcolor='#1a1b26')

# Create the main window and start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedDigitalClock(root)
    root.mainloop()