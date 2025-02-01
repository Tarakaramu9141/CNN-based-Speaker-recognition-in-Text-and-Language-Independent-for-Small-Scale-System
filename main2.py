import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import tkinter.filedialog as filedialog

# Create a tooltip class
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip_window, text=self.text, background="lightyellow", borderwidth=1, relief="solid")
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

# Main application class
class SpeakerRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CNN Based Speaker Recognition")
        self.root.geometry("1200x800")
        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Create frames for each tab
        self.dataset_frame = ttk.Frame(self.notebook)
        self.model_frame = ttk.Frame(self.notebook)
        self.prediction_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.dataset_frame, text='Dataset')
        self.notebook.add(self.model_frame, text='Model Training')
        self.notebook.add(self.prediction_frame, text='Prediction')

        # Dataset Tab
        self.create_dataset_tab()

        # Model Training Tab
        self.create_model_tab()

        # Prediction Tab
        self.create_prediction_tab()

        # Status Bar
        self.status = tk.Label(root, text="Welcome to the Speaker Recognition System", bd=1, relief=tk.SUNKEN, anchor='w')
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def create_dataset_tab(self):
        # Upload Dataset Button
        upload_button = ttk.Button(self.dataset_frame, text="Upload Speech Dataset", command=self.uploadDataset)
        upload_button.pack(pady=20)
        ToolTip(upload_button, "Select the directory containing the speech dataset.")

        # Path Label
        self.path_label = tk.Label(self.dataset_frame, text="", wraplength=600)
        self.path_label.pack(pady=10)

    def create_model_tab(self):
        # Run CNN Button
        cnn_button = ttk.Button(self.model_frame, text="Run CNN Algorithm", command=self.runCNN)
        cnn_button.pack(pady=20)
        ToolTip(cnn_button, "Train the CNN model on the uploaded dataset.")

        # Run Random Forest Button
        rf_button = ttk.Button(self.model_frame, text="Run Random Forest Algorithm", command=self.runRandomForest)
        rf_button.pack(pady=20)
        ToolTip(rf_button, "Train the Random Forest model on the dataset.")

        # Progress Bar
        self.progress = ttk.Progressbar(self.model_frame, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=20)

    def create_prediction_tab(self): # Upload Test Audio Button
        predict_button = ttk.Button(self.prediction_frame, text="Upload Test Audio & Recognize Speaker", command=self.predict)
        predict_button.pack(pady=20)
        ToolTip(predict_button, "Select an audio file to recognize the speaker.")

        # Text Area for Output
        self.text_output = tk.Text(self.prediction_frame, height=15, width=90)
        self.text_output.pack(pady=10)
        self.text_output.config(font=('times', 12, 'bold'))

    def uploadDataset(self):
        # Function to upload dataset
        filename = filedialog.askdirectory(initialdir=".")
        self.path_label.config(text=filename)
        self.text_output.insert(tk.END, filename + " loaded\n\n")
        self.status.config(text="Dataset uploaded successfully.")

    def runCNN(self):
        # Function to run CNN
        self.progress.start()
        # Simulate training process
        self.status.config(text="Training CNN model...")
        # Add your CNN training code here
        self.progress.stop()
        self.status.config(text="CNN model trained successfully.")

    def runRandomForest(self):
        # Function to run Random Forest
        self.progress.start()
        # Simulate training process
        self.status.config(text="Training Random Forest model...")
        # Add your Random Forest training code here
        self.progress.stop()
        self.status.config(text="Random Forest model trained successfully.")

    def predict(self):
        # Function to predict speaker
        self.text_output.delete('1.0', tk.END)
        filename = filedialog.askopenfilename(initialdir="testSpeech")
        # Add your prediction code here
        self.text_output.insert(tk.END, "Uploaded Speech Recognized for Person: [Name]\n\n")
        self.status.config(text="Prediction completed.")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = SpeakerRecognitionApp(root)
    root.mainloop()