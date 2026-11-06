default ria_expression = "base"

init -5 python:
    RIA_MASTER_V2 = "images/characters/ria/ui_master_v2.png"
    RIA_FACE_ORIGIN = (340, 110)
    RIA_FACE_SIZE = (320, 320)
    RIA_PORTRAIT_CROP = (190, 40, 630, 850)
    RIA_PORTRAIT_ZOOM = 0.95

    def ria_expression_full(expression):
        # Only the small face mask can replace pixels. The master body is shared.
        if expression == "base":
            return renpy.displayable(RIA_MASTER_V2)
        return Composite(
            (993, 1584),
            (0, 0), RIA_MASTER_V2,
            RIA_FACE_ORIGIN, AlphaMask(
                Transform("images/characters/ria/expressions/%s.png" % expression, xysize=RIA_FACE_SIZE),
                "images/characters/ria/expressions/shy_features_mask.svg" if expression == "shy" else "images/characters/ria/expressions/features_mask.svg"))

    def ria_portrait_display(st, at):
        # Old production art was removed for recreation; dialogue remains usable.
        if not renpy.loadable(RIA_MASTER_V2):
            return Null(), None
        expression = renpy.store.ria_expression
        # Defaults also cover old saves; unfinished assets fall back to the master.
        if expression not in ("base", "smile", "shy", "serious") or (
                expression != "base" and not renpy.loadable("images/characters/ria/expressions/%s.png" % expression)):
            expression = "base"
        return Transform(Crop(RIA_PORTRAIT_CROP, ria_expression_full(expression)), zoom=RIA_PORTRAIT_ZOOM), None

label ria_expression_preview:
    $ cream_preview_active = False
    $ cream_focus = "ria"
    $ active_route = "ria"
    $ speech_informal = True
    $ chapter = "강리아 · 표정 비교"
    $ location = "초여름 · 퇴근길"
    $ ria_expression = "base"
    r "오늘 코스는 다시 써야겠네. 휴무인 식당, 골목, 이 카페."
    $ ria_expression = "smile"
    r "그러게! 지도한테 따질 수도 없고..."
    $ ria_expression = "shy"
    r "...좋아. 대신 네 얘기도 하나씩. 나만 취재당하는 건 싫어."
    $ ria_expression = "serious"
    r "나는 궁금한데. 어떤 걸 찍고 싶었는지."
    $ ria_expression = "base"
    menu:
        "R02 실제 대화로 확인":
            jump ria_r02_preview
        "표정 비교 다시 보기":
            jump ria_expression_preview
        "처음 화면으로":
            return

label ria_r02_preview:
    $ speech_informal = True
    jump ria_r02_preview_loop

label ria_r02_preview_loop:
    $ cream_preview_active = False
    $ cream_preview_mode = None
    $ cream_focus = "ria"
    $ active_route = "ria"
    $ dating = False
    $ afterwork_preference = "quiet"
    $ memory = {}
    $ completed = []
    $ affinity = {"ria":14, "jihyun":0, "yujin":0, "seoyun":0}
    call ria_r02
    menu:
        "표정 비교 보기":
            jump ria_expression_preview
        "존댓말 / 반말 전환해서 다시 보기":
            $ speech_informal = not speech_informal
            jump ria_r02_preview_loop
        "처음 화면으로":
            return
