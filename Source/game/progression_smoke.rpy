# Developer-only manual runtime regression. Not run in this environment.
label progression_smoke:
    if not config.developer:
        return
    $ progression_smoke_old_state = progression_state
    $ progression_smoke_old_affinity = affinity
    $ progression_smoke_old_memory = memory
    $ progression_state = pm.initial_state()
    $ affinity = {"ria": 50, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ memory = {"ria_core_understanding": True}
    $ progression_apply("smoke-choice", "ria", -5, 10)
    $ assert affinity["ria"] == 45
    $ assert progression_relation("ria") == 25
    $ progression_apply("smoke-choice", "ria", -5, 10)
    $ assert affinity["ria"] == 45
    "개발 검사: 호감도 45, 편안함 25인지 우리의 기록에서 확인하세요."
    "수동 저장 → 다른 선택 → 불러오기, 롤백 → 재선택을 각각 확인하세요."
    $ progression_state = progression_smoke_old_state
    $ affinity = progression_smoke_old_affinity
    $ memory = progression_smoke_old_memory
    return

