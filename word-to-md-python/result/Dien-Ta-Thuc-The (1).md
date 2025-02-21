<p>1. Xác định các thuộc tính cho việc hình thành thực thể và diễn tả các quy<br />
tắc mô tả, ràng buộc về bản số :</p>
<ol>
<li>Xác định các thực thể của bài toán lưu trữ :</li>
</ol>
<ul>
<li>CUSTOMER(Khách hàng)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>cus_id(Mã khách hàng): Thuộc tính khoá</li>
<li>fullname(Tên khách hàng)</li>
<li>gender(Giới tính khách hàng:Nam/Nữ)</li>
<li>phone(Số điện thoại khách hàng)</li>
<li>addr( Địa chỉ của khách hàng)</li>
<li>PET(Thú cưng)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>pet_id(Mã thú cưng): Thuộc tính khoá</li>
<li>pet_name(Tên thú cưng)</li>
<li>pet_age(Tuổi thú cưng)</li>
<li>pet_weight(Cân nặng của thú cưng)</li>
<li>PET_CATEGORY(Loại thú cưng)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>petc_id(Mã loại thú cưng): Thuộc tính khoá</li>
<li>petc_name(Tên loạii: Mèo/chó/chim/chuột/sóc)</li>
<li>PET_PRODUCT(Sản phẩm)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>prod_id(Mã sản phẩm): Thuộc tính khoá</li>
<li>prod_name(Tên sản phẩm)</li>
<li>price(Giá)</li>
<li>discount(GIảm giá)</li>
<li>PET_PRODUCT_DETAIL(Chi tiết sản phẩm)</li>
</ul>
<p>Các thuộc tính</p>
<ul>
<li>ppd_id (Mã chi tiết sản phẩm): Thuộc tính khoá</li>
<li>c_name(Loại sản phẩm: Thức ăn cho Chó/Thức ăn cho Mèo/ Sữa/Thuốc/Thực phẩm chức năng)</li>
<li>brand (Tên nhãn hiệu)</li>
<li>company(Công ty sản xuất)</li>
<li>origin(Nơi sản xuất)</li>
<li>mfg_date(Ngày sản xuất)</li>
<li>ex_date(Ngày hết hạn)</li>
<li>qoh (Số lượng hàng trong kho)</li>
<li>ORDER_P(Đơn hàng)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>ord_id(Mã đơn hàng): Thuộc tính khoá</li>
<li>ord_date(Ngày mua hàng)</li>
<li>ed_date(Ngày nhận hàng)</li>
<li>ord_stt(Trạng thái đơn hàng: Đang giao/Đã nhận)</li>
<li>ORDER_DETAIL(Chi tiết đơn hàng)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>ord_dt_id(Mã chi tiết đơn hàng): Thuộc tính khoá</li>
<li>quantity(Số lượng)</li>
<li>unit(Đơn vị)</li>
<li>quantity_p(Giá/đơn vị)</li>
<li>PAYMENT (Thanh toán)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>pm_id (Mã thanh toán): Thuộc tính khóa</li>
<li>amount_paid (Lượng tiền thanh toán)</li>
<li>pm_method (Hình thức thanh toán: Tiền mặt/ VISA/MASTERCARD/ Ví MOMO)</li>
<li>pm_stt (Tình trạng thanh toán: Hoàn thành/ Chưa thanh toán)</li>
<li>SERVICE (Dịch vụ)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>serv_id (Mã dịch vụ): Thuộc tính khóa</li>
<li>serv_name (Tên dịch vụ)</li>
<li>serv_detail (Chi tiết dịch vụ)</li>
<li>serv_fee (Chi phí dịch vụ)</li>
<li>APPOINTMENT (Lịch hẹn)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>appt_id (Mã lịch hẹn) : thuộc tính khóa</li>
<li>date_appt (Ngày diễn ra cuộc hẹn)</li>
<li>time_appt (Thời gian diễn ra cuộc hẹn)</li>
<li>STAFF (Nhân viên)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>stf_id (Mã nhân viên): thuộc tính khóa</li>
<li>fname (Tên nhân viên)</li>
<li>midname (Tên lót nhân viên)</li>
<li>lname (Họ nhân viên)</li>
<li>gender (Giới tính nhân viên: Nam/ Nữ)</li>
<li>phone (Số điện thoại nhân viên)</li>
<li>addr (Địa chỉ của nhân viên)</li>
<li>salary (Lương nhân viên)</li>
<li>position (Chức vụ nhân viên)</li>
<li>APPOINTMENT_DETAIL (Chi tiết lịch hẹn)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>appt_details_id (Mã chi tiết cuộc hẹn): thuộc tính khóa</li>
<li>demand (Yêu cầu của khách hàng)</li>
<li>discount (Ưu đãi của cửa hàng thú cưng)</li>
<li>stt (Trạng thái của cuộc hẹn: Đã thực hiện/ Chưa thực hiện)</li>
<li>FEEDBACK(Phản hồi, ý kiến)</li>
</ul>
<p>Các thuộc tính:</p>
<ul>
<li>fb_id (Mã lời phản hồi): thuộc tính khóa</li>
<li>fb_title (Tiêu đề lời phản hồi)</li>
<li>fb_detail (Nội dung phản hồi)</li>
<li>date_fb (Ngày viết phản hồi)</li>
</ul>
