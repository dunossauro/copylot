from kivy.tests.common import GraphicUnitTest
from app import Copylot


class BoxGraphicUnitTest(GraphicUnitTest):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        self.app = Copylot().build()
        self.render(self.app)


class TestRoot(BoxGraphicUnitTest):
    def test_copylot_label_render(self):
        assert self.app.ids.first_label.text == 'Copylot'
