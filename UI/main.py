from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class JeevesApp(App):
    pass

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        user_city = self.search_input.text
        api_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + user_city + '&appid=44db6a862fba0b067b1930da0d769e98'
        request = UrlRequest(api_url, self.found_location)

    def found_location(self, request, data):
        print request
        print data



if __name__ == '__main__':
        JeevesApp().run()