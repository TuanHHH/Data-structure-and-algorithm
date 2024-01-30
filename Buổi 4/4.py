def is_anagram(a,b):
    # Nếu chiều dài khác nhau kết quả sẽ trả về false
    if len(a) != len(b):
        return False
    else:
        # Tạo ra 1 set với các giá trị đặc trưng không trùng lặp
        character_in_a = set(a)
        character_in_b = set(b)
        # Nếu 2 set của 2 string trên khác nhau sẽ trả về kết quả False
        if character_in_a != character_in_b:
            return False
        else:
            # Nếu 2 set của 2 string trên giống nhau thì kiểm tra tiếp số kí tự riêng của 2 hàm trên
            for char in character_in_a:
                # Nếu có 1 kí tên của 1 bên khác với bên còn lại sẽ trả về False
                if a.count(char) != b.count(char):
                    return False  
            # Nếu giống hết thì trả về giá trị về True
            return True
        
print(is_anagram('gramabaa','mrgaaaab'))