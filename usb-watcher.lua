--- USB Watcher for auto audio note transciption

local function watchForUSBChanges(data)
  if data["eventType"] == "added" then
    hs.notify.show("Auto Audio Note", "You just connected", data["productName"])
    if data["productName"] == "Wireless Microphone TX" then
      hs.execute("~/Documents/side_projects/auto-audio-note/run.sh", true)
    end
  end
end

local USBWatcher = nil
USBWatcher = hs.usb.watcher.new(watchForUSBChanges)
USBWatcher:start()

