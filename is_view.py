 # test pointer class view 
        def is_view_arranger(_):
            application = Live.Application.get_application()
            view=application.view
            res=view.is_view_visible("Arranger")
            return res,
        self.osc_server.add_handler("/live/application/view/get/is_view_arranger", is_view_arranger)
        self.osc_server.send("/live/application/view/get/is_view_arranger")

       # test pointer class view 
        def is_view_session(_):
            application = Live.Application.get_application()
            view=application.view
            res=view.is_view_visible("Session")
            return res,
        self.osc_server.add_handler("/live/application/view/get/is_view_session", is_view_session)
        self.osc_server.send("/live/application/view/get/is_view_session")