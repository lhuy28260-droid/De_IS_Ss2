
def process_rikkeimart_order(item_status, customer_response):
    """
    Mô phỏng luồng xử lý đơn hàng RikkeiMart.

    item_status:
        - "available"
        - "out_of_stock"

    customer_response:
        - "yes"
        - "no"
        - "timeout"
    """

    try:
        # Trường hợp sản phẩm còn hàng
        if item_status == "available":
            return "Sản phẩm còn hàng. Tiếp tục xử lý đơn hàng."

        # Trường hợp sản phẩm hết hàng
        if item_status == "out_of_stock":
            print("Sản phẩm hết hàng.")
            print("Tài xế đề xuất sản phẩm thay thế.")
            print("Hệ thống gửi thông báo đến khách hàng.")

            # Khách hàng đồng ý
            if customer_response == "yes":
                return "Khách hàng đồng ý. Thay thế sản phẩm và tiếp tục đơn hàng."

            # Khách hàng từ chối
            if customer_response == "no":
                return "Khách hàng từ chối. Hủy sản phẩm/đơn theo chính sách."

            # Khách hàng không phản hồi trong 3 phút
            if customer_response == "timeout":
                return "Timeout 3 phút. Auto-cancel đơn an toàn để giải phóng tài xế."

            return "Phản hồi khách hàng không hợp lệ."

        return "Trạng thái sản phẩm không hợp lệ."

    except Exception as error:
        # Đảm bảo chương trình không bị crash khi có lỗi bất ngờ
        return f"Lỗi được xử lý an toàn: {error}"


# ===== Mô phỏng các trường hợp =====

print(process_rikkeimart_order("available", None))

print(process_rikkeimart_order("out_of_stock", "yes"))

print(process_rikkeimart_order("out_of_stock", "no"))

print(process_rikkeimart_order("out_of_stock", "timeout"))

