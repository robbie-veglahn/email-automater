import email_automator

def test_email_send():
    assert email_automator.send_email(["robbie.veglahn@gmail.com"], "TEST", "HI ROBBIE, THIS IS A TEST!!!")

def test_email_send_mult_recip():
    assert email_automator.send_email(["robbie.veglahn@gmail.com", "sugrue122@gmail.com"], "TEST", "HI ROBBIE AND LEAH, THIS IS A TEST FOR MULTIPLE RECIPIENTS!!!")



