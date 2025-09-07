from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

# Defining the text input layout and logic
class TextInputLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(TextInputLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'  # Vertical layout
        self.spacing = 20  # Space between widgets
        self.padding = [30, 30, 30, 30]  # Padding around the layout
        
        # Title label
        title_label = Label(
            text="Text Input App",
            font_size=32,
            size_hint=(1, 0.1),
            halign='center',
            valign='middle'
        )
        title_label.bind(size=title_label.setter('text_size'))
        self.add_widget(title_label)
        
        # Text input field where users can type
        self.text_input = TextInput(
            hint_text="Type your message here...",
            font_size=20,
            size_hint=(1, 0.15),
            multiline=True,
            cursor_blink=True
        )
        self.add_widget(self.text_input)
        
        # Button container for action buttons
        button_container = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.1),
            spacing=15
        )
        
        # Display button to show the typed text
        display_button = Button(
            text="Display Text",
            font_size=22,
            size_hint=(0.5, 1),
            on_press=self.display_text
        )
        button_container.add_widget(display_button)
        
        # Clear button to clear both input and display
        clear_button = Button(
            text="Clear All",
            font_size=22,
            size_hint=(0.5, 1),
            on_press=self.clear_all
        )
        button_container.add_widget(clear_button)
        
        self.add_widget(button_container)
        
        # Display area label
        display_title = Label(
            text="Your Text Will Appear Below:",
            font_size=18,
            size_hint=(1, 0.08),
            halign='center',
            valign='middle'
        )
        display_title.bind(size=display_title.setter('text_size'))
        self.add_widget(display_title)
        
        # Label to display the typed text
        self.display_label = Label(
            text="[No text entered yet]",
            font_size=20,
            size_hint=(1, 0.57),
            halign='left',
            valign='top',
            text_size=(None, None),
            markup=True
        )
        self.display_label.bind(size=self.update_display_text_size)
        self.add_widget(self.display_label)
    
    # Function to display the typed text
    def display_text(self, instance):
        input_text = self.text_input.text.strip()
        
        if input_text:
            # Display the text with some formatting
            self.display_label.text = f"[b]You typed:[/b]\n\n{input_text}"
            # Update character count
            char_count = len(input_text)
            word_count = len(input_text.split()) if input_text else 0
            instance.text = f"Display Text\n({char_count} chars, {word_count} words)"
        else:
            self.display_label.text = "[i]Please enter some text first![/i]"
            instance.text = "Display Text"
    
    # Function to clear both input and display
    def clear_all(self, instance):
        self.text_input.text = ""
        self.display_label.text = "[No text entered yet]"
        
        # Reset the display button text
        display_button = self.children[2].children[1]  # Access the display button
        display_button.text = "Display Text"
        
        # Focus back to the text input
        self.text_input.focus = True
    
    # Function to update display label text size for proper wrapping
    def update_display_text_size(self, instance, size):
        instance.text_size = (size[0] - 20, None)  # Leave some margin

# Main App class
class TextInputApp(App):
    def build(self):
        # Set window title
        self.title = "Text Input App"
        return TextInputLayout()

# Running the application
if __name__ == '__main__':
    TextInputApp().run()