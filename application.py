import Live
from typing import Optional, Tuple, Any
from .handler import AbletonOSCHandler

class ApplicationHandler(AbletonOSCHandler):
    def init_api(self):
        #--------------------------------------------------------------------------------
        # Generic callbacks
        #--------------------------------------------------------------------------------
        def get_version(_) -> Tuple:
            application = Live.Application.get_application()
            ##self.logger.info("## Live")
            ##log_object_info(Live, obj_name="Live")
            ##self.logger.info("## Application")
            ##log_object_info(application, obj_name="Application")
            ##self.logger.info("## Application.View")
            ##log_object_info(application.view, obj_name="Application.View")
            ##self.logger.info("## Song")
            ##log_object_info(Live.Song, obj_name="Application.Song")
            ##self.logger.info("## Song")
            ##log_object_info(Live.Song.Song, obj_name="Application.Song.Song")
            return application.get_major_version(), application.get_minor_version()
        self.osc_server.add_handler("/live/application/get/version", get_version)
        self.osc_server.send("/live/startup")
        

        def get_average_process_usage(_) -> Tuple:
            application = Live.Application.get_application()
            return application.average_process_usage,
        self.osc_server.add_handler("/live/application/get/average_process_usage", get_average_process_usage)
        self.osc_server.send("/live/application/get/average_process_usage")

        def get_version_string(_):
            application = Live.Application.get_application()
            return str(application.get_version_string()),
        self.osc_server.add_handler("/live/application/get/version_string", get_version_string)
        self.osc_server.send("/live/application/get/version_string")
        
       # Application.view toggle_browser()
       # Displays the device chain and the browser and activates Hot-Swap Mode for the selected device. Calling this function again deactivates Hot-Swap Mode.
        def set_toggle_browser(_):
            application = Live.Application.get_application()
            view=application.view
            view.toggle_browse()
            return str("toogle"),
        self.osc_server.add_handler("/live/application/view/set/toggle_browser", set_toggle_browser)
        self.osc_server.send("/live/application/view/set/toggle_browser")

       # Application.view :is_view_arranger() 
       # Query if view arranger is visible
        def is_view_arranger(_):
            application = Live.Application.get_application()
            view=application.view
            res=view.is_view_visible("Arranger")
            return res,
        self.osc_server.add_handler("/live/application/view/get/is_view_arranger", is_view_arranger)
        self.osc_server.send("/live/application/view/get/is_view_arranger")

       # Application.view :is_view_session() 
       # Query if view session is visible 
        def is_view_session(_):
            application = Live.Application.get_application()
            view=application.view
            res=view.is_view_visible("Session")
            return res,
        self.osc_server.add_handler("/live/application/view/get/is_view_session", is_view_session)
        self.osc_server.send("/live/application/view/get/is_view_session")

        # Application.view :show_view(arg1) 'Arranger' , 'Browser' , 'Session' ,  'Detail/DeviceChain'  
        def show_view(params: Optional[Tuple] = ()):
            application = Live.Application.get_application()
            view=application.view
            view.show_view(params[0])
            return str("show_view"),
        self.osc_server.add_handler("/live/application/view/set/show_view", show_view)
        self.osc_server.send("/live/application/view/set/show_view")

         ##  Parameters: direction  view_name  modifier_pressed
            #
            # direction [int] is 0 = up, 1 = down, 2 = left, 3 = right
            # modifier_pressed [bool] If view_name is "Arranger" and modifier_pressed is 1 and direction is left or right, then the size of the selected time region is modified, otherwise the position of the playback cursor is moved.
            # Not all views are scrollable, and not in all directions. Currently, only the Arranger , Browser , Session , and Detail/DeviceChain views can be scrolled.
            # You can also pass an empty view_name " " , which refers to the Arrangement or Session View (whichever view is visible).
            #view.zoom_view(params[0],params[1],params[2])
        def set_scroll_view(params: Optional[Tuple] = ()):
            application = Live.Application.get_application()
            view=application.view
            view.scroll_view(params[0],params[1],params[2])
            return str("scroll"),
        self.osc_server.add_handler("/live/application/set/scroll_view", set_scroll_view)
        self.osc_server.send("/live/application/set/scroll_view")

        ##  Parameters: direction  view_name  modifier_pressed
            #
            # direction [int] is 0 = up, 1 = down, 2 = left, 3 = right
            # modifier_pressed [bool] If view_name is "Arranger" and modifier_pressed is 1 and direction is left or right, then the size of the selected time region is modified, otherwise the position of the playback cursor is moved.
            # Not all views are scrollable, and not in all directions. Currently, only the Arranger , Browser , Session , and Detail/DeviceChain views can be scrolled.
            # You can also pass an empty view_name " " , which refers to the Arrangement or Session View (whichever view is visible).
            #view.zoom_view(params[0],params[1],params[2])
        def set_zoom_view(params: Optional[Tuple] = ()):
            application = Live.Application.get_application()
            view=application.view
            
            view.zoom_view(params[0],params[1],params[2])
            return str("scroll"),
        self.osc_server.add_handler("/live/application/set/zoom_view", set_zoom_view)
        self.osc_server.send("/live/application/set/zoom_view")    

        # Debug purpose only
        def log_object_info(obj, obj_name="object"):
         attributes = dir(obj)
         self.logger.info(f"Oggetto '{obj_name}': elenco metodi e proprietà:")
         for attr in attributes:
            try:
                attr_value = getattr(obj, attr)  # Ottieni il valore dell'attributo
                self.logger.info(f"  - {attr}: {repr(attr_value)}")
            except Exception as e:
                self.logger.info(f"  - {attr}: (non accessibile, errore: {e})")
