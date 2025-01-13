-- Controls that hold Application information 
local bAlive = false
local lblLive = root:findByName("lblLive", true)
local lblVer = root:findByName("lblVer", true)
local lblAve = root:findByName("lblAve", true)
-- Contros to update Song information 
local lblStartTime = root:findByName("lblStartTime", true)
local btnPlay = root:findByName("btnPlay", true)
local btnRec = root:findByName("btnRec", true)

local btnViewSes = root:findByName("btnViewSes", true)
local btnViewArr = root:findByName("btnViewArr", true)



local lblBars = root:findByName("lblBars", true)
local lblBeats = root:findByName("lblBeats", true)
local lblSixt = root:findByName("lblSixt", true)


local btnPunchIn = root:findByName("btnPunchIn", true)
local btnPunchOut = root:findByName("btnPunchOut", true)
local btnLoop = root:findByName("btnLoop", true)
local btnOverdub = root:findByName("btnOverdub", true)
local btnSessRec = root:findByName("btnSessRec", true)
local btnSesAutRec = root:findByName("btnSesAutRec", true)
local btnReAut = root:findByName("btnReAut", true)
local btnCaptMidi = root:findByName("btnCaptMidi", true)



local lblCrSgtime = root:findByName("lblCrSgtime", true)

local last= 99
local running=false 

 -- Task Schedule 
local delay = {a=3000,b=6100} -- every 1000ms = 1s
local last = {a=0,b=0}


function init()

 print("Ableton OSC ver 0.1")
 
end


    
function onReceiveOSC(message, connections)
  local path = message[1]
  local arguments = message[2]
  
  
  -- If Ableton live running start OSC listener 
  if ( path=="/live/test" and arguments[1].value=="ok" and running==false) then
    --sendOSC("/live/song/start_listen/start_time")
    --sendOSC("/live/song/start_listen/is_playing")
    --sendOSC("/live/song/start_listen/current_song_time")
    --sendOSC("/live/song/start_listen/record_mode")
    --sendOSC("/live/song/start_listen/punch_in")
    --sendOSC("/live/song/start_listen/punch_out")
    --sendOSC("/live/song/start_listen/loop")
    --sendOSC("/live/song/start_listen/arrangement_overdub")
    --sendOSC("/live/song/start_listen/session_record")
    --sendOSC("/live/song/start_listen/session_automation_record")
    --sendOSC("/live/song/start_listen/re_enable_automation_enabled")
    --sendOSC("/live/song/start_listen/can_capture_midi")
    
    end
  
  
  if ( path=="/live/test" and arguments[1].value=="ok") then
    lblLive.values.text="OK"
    running=true
    last.b=getMillis()
   end
   
  
  
  
  -- Get version   
  if ( path=="/live/application/get/version_string") then
      lblVer.values.text=arguments[1].value
    end
  -- Get average process  
  if ( path=="/live/application/get/average_process_usage" and arguments[1].value ~=nil ) then
      lblAve.values.text=arguments[1].value
    end
  
  if ( path=="/live/application/view/get/is_view_session") then
      btnViewSes.values.x=arguments[1].value
    end
  
  if ( path=="/live/application/view/get/is_view_arranger") then
      btnViewArr.values.x=arguments[1].value
    end
  
  
  
  -- Listener Song parameter start_time
  if ( path=="/live/song/get/start_time") then
      -- Send value to object  
       lblStartTime:notify("start_time",arguments[1].value)
       btnPlay:notify("start_time",arguments[1].value)
  end
   
  
   -- Is playing
  if ( path=="/live/song/get/is_playing" and arguments[1].value == true) then
      --print ('send notify'..tostring(arguments[1].value))
      btnPlay:notify("start_play",tonumber(arguments[1].value))
      
      -- The listener record doesn't work..
      --sendOSC('/live/song/get/session_record_status')
      
  end
   -- Is playing (update status )
  if ( path=="/live/song/get/is_playing" and arguments[1].value == false) then
      --print ('send notify'..tostring(arguments[1].value))
      btnPlay:notify("stop_play",tonumber(arguments[1].value))
      btnRec:notify("stop_play",tonumber(arguments[1].value))
  end
  
  
  
   -- Is recording (update status )
  if ( path=="/live/song/get/record_mode" and arguments[1].value == true) then
      --print ('send notify'..tostring(arguments[1].value))
      btnRec:notify("rec_start",tonumber(arguments[1].value))
  end
  
  -- Is recording (update status )
  if ( path=="/live/song/get/record_mode" and arguments[1].value == false) then
      --print ('send notify'..tostring(arguments[1].value))
      btnRec:notify("rec_stop",tonumber(arguments[1].value))
  end
  
  
  if ( path=="/live/song/get/current_song_time" ) then
     --playing=0
     --lblCrSgtime.values.text=tostring(arguments[1].value)
     lblCrSgtime:notify('time',arguments[1].value)
     sendOSC('/live/song/get_current_beats_song_time')  
  end
  
  
  if ( path=="/live/song/get_current_beats_song_time" ) then
     lblBars:notify('bars',arguments[1].value)
     lblBeats:notify('beats',arguments[2].value)
     lblSixt:notify('sixt',arguments[3].value)
       
  end
  
  
  if ( path=="/live/song/get/punch_in" ) then
     btnPunchIn:notify('PunchIn',arguments[1].value)
           
  end
  
  if ( path=="/live/song/get/punch_out" ) then
     btnPunchOut:notify('PunchOut',arguments[1].value)
  end
  
  if ( path=="/live/song/get/loop" ) then
     btnLoop:notify('Loop',arguments[1].value)
  end
  
  if ( path=="/live/song/get/arrangement_overdub" ) then
     btnOverdub:notify('Overdub',arguments[1].value)
  end
  
  if ( path=="/live/song/get/session_record" ) then
     btnSessRec:notify('SessRec',arguments[1].value)
  end
  
   if ( path=="/live/song/get/session_automation_record" ) then
     btnSesAutRec:notify('SesAutRec',arguments[1].value)
  end
  
   if ( path=="/live/song/get/re_enable_automation_enabled" ) then
     btnReAut:notify('ReAut',arguments[1].value)
  end
  
  if ( path=="/live/song/get/can_capture_midi" ) then
     btnCaptMidi:notify('CanCapMidi',arguments[1].value)
  end
  

end


-- Task schedule 3000 ms
function update()
  local now = getMillis()
  if(now - last.a > delay.a) then
    last.a = now
     sendOSC("/live/test")
     sendOSC("/live/application/view/get/is_view_arranger")
     sendOSC("/live/application/view/get/is_view_session")
     
     --sendOSC("/live/application/get/version_string")
     --sendOSC("/live/application/get/average_process_usage")
   
    
  end
  if(now - last.b > delay.b) then
    last.b = now
     lblLive.values.text="---"
     running=false
  end
  
end