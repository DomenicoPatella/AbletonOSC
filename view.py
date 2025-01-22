import Live
from functools import partial
from typing import Optional, Tuple, Any
from .handler import AbletonOSCHandler

class ViewHandler(AbletonOSCHandler):
    def __init__(self, manager):
        super().__init__(manager)
        self.class_identifier = "view"

        

    def init_api(self):
        def get_selected_scene(params: Optional[Tuple] = ()):
            return (list(self.song.scenes).index(self.song.view.selected_scene),)

        def get_selected_track(params: Optional[Tuple] = ()):
            return (list(self.song.tracks).index(self.song.view.selected_track),)

        def get_selected_clip(params: Optional[Tuple] = ()):
            return (get_selected_track()[0], get_selected_scene()[0])
        
        def get_selected_device(params: Optional[Tuple] = ()):
            return (get_selected_track()[0], list(self.song.view.selected_track.devices).index(self.song.view.selected_track.view.selected_device))
        
        def get_follow_song(params: Optional[Tuple] = ()):
            local=self.song.view.follow_song
            return(local,)

        def set_selected_scene(params: Optional[Tuple] = ()):
            self.song.view.selected_scene = self.song.scenes[params[0]]

        def set_selected_track(params: Optional[Tuple] = ()):
            self.song.view.selected_track = self.song.tracks[params[0]]

        def set_selected_clip(params: Optional[Tuple] = ()):
            set_selected_track((params[0],))
            set_selected_scene((params[1],))

        def set_selected_device(params: Optional[Tuple] = ()):
            device = self.song.tracks[params[0]].devices[params[1]]
            self.song.view.select_device(device)
            return params[0], params[1]
        
        def set_follow_song(params: Optional[Tuple] = ()):
            self.song.view.follow_song=params[0]
            


        
       
        self.osc_server.add_handler("/live/view/get/selected_scene", get_selected_scene)
        self.osc_server.add_handler("/live/view/get/selected_track", get_selected_track)
        self.osc_server.add_handler("/live/view/get/selected_clip", get_selected_clip)
        self.osc_server.add_handler("/live/view/get/selected_device", get_selected_device)
        self.osc_server.add_handler("/live/view/get/follow_song", get_follow_song)
        
        self.osc_server.add_handler("/live/view/set/selected_scene", set_selected_scene)
        self.osc_server.add_handler("/live/view/set/selected_track", set_selected_track)
        self.osc_server.add_handler("/live/view/set/selected_clip", set_selected_clip)
        self.osc_server.add_handler("/live/view/set/selected_device", set_selected_device)
        self.osc_server.add_handler("/live/view/set/follow_song", set_follow_song)
       

        #self.osc_server.add_handler("/live/application/get_current_beats_song_time", get_current_beats_song_time)
        
        self.osc_server.add_handler('/live/view/start_listen/selected_scene', partial(self._start_listen, self.song.view, "selected_scene", getter=get_selected_scene))
        self.osc_server.add_handler('/live/view/start_listen/selected_track', partial(self._start_listen, self.song.view, "selected_track", getter=get_selected_track))
        self.osc_server.add_handler('/live/view/start_listen/follow_song', partial(self._start_listen, self.song.view, "follow_song", getter=get_follow_song))
        
        self.osc_server.add_handler('/live/view/stop_listen/selected_scene', partial(self._stop_listen, self.song.view, "selected_scene"))
        self.osc_server.add_handler('/live/view/stop_listen/selected_track', partial(self._stop_listen, self.song.view, "selected_track"))
        self.osc_server.add_handler('/live/view/stop_listen/follow_song', partial(self._stop_listen, self.song.view, "follow_song"))


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

