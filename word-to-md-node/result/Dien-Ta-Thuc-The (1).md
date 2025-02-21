1\. Xác định các thuộc tính cho việc hình thành thực thể và diễn tả các quy tắc mô tả, ràng buộc về bản số :

1.  Xác định các thực thể của bài toán lưu trữ :

*   CUSTOMER(Khách hàng)

Các thuộc tính:

*   cus\_id(Mã khách hàng): Thuộc tính khoá
*   fullname(Tên khách hàng)
*   gender(Giới tính khách hàng:Nam/Nữ)
*   phone(Số điện thoại khách hàng)
*   addr( Địa chỉ của khách hàng)
*   PET(Thú cưng)

Các thuộc tính:

*   pet\_id(Mã thú cưng): Thuộc tính khoá
*   pet\_name(Tên thú cưng)
*   pet\_age(Tuổi thú cưng)
*   pet\_weight(Cân nặng của thú cưng)
*   PET\_CATEGORY(Loại thú cưng)

Các thuộc tính:

*   petc\_id(Mã loại thú cưng): Thuộc tính khoá
*   petc\_name(Tên loạii: Mèo/chó/chim/chuột/sóc)
*   PET\_PRODUCT(Sản phẩm)

Các thuộc tính:

*   prod\_id(Mã sản phẩm): Thuộc tính khoá
*   prod\_name(Tên sản phẩm)
*   price(Giá)
*   discount(GIảm giá)
*   PET\_PRODUCT\_DETAIL(Chi tiết sản phẩm)

Các thuộc tính

*   ppd\_id (Mã chi tiết sản phẩm): Thuộc tính khoá
*   c\_name(Loại sản phẩm: Thức ăn cho Chó/Thức ăn cho Mèo/ Sữa/Thuốc/Thực phẩm chức năng)
*   brand (Tên nhãn hiệu)
*   company(Công ty sản xuất)
*   origin(Nơi sản xuất)
*   mfg\_date(Ngày sản xuất)
*   ex\_date(Ngày hết hạn)
*   qoh (Số lượng hàng trong kho)
*   ORDER\_P(Đơn hàng)

Các thuộc tính:

*   ord\_id(Mã đơn hàng): Thuộc tính khoá
*   ord\_date(Ngày mua hàng)
*   ed\_date(Ngày nhận hàng)
*   ord\_stt(Trạng thái đơn hàng: Đang giao/Đã nhận)
*   ORDER\_DETAIL(Chi tiết đơn hàng)

Các thuộc tính:

*   ord\_dt\_id(Mã chi tiết đơn hàng): Thuộc tính khoá
*   quantity(Số lượng)
*   unit(Đơn vị)
*   quantity\_p(Giá/đơn vị)
*   PAYMENT (Thanh toán)

Các thuộc tính:

*   pm\_id (Mã thanh toán): Thuộc tính khóa
*   amount\_paid (Lượng tiền thanh toán)
*   pm\_method (Hình thức thanh toán: Tiền mặt/ VISA/MASTERCARD/ Ví MOMO)
*   pm\_stt (Tình trạng thanh toán: Hoàn thành/ Chưa thanh toán)
*   SERVICE (Dịch vụ)

Các thuộc tính:

*   serv\_id (Mã dịch vụ): Thuộc tính khóa
*   serv\_name (Tên dịch vụ)
*   serv\_detail (Chi tiết dịch vụ)
*   serv\_fee (Chi phí dịch vụ)
*   APPOINTMENT (Lịch hẹn)

Các thuộc tính:

*   appt\_id (Mã lịch hẹn) : thuộc tính khóa
*   date\_appt (Ngày diễn ra cuộc hẹn)
*   time\_appt (Thời gian diễn ra cuộc hẹn)
*   STAFF (Nhân viên)

Các thuộc tính:

*   stf\_id (Mã nhân viên): thuộc tính khóa
*   fname (Tên nhân viên)
*   midname (Tên lót nhân viên)
*   lname (Họ nhân viên)
*   gender (Giới tính nhân viên: Nam/ Nữ)
*   phone (Số điện thoại nhân viên)
*   addr (Địa chỉ của nhân viên)
*   salary (Lương nhân viên)
*   position (Chức vụ nhân viên)
*   APPOINTMENT\_DETAIL (Chi tiết lịch hẹn)

Các thuộc tính:

*   appt\_details\_id (Mã chi tiết cuộc hẹn): thuộc tính khóa
*   demand (Yêu cầu của khách hàng)
*   discount (Ưu đãi của cửa hàng thú cưng)
*   stt (Trạng thái của cuộc hẹn: Đã thực hiện/ Chưa thực hiện)
*   FEEDBACK(Phản hồi, ý kiến)

Các thuộc tính:

*   fb\_id (Mã lời phản hồi): thuộc tính khóa
*   fb\_title (Tiêu đề lời phản hồi)
*   fb\_detail (Nội dung phản hồi)
*   date\_fb (Ngày viết phản hồi)