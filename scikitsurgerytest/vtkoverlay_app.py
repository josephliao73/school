import sys
from PySide6.QtWidgets import QApplication
from sksurgeryutils.common_overlay_apps import OverlayBaseWidget

class OverlayApp(OverlayBaseWidget):
    def update_view(self):
        _, image = self.video_source.read()
        self.vtk_overlay_window.set_video_image(image)
        self.vtk_overlay_window.Render()
    
if __name__ == "__main__":
    app = QApplication([])
    video_source = 0
    viewer = OverlayApp(video_source)
    model_dir = "./models"
    viewer.add_vtk_models_from_dir(model_dir)
    #
    viewer.show()
    viewer.start()
    sys.exit(app.exec_())