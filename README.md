﻿# OsuMapFilter  
Filter existing maps  
過濾已有的圖  
效果:  
![](https://i.imgur.com/yjkvH6o.png)  

you need map list to make this script work  
if you from greasyfork, get python script on [my github](https://github.com/x94fujo6rpg/osuMapFilter)  

if you aren't open [https://osu.ppy.sh/beatmapsets](https://osu.ppy.sh/beatmapsets) directly  
F5 to run the script  

## update

- v0.5:
    - auto save & load old data
    - auto add map to list when download
      - also work at map page (https://osu.ppy.sh/beatmapsets/xxxxxxx)
      - but it won't sync to other tab. if you open the list page (https://osu.ppy.sh/beatmapsets), you need F5 to refresh the page so the script can re-load list data
    - read file will overwrite it
    - this is not 100%. if you have del some map or add new map in other way, re-run python script & load list data

- v0.4:
	- improve speed

- v0.3:
	- fix for new site ui

- v0.2: 
	- add stop button, fix some issue  
	- make map links open in new tab (prevent accidental clicks)  

## usage
require: [Python 3.8+](https://www.python.org/downloads/) / [Tampermonkey](https://www.tampermonkey.net/)  
* put `getmaplist.py` under osu path
```bash
osu
├──getmaplist.py
├──osu!.exe
...
```

default osu path:  
`C:\Users\<Username>\AppData\Local\osu!`  
`C:\Program Files\osu!`  
`C:\Program Files(x86)\osu!`  

* run `getmaplist.py`, this will generate `map_list.txt`
* install [osuMapFilter.js](https://greasyfork.org/scripts/409887)
* when you open https://osu.ppy.sh/beatmapsets
* load `map_list.txt`

then it will start filtering maps
  
## 中文說明:
需求: [Python 3.8+](https://www.python.org/downloads/) / [Tampermonkey](https://www.tampermonkey.net/)  
* 將 `getmaplist.py` 放到跟 `osu!.exe` 相同路徑下  
```bash
osu
├──getmaplist.py
├──osu!.exe
...
```
osu預設路徑:  
`C:\Users\<Username>\AppData\Local\osu!`  
`C:\Program Files\osu!`  
`C:\Program Files(x86)\osu!`  

* 執行 `getmaplist.py`，成功後會產生 `map_list.txt`
* 安裝 [osuMapFilter.js](https://greasyfork.org/scripts/409887)
* 打開 https://osu.ppy.sh/beatmapsets
* 檔案 > 選擇之前產生的 `map_list.txt`
檔案正確的話會開始過濾

