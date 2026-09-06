
BASE_PAYOUT = 20_000
BONUS_THRESHOLD = 50
BONUS_RATE = 0.10


def calculate_driver_payout(transactions):
    """
    Tính thù lao tuần cho từng tài xế.

    Quy tắc:
    - DELIVERED: 20.000đ / đơn
    - > 50 đơn DELIVERED: thưởng thêm 10%
    - DISPUTED: tạm giữ, không tính vào payout
    """

    result = {}

    for transaction in transactions:
        driver_id = transaction.get("driver_id")
        order_id = transaction.get("order_id")
        status = transaction.get("status")

        # Kiểm tra dữ liệu cơ bản
        if not driver_id or not order_id:
            continue

        # Khởi tạo thông tin tài xế
        if driver_id not in result:
            result[driver_id] = {
                "delivered_orders": 0,
                "base_payout": 0,
                "bonus": 0,
                "total_payout": 0,
                "disputed_orders": [],
                "held_amount": 0
            }

        driver = result[driver_id]

        # Đơn giao thành công
        if status == "DELIVERED":
            driver["delivered_orders"] += 1
            driver["base_payout"] += BASE_PAYOUT

        # Đơn đang tranh chấp
        elif status == "DISPUTED":
            driver["disputed_orders"].append(order_id)
            driver["held_amount"] += BASE_PAYOUT

        # Trạng thái không hợp lệ
        else:
            continue

    # Tính thưởng sau khi đã tổng hợp toàn bộ giao dịch
    for driver in result.values():

        if driver["delivered_orders"] > BONUS_THRESHOLD:
            driver["bonus"] = int(
                driver["base_payout"] * BONUS_RATE
            )

        driver["total_payout"] = (
            driver["base_payout"] + driver["bonus"]
        )

    return result


# =========================
# DỮ LIỆU TPS MÔ PHỎNG
# =========================

transactions = [
    {"driver_id": "D01", "order_id": "O001", "status": "DELIVERED"},
    {"driver_id": "D01", "order_id": "O002", "status": "DELIVERED"},
    {"driver_id": "D01", "order_id": "O003", "status": "DISPUTED"},
    {"driver_id": "D01", "order_id": "O004", "status": "DELIVERED"},

    {"driver_id": "D02", "order_id": "O005", "status": "DELIVERED"},
    {"driver_id": "D02", "order_id": "O006", "status": "DELIVERED"},
]


# =========================
# TÍNH THÙ LAO
# =========================

payout_report = calculate_driver_payout(transactions)


# =========================
# HIỂN THỊ MIS REPORT
# =========================

for driver_id, data in payout_report.items():
    print(f"\nTài xế: {driver_id}")
    print(f"Số đơn DELIVERED: {data['delivered_orders']}")
    print(f"Thù lao cơ bản: {data['base_payout']:,}đ")
    print(f"Thưởng: {data['bonus']:,}đ")
    print(f"Tổng thù lao được trả: {data['total_payout']:,}đ")
    print(f"Đơn đang tranh chấp: {data['disputed_orders']}")
    print(f"Tiền đang tạm giữ: {data['held_amount']:,}đ")

