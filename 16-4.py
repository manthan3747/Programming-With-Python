from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Defining the counter layout and logic
class CounterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CounterLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'  # Vertical layout
        self.spacing = 20  # Space between widgets
        self.padding = [50, 50, 50, 50]  # Padding around the layout
        
        # Initialize counter value
        self.counter_value = 0
        
        # Label to display the counter value
        self.counter_label = Label(
            text=str(self.counter_value),
            font_size=72,
            size_hint=(1, 0.6),
            halign='center',
            valign='middle'
        )
        # Bind the label size to text size for proper centering
        self.counter_label.bind(size=self.counter_label.setter('text_size'))
        self.add_widget(self.counter_label)
        
        # Button container for better spacing
        button_container = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.4),
            spacing=10
        )
        
        # Increment button
        increment_button = Button(
            text="Tap to Count!",
            font_size=28,
            size_hint=(1, 0.5),
            on_press=self.increment_counter
        )
        button_container.add_widget(increment_button)
        
        # Reset button
        reset_button = Button(
            text="Reset",
            font_size=24,
            size_hint=(1, 0.3),
            on_press=self.reset_counter
        )
        button_container.add_widget(reset_button)
        
        self.add_widget(button_container)
    
    # Function to increment the counter
    def increment_counter(self, instance):
        self.counter_value += 1
        self.counter_label.text = str(self.counter_value)
        
        # Update button text based on counter value
        if self.counter_value == 1:
            instance.text = "Keep Going!"
        elif self.counter_value == 10:
            instance.text = "Nice! Double Digits!"
        elif self.counter_value == 50:
            instance.text = "Halfway to 100!"
        elif self.counter_value == 100:
            instance.text = "Century Club!"
        elif self.counter_value % 25 == 0 and self.counter_value > 100:
            instance.text = f"Amazing! {self.counter_value} taps!"
        elif self.counter_value > 1:
            instance.text = "Tap to Count!"
    
    # Function to reset the counter
    def reset_counter(self, instance):
        self.counter_value = 0
        self.counter_label.text = str(self.counter_value)
        
        # Reset the increment button text
        increment_button = self.children[0].children[1]  # Access the increment button
        increment_button.text = "Tap to Count!"

# Main App class
class CounterApp(App):
    def build(self):
        # Set window title
        self.title = "Counter App"
        return CounterLayout()

# Running the application
if __name__ == '__main__':
    CounterApp().run()