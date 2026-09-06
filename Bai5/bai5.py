def process_rikkeimart_order(item_status, customer_response):
    """
    Mô phỏng luồng xử lý đơn hàng RikkeiMart.

    item_status:
        "available"     : sản phẩm còn hàng
        "out_of_stock"  : sản phẩm hết hàng

    customer_response:
        "yes"            : khách đồng ý thay thế
        "no"             : khách từ chối
        "timeout"        : khách không phản hồi trong 3 phút
        None              : không áp dụng khi sản phẩm còn hàng
    """
    try:
        if item_status == "available":
            return "Sản phẩm còn hàng -> tiếp tục xử lý đơn hàng."

        if item_status != "out_of_stock":
            return "Trạng thái sản phẩm không hợp lệ."

        print("Sản phẩm hết hàng.")
        print("Tài xế chọn: Đề xuất sản phẩm thay thế tương đương.")
        print("Hệ thống gửi thông báo xác nhận đến khách hàng.")

        if customer_response == "yes":
            return "Khách hàng đồng ý -> thay thế sản phẩm và tiếp tục đơn hàng."

        if customer_response == "no":
            return "Khách hàng từ chối -> xử lý hủy sản phẩm/đơn theo chính sách."

        if customer_response == "timeout":
            return "Timeout 3 phút -> Auto-cancel an toàn để giải phóng tài xế."

        return "Phản hồi khách hàng không hợp lệ."

    except Exception as error:
        return f"Lỗi được xử lý an toàn: {error}"


if __name__ == "__main__":
    test_cases = [
        ("available", None),
        ("out_of_stock", "yes"),
        ("out_of_stock", "no"),
        ("out_of_stock", "timeout"),
    ]

    for item_status, customer_response in test_cases:
        print("-" * 70)
        print(process_rikkeimart_order(item_status, customer_response))
