#!/usr/bin/haserl
<%
ipaddr=$(printenv | grep HTTP_HOST | cut -d= -f2 | cut -d: -f1)
button() {
  id=$(echo "${2// /-}" | tr '[:upper:]' '[:lower:]' | tr -cd '[:alnum:]-' )
  echo "<img id=\"${id}\" src=\"/img/${1}\" alt=\"${2}\" title=\"${2}\">"
}
%>
<div class="alert alert-danger">Motors not initialized.</div>
<div class="control-board">
<div class="control">
<% button "arrow-ul.svg" "Pan up left" %>
<% button "arrow-uc.svg" "Pan up" %>
<% button "arrow-ur.svg" "Pan up right" %>
<% button "arrow-cl.svg" "Pan left" %>
<% button "arrow-cr.svg" "Pan right" %>
<% button "arrow-dl.svg" "Pan down left" %>
<% button "arrow-dc.svg" "Pan down" %>
<% button "arrow-dr.svg" "Pan down right" %>
<% button "speed-slow.svg" "Speed" %>
<% button "zoom-close.svg" "Zoom in" %>
<% button "zoom-far.svg" "Zoom out" %>
<% [ "true" = "$(yaml-cli -g .nightMode.enabled)" ] && button "light-off.svg" "Night mode" %>
<% button "focus-plus.svg" "Focus: plus" %>
<% button "focus-auto.svg" "Focus: auto" %>
<% button "focus-minus.svg" "Focus: minus" %>
<% button "preset-home.svg" "Preset: Home" %>
<% button "preset-save.svg" "Preset: Save" %>
<% button "preset-1.svg" "Preset 1" %>
<% button "preset-2.svg" "Preset 2" %>
<% button "preset-3.svg" "Preset 3" %>
<% button "preset-4.svg" "Preset 4" %>
<% button "preset-5.svg" "Preset 5" %>
<% button "preset-6.svg" "Preset 6" %>
<% button "preset-7.svg" "Preset 7" %>
<% button "preset-8.svg" "Preset 8" %>
<% button "preset-9.svg" "Preset 9" %>
</div>
</div>

<script>
function reqListener() {
  console.log(this.responseText);
}

function sendToApi(endpoint) {
  const xhr = new XMLHttpRequest();
  xhr.addEventListener("load", reqListener);
  xhr.open("GET", "http://<%= $ipaddr %>/" + endpoint);
  xhr.send();
}

function initControls() {
  $$('a[id^=pan-],a[id^=zoom-]').forEach(el => {
    el.style.backgroundColor = 'red';
    el.addEventListener('click', event => {
      event.preventDefault();
      alert('Sorry, this feature does not work, yet!');
    });
  });

  if ($('#night-mode')) $('#night-mode').addEventListener('click', event => {
    event.preventDefault();
    event.target.src = (event.target.src.split('/').pop() == 'light-on.svg') ? '/img/light-off.svg' : '/img/light-on.svg';
    sendToApi('/night/toggle');
  });

  if ($('#speed')) $('#speed').addEventListener('click', event => {
    event.preventDefault();
    event.target.src = (event.target.src.split('/').pop() == 'speed-slow.svg') ? '/img/speed-fast.svg' : '/img/speed-slow.svg';
    // sendToApi('/speed/toggle');
  });
}

window.addEventListener('load', initControls);
</script>