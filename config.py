"""
Конфигурация проектов и доступов
"""
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "1296668664"))
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Проекты системы
PROJECTS = {
    "filter_kg": {
        "name": "Filter.kg",
        "emoji": "💧",
        "amo_domain": "filter1kg.amocrm.ru",
        "amo_token": os.getenv("AMO_TOKEN_FILTER", ""),
        "pipeline_id": 10581262,
        "status_map": {
            83450574: "Неразобранное",
            83450786: "Неразобранное",
            83450578: "Физ лица",
            83450582: "Первый контакт",
            83450586: "Вышли на ЛПР",
            83450590: "Назначено демо",
            83450790: "Демо проведено",
            83832670: "Партнёры",
            83450798: "Деньги в кассе",
            83450802: "Принимают решение",
            83450806: "Мотивированный отказ",
            142: "Успешно реализовано",
            143: "Закрыто / не реализовано",
        },
        "won_statuses": [83450798, 142],
        "lost_statuses": [83450806, 143],
    },
    "a_farm": {
        "name": "А-Фарм",
        "emoji": "🏥",
        "amo_domain": os.getenv("AMO_DOMAIN_AFARM", "bariatriakg1.amocrm.ru"),
        "amo_token": os.getenv(
            "AMO_TOKEN_AFARM",
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImJkNzVkZjkzNDhhOTc3OGIxMWIwZmIzYTA1ZTU3ZTQyYTJmMWFjNTc3M2NlMmJjMmMyNDM2MzFkNzBjZGRmZjMxY2IzN2RmYWFmNDJhODZmIn0.eyJhdWQiOiJkOTQ0YTc3Yy02ZTU0LTQ4NDYtOTY0ZS1iYzBjZDMzZDlmN2EiLCJqdGkiOiJiZDc1ZGY5MzQ4YTk3NzhiMTFiMGZiM2EwNWU1N2U0MmEyZjFhYzU3NzNjZTJiYzJjMjQzNjMxZDcwY2RkZmYzMWNiMzdkZmFhZjQyYTg2ZiIsImlhdCI6MTc3MzgxNzkwNCwibmJmIjoxNzczODE3OTA0LCJleHAiOjE4MDY1Mzc2MDAsInN1YiI6IjEwMTk2NzE0IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMxMzQzMDU4LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiZGJkOTQ4NjctNTlkNS00YTUwLTk3YjItODZiZTE0ZWI3ZDE1IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.jHh0eETtPtIHU84DENfG9Y5oXS8LvJC_2tZsRo__spRsK65SGDtsYHgjPZ-vt89GdkWuCqH24Z5xBKuT6bBFnDV6ftWJz4MM2IwCaCR6gh7PeBFbAmDQBnwxN4w_z-v6uWIr7MrpDABduCEyALVglMCwh4R2LVjPUiL6bVL2zIGpfSKOJ_ks47i6YBIoghxiuXuLnz0XOJK6LAXr13vzrOIslu_ec0BQ06-skXdYd5AZT9EoAM79pMIDlarS_m7PGMP2bJaEC14NZMEq3smNk_EFK9u2Op_zcEKg1olfnuINeFKyTqykwjt9rVR0XYxIl1-aruxy2cd3I7k8bNwDRQ"
        ),
        "pipeline_id": 10599806,
        "status_map": {
            83582914: "Неразобранное",
            83582918: "Первичный контакт",
            83584950: "Гос. клиники",
            83584954: "Частные клиники",
            83584958: "Сформированный запрос",
            83584962: "На перспективу",
            83584966: "Сформировано КП",
            83582922: "Переговоры",
            83582926: "Принимают решение",
            83584970: "Готовим контракт",
            84101454: "Смежное",
            83627518: "Нецелевой",
            142: "Успешно реализовано",
            143: "Закрыто / не реализовано",
        },
        "won_statuses": [142],
        "lost_statuses": [143, 83627518],
    },
    "dkauto": {
        "name": "DKAuto",
        "emoji": "🚗",
        "amo_domain": os.getenv("AMO_DOMAIN_DKAUTO", ""),
        "amo_token": os.getenv("AMO_TOKEN_DKAUTO", ""),
        "pipeline_id": None,
        "status_map": {},
        "won_statuses": [],
        "lost_statuses": [],
    },
    "logistics": {
        "name": "Логистика",
        "emoji": "🚚",
        "amo_domain": os.getenv("AMO_DOMAIN_LOGISTICS", ""),
        "amo_token": os.getenv("AMO_TOKEN_LOGISTICS", ""),
        "pipeline_id": None,
        "status_map": {},
        "won_statuses": [],
        "lost_statuses": [],
    },
}

REPORT_HOUR = 9   # час ежедневного отчёта (UTC+6 Бишкек = UTC+0 + 6)
REPORT_HOUR_UTC = 3  # 9:00 Бишкек = 03:00 UTC
