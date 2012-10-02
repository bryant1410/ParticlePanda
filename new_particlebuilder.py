import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty, ListProperty, StringProperty, ObjectProperty

class ParticleBuilder(Widget):
    pass

class Particle_Pos_Prop(BoxLayout):
	pos_type = StringProperty(None)
	scatter_minimum = NumericProperty(-100)
	scatter_maximum = NumericProperty(100)
	scatter_value = NumericProperty(0)

class Particle_Property(BoxLayout):
	prop_type = StringProperty(None)
	initial_minimum = NumericProperty(-100)
	initial_maximum = NumericProperty(100)
	initial_value = NumericProperty(0)
	scatter_minimum = NumericProperty(-100)
	scatter_maximum = NumericProperty(100)
	scatter_value = NumericProperty(0)
	rate_minimum = NumericProperty(0)
	rate_maximum = NumericProperty(5)
	rate_value = NumericProperty(.5)
	amount_minimum = NumericProperty(-100)
	amount_maximum = NumericProperty(100)
	amount_value = NumericProperty(0)
	iter_minimum = NumericProperty(0)
	iter_maximum = NumericProperty(10)
	iter_value = NumericProperty(1)



Factory.register('Particle_Property', Particle_Property)
Factory.register('Particle_Pos_Prop', Particle_Pos_Prop)

class ParticleBuilderApp(App):
    def build(self):
        return ParticleBuilder()

if __name__ == '__main__':
    ParticleBuilderApp().run()

