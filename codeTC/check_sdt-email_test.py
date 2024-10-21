from functions.check_sdt_email import check_email, check_sdt
import pytest

def test_email_hop_le():
    assert check_email('nguoidung@gmail.com')
    assert check_email('test123@gmail.com')
    assert check_email('email.test@gmail.com')

def test_email_khong_hop_le():
    assert not check_email('nguoidung@yahoo.com')
    assert not check_email('nguoidung@gmail.net')
    assert not check_email('nguoidung@gmailcom')
    assert not check_email('nguoidung@outlook.com')
    assert not check_email('nguoidung@')
    assert check_email('@gmail.com')
    assert not check_email('')

def test_email_case_insensitive():
    assert check_email('nguoidung@GMAIL.COM') == False
    assert check_email('nguoidung@Gmail.Com') == False

def test_sdt_hop_le():
    assert check_sdt('0123456789') == True
    assert check_sdt('0987654321') == True
    assert check_sdt('0912345678') == True

def test_sdt_khong_hop_le_do_do_dai():
    assert check_sdt('012345678') == False  
    assert check_sdt('01234567890') == False 
    assert not check_sdt('') 

def test_sdt_khong_hop_le_do_ky_tu():
    assert check_sdt('01234abcde') == False  
    assert check_sdt('phone1234') == False   
    assert check_sdt('09876 54321') == False 
    assert check_sdt('09876-54321') == False 
