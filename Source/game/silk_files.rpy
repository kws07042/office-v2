# 저장·불러오기: 장면 썸네일이 보이는 3×2 카드, 쪽 넘김, 자동·퀵 저장 칸.
# 1쪽의 칸 이름은 예전과 같은 "1"~"6"이라 이전 저장도 그대로 보인다.

define config.thumbnail_width = 384
define config.thumbnail_height = 216
define SILK_FILE_PAGES = 6
define SILK_FILE_COLS = 3
define SILK_FILE_ROWS = 2

init 8 python:
    def silk_save_name():
        # 저장 칸에 보일 한 줄: '장 제목 · 장소'
        st = renpy.store
        chapter = getattr(st, "chapter", "") or ""
        place = (getattr(st, "location", "") or "").rpartition("·")[2].strip()
        st.save_name = " · ".join(x for x in (chapter, place) if x)

    config.start_interact_callbacks.append(silk_save_name)

transform silk_slot_in(i=0):
    on show:
        alpha 0.0 yoffset 10
        pause (0.04 * i)
        easein 0.24 alpha 1.0 yoffset 0

style silk_slot_button is button:
    background silk_surface("card")
    hover_background silk_surface("card_on")
    insensitive_background silk_surface("quiet")
    padding (11, 11, 13, 15)
    xysize (292, 230)
style silk_page_button is silk_small_button:
    selected_background silk_surface("selected")
    xminimum 46
style silk_page_button_text is silk_small_button_text:
    selected_color "#FFFDFB"
    xalign 0.5

screen file_slots(mode):
    $ page = FileCurrentPage()
    if (page in ("auto", "quick") and mode == "save") or (page not in ("auto", "quick") and not (page.isdigit() and 1 <= int(page) <= SILK_FILE_PAGES)):
        $ page = "1"
    add "silk ground"
    frame:
        at (silk_menu_panel if silk_motion_on() else silk_still)
        xalign 0.5 yalign 0.5 xsize 1010 ysize 660 padding (36, 26, 40, 30)
        background silk_surface("panel")
        vbox:
            spacing 12
            hbox:
                spacing 18
                use silk_menu_title(("저장" if mode == "save" else "불러오기"), ("Save" if mode == "save" else "Load"))
                text ("저장할 칸을 고르세요. 선택과 기억이 함께 저장됩니다." if mode == "save" else "이어서 읽을 장면을 고르세요.") size 17 color "#6E4553" yalign 0.75
            hbox:
                spacing 6
                for p in range(1, SILK_FILE_PAGES + 1):
                    textbutton str(p) action FilePage(str(p)) selected (page == str(p)) style "silk_page_button" id ("file_page_%d" % p)
                null width 14
                if mode == "load":
                    textbutton "자동" action FilePage("auto") selected (page == "auto") style "silk_page_button" id "file_page_auto"
                    textbutton "퀵" action FilePage("quick") selected (page == "quick") style "silk_page_button" id "file_page_quick"
            grid SILK_FILE_COLS SILK_FILE_ROWS:
                spacing 14
                for i in range(1, SILK_FILE_COLS * SILK_FILE_ROWS + 1):
                    $ slot = str(i)
                    $ pg = page
                    $ filled = FileLoadable(slot, page=pg)
                    button:
                        at (silk_slot_in(i) if silk_motion_on() else silk_still)
                        style "silk_slot_button"
                        id ("file_slot_%s_%s" % (pg, slot))
                        action (FileSave(slot, confirm=True, page=pg) if mode == "save" else FileLoad(slot, confirm=True, page=pg))
                        sensitive (mode == "save" or filled)
                        alt ("%s쪽 %s칸" % (pg, slot))
                        vbox:
                            spacing 6
                            fixed:
                                xysize (270, 152)
                                add Solid("#E7DFD8")
                                if filled:
                                    add FileScreenshot(slot, page=pg) xysize (270, 152) fit "contain" xalign 0.5 yalign 0.5
                                else:
                                    text "비어 있음" size 17 color "#A3959B" xalign 0.5 yalign 0.5
                            hbox:
                                spacing 8
                                text (("자동 " if page == "auto" else ("퀵 " if page == "quick" else "")) + slot) font "fonts/Jua-Regular.ttf" size 18 color "#B3123F"
                                text FileTime(slot, page=pg, format="%m월 %d일 %H:%M", empty="") size 14 color "#6E4553" yalign 0.8
                            $ save_line = FileSaveName(slot, empty="", page=pg)
                            text (save_line if len(save_line) <= 24 else save_line[:23] + "…") size 14 color "#3B0B22" xmaximum 270
        hbox:
            yalign 1.0 xalign 1.0 spacing 10
            textbutton "돌아가기" action Return() style "silk_small_button"
