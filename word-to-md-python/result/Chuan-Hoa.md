**4\. Chuẩn hóa mô hình:**
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

* Xét **_quan hệ PAYMENT(pm_id,amount_paid,pm_method,pm_stt,cus_id)_** , ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D, E tương ứng. Khi đó, quan hệ PAYMENT và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D, E) F = {A→B, A→C, A→D, A→E}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính khác
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là pm_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

* Xét **_quan hệ SERVICE(serv_id,serv_name,serv_detail,serv_fee, cus_id)_** , ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D, E tương ứng. Khi đó, quan hệ SERVICE và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D, E) F = {A→B, A→C, A→D, A→E}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính khác
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là serv_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

* Xét **_quan hệ APPOINTMENT(appt_id, date_appt, time_appt, cus_id)_** , ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D tương ứng. Khi đó, quan hệ APPOINTMENT và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D) F = {A→B, A→C, A→D}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính khác
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là appt_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

* Xét **_quan hệ STAFF(stf_id, lname, midname, fname, gender, phone, addr, salary, position, manager_id)_** ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D, E, G, H, I, J, K tương ứng. Khi đó, quan hệ STAFF và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D, E, G, H, I, J, K) F = {A→B, A→C, A→D, A→E, A→G, A→H, A→I, A→J, A→K}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính khác
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là pm_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

* Xét **_quan hệ APPOINTMENT_DETAIL(appt_details_id, demand, discount, stt, appt_id, stf_id)_** ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D, E, G tương ứng. Khi đó, quan hệ APPOINTMENT_DETAIL và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D, E,G) F = {A→B, A→C, A→D, A→E, A→G}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính khác
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là pm_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

* Xét **_quan hệ STAFF_SER(stf_id, serv_id, date_serv, time_serv)_** ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D tương ứng. Khi đó, quan hệ STAFF_SER và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D, E,G) F = {AB→C, AB→D}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính khác
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là pm_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

* Xét **_quan hệ APPD_SERV(stf_id, serv_id, date_serv, time_serv)_** ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D tương ứng. Khi đó, quan hệ APPD_SERV và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D, E,G) F = {AB→C, AB→D}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính khác
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là pm_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

* Xét **_quan hệ FEEDBACK(fb_id, fb_title, fb_detail, date_fb, cus_id)_** , ký hiệu tên các thuộc tính của quan hệ trên lần lượt là A, B, C, D, E tương ứng. Khi đó, quan hệ FEEDBACK và tập phụ thuộc hàm F được viết gọn là: R(A, B, C, D, E) F = {A→B, A→C, A→D, A→E}.

Ta thấy, lược đồ quan hệ thỏa mãn các yêu cầu sau:

  * Các trường thuộc tính là nguyên tố, không chứa giá trị phức
  * Không chứa thuộc tính gây lặp
  * Không chứa thuộc tính có thể tính toán từ các thuộc tính kahsc
  * Các trường thuộc tính không phải là khóa chính, phụ thuộc hoàn toàn vào khóa chính là pm_id. Không phụ thuộc một phần hay phụ thuộc bắc cầu thông qua thuộc tính khác. 
  * Đây là lược đồ đạt chuẩn hóa dạng 3.

