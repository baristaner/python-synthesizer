import tkinter as tk
from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth,Triangle
from pydub.effects import low_pass_filter, high_pass_filter

class SynthesizerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Synthesizer")
        self.geometry("250x300")
        self.create_widgets()
    
    def create_widgets(self):
        self.frequency_label = tk.Label(self, text="Frequency")
        self.frequency_label.pack()
        self.frequency_entry = tk.Entry(self)
        self.frequency_entry.pack()
        
        self.duration_label = tk.Label(self, text="Duration")
        self.duration_label.pack()
        self.duration_entry = tk.Entry(self)
        self.duration_entry.pack()
        
        self.waveform_label = tk.Label(self, text="Waveform")
        self.waveform_label.pack()
        self.waveform_var = tk.StringVar()
        self.waveform_var.set("sine")
        self.waveform_dropdown = tk.OptionMenu(self, self.waveform_var, "sine", "square", "sawtooth","triangle")
        self.waveform_dropdown.pack()

        self.filter_label = tk.Label(self, text="Filter")
        self.filter_label.pack()
        self.filter_var = tk.StringVar()
        self.filter_var.set("low_pass")
        self.filter_dropdown = tk.OptionMenu(self, self.filter_var, "low_pass", "high_pass")
        self.filter_dropdown.pack()

        self.cutoff_label = tk.Label(self, text="Cutoff Frequency")
        self.cutoff_label.pack()
        self.cutoff_entry = tk.Entry(self)
        self.cutoff_entry.pack()
        
        self.play_button = tk.Button(self, text="Play", command=self.play)
        self.play_button.pack()
    
    def play(self):
        frequency = float(self.frequency_entry.get())
        duration = float(self.duration_entry.get())
        waveform = self.waveform_var.get()
        filter_type = self.filter_var.get()
        cutoff = float(self.cutoff_entry.get())

        # Generate the waveform
        if waveform == 'sine':
            wave = Sine(frequency).to_audio_segment(duration * 1000)
        elif waveform == 'square':
            wave = Square(frequency).to_audio_segment(duration * 1000)
        elif waveform == 'sawtooth':
            wave = Sawtooth(frequency).to_audio_segment(duration * 1000)
        elif waveform == 'triangle':
            wave = Sawtooth(frequency).to_audio_segment(duration * 1000)
        else:
            print("Invalid waveform")
            return

        # Apply the filter
        if filter_type == 'low_pass':
            wave = low_pass_filter(wave, cutoff)
        elif filter_type == 'high_pass':
            wave = high_pass_filter(wave, cutoff)
        else:
            print("Invalid filter type")
        return

        # Play the filtered wave
        wave.export("filtered_wave.wav", format="wav")

if __name__ == "__main__":
    app = SynthesizerApp()
    app.mainloop()

