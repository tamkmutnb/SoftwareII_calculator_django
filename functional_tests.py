from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self):

        #uesr open browser and go to web_page
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        #He saw that there is 'Home_Page text in the browser title'

        self.assertIn('Home_Page', self.browser.title)

        #He saw that there is a 'Welcome Text'
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to web app calculator !', header_text)

        #He saw the enter first number label
        num1_label = self.browser.find_element_by_tag_name('label').text
        self.assertIn('Enter 1st number (this is X var) :', num1_label)

        # He saw the enter second number label:
        num2_label = self.browser.find_element_by_xpath("//label[@for='sec_num_label']").text
        self.assertIn('Enter 2st number (this is Y var) :', num2_label)

        # He saw the enter  op label:
        op_label = self.browser.find_element_by_xpath("//label[@for='op_label']").text
        self.assertIn('Enter Operator     (+, -, *, /) :       ', op_label)

        # He saw a 1st num box
        num1_box = self.browser.find_element_by_name("num1")
        self.assertEqual(
            num1_box.get_attribute('type'),
            'text'
        )
        # He saw a 1st num placeholder
        self.assertEqual(
            num1_box.get_attribute('placeholder'),
            'for X enter Number ONLY'
        )

        # He saw a 2nd num box
        num2_box = self.browser.find_element_by_name("num2")
        self.assertEqual(
            num1_box.get_attribute('type'),
            'text'
        )
        # He saw a 2nd num placeholder
        self.assertEqual(
            num2_box.get_attribute('placeholder'),
            'for Y enter Number ONLY'
        )

        # He saw a op box
        op_box = self.browser.find_element_by_name("operator")
        self.assertEqual(
            op_box.get_attribute('type'),
            'text'
        )
        # He saw a op placeholder
        self.assertEqual(
            op_box.get_attribute('placeholder'),
            "for operator ' +, -, *, / ' ONLY"
        )

        # He saw calculate button
        cal_btn = self.browser.find_element_by_name("Calculate_btn")
        self.assertEqual(
            cal_btn.get_attribute('type'),
            'submit'
        )

        # He saw the enter  op label:
        log_label = self.browser.find_element_by_xpath("//label[@for='log_label']").text
        self.assertIn('Log :', log_label)

        # He saw ClearALL button
        clr_btn = self.browser.find_element_by_name("Clear_btn")
        self.assertEqual(
            clr_btn.get_attribute('type'),
            'submit'
        )

        #he put 1st and 2nd number then click
        num1_box.send_keys(2)
        num2_box.send_keys(3)
        op_box.send_keys('+')
        cal_btn.click()
        #self.browser.get('http://localhost:8000')
        time.sleep(8)
        #he put the same numbers but change OP
        num1_box = self.browser.find_element_by_name("num1")
        num2_box = self.browser.find_element_by_name("num2")
        op_box = self.browser.find_element_by_name("operator")
        num1_box.send_keys(500)
        num2_box.send_keys(100)
        op_box.send_keys('-')
        cal_btn.click()



        num1_box = self.browser.find_element_by_name("num1")
        num2_box = self.browser.find_element_by_name("num2")
        op_box = self.browser.find_element_by_name("operator")
        num1_box.send_keys(2)
        num2_box.send_keys(3)
        op_box.send_keys('*')
        cal_btn.click()


        num1_box = self.browser.find_element_by_name("num1")
        num2_box = self.browser.find_element_by_name("num2")
        op_box = self.browser.find_element_by_name("operator")
        num1_box.send_keys(2)
        num2_box.send_keys(3)
        op_box.send_keys('/')
        cal_btn.click()
        time.sleep(50)





        #Check HomePage, Sign Up and Log in Link
        '''
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)
        '''
        '''
        #This is how to check welcome text
        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)
        '''
        #Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        #check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        #check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        #check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        #check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        #check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )

    def test_login_fail(self):
        #BASIC TEST
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
		# เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        # check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        # check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        # check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        # check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        #END BASIC TEST
        error_message = self.browser.find_element_by_tag_name('ul').text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.',
                      error_message)

        time.sleep(20)
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        error_message = self.browser.find_elements_by_xpath("//ul[@class='errorlist nonfield']").text
        self.assertIn('Please enter a correct username and password. Note that both fields may be case-sensitive.', error_message)

    def test_login_pass(self):
        #basic test
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        # check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        # check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        # check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        # check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        #end basic test

        # Check Type Username Pass RIGHT !
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        # username_box.send_keys('tamtong007')
        # password_box.send_keys('o87525o135')
        login_button.click()
        # Check Redirect !!!!!

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        logout_link = self.browser.find_element_by_link_text('Log out').text
        self.assertIn('Log out', logout_link)

        id_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('ID : jesselingard', id_text)

        '''Check Click Link
        homepage_click = self.browser.find_element_by_link_text('Home page')
        homepage_click.click()
        time.sleep(2)'''

        '''End of Checking Login'''

    def test_flow(self):
        # basic test
        self.browser.get('http://localhost:8000')
        '''Test Only Index'''
        # เขาสังเกตุว่าชื่อเว็บจะมีคำว่า grade guide
        # She notices the page title and header mention to-do lists
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        welcome_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Welcome to GradeGuide !', welcome_text)

        totaluser_text = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Total users registered:', totaluser_text)

        # Check User Loging in
        login_click = self.browser.find_element_by_link_text('Log in')
        login_click.click()

        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GradeGuide', header_text)

        # Check HomePage, Sign Up and Log in Link
        homepage_link = self.browser.find_element_by_link_text('Home page').text
        self.assertIn('Home page', homepage_link)

        signup_link = self.browser.find_element_by_link_text('Sign up').text
        self.assertIn('Sign up', signup_link)

        login_link = self.browser.find_element_by_link_text('Log in').text
        self.assertIn('Log in', login_link)

        login_h2 = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', login_h2)
        # check Label Username:
        username_label = self.browser.find_element_by_xpath("//label[@for='id_username']").text
        self.assertIn('Username:', username_label)
        # check Label Input Box
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(
            username_box.get_attribute('type'),
            'text'
        )
        # check Label Password:
        password_label = self.browser.find_element_by_xpath("//label[@for='id_password']").text
        self.assertIn('Password:', password_label)
        # check Label Input Pasword Box
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(
            password_box.get_attribute('type'),
            'password'
        )

        # check button
        login_button = self.browser.find_element_by_tag_name("button")
        self.assertEqual(
            login_button.get_attribute('type'),
            'submit'
        )
        # end basic test

        # log in
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        # username_box.send_keys('tamtong007')
        # password_box.send_keys('o87525o135')
        login_button.click()
        self.browser.get('http://localhost:8000/flow.html')

        self.assertIn('', self.browser.title)

        # test Flow H1 text
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Flow', header_text)

        # test input Search text
        subject_head = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('subject :', subject_head)

        # test search box
        subject_placeholder = self.browser.find_element_by_id("search_placeholder")
        self.assertEqual(
            subject_placeholder.get_attribute('type'),
            'text'
        )
        # test submit button
        submit_button = self.browser.find_element_by_id("submit_button")
        self.assertEqual(
            submit_button.get_attribute('type'),
            'submit'
        )

        # test fullflow button
        fullflow_button = self.browser.find_element_by_id("fullflow_button")
        self.assertEqual(
            fullflow_button.get_attribute('type'),
            'button'
        )

    def test_flow_pic(self):
        self.browser.get('http://localhost:8000/flow.html')

        flow_button = self.browser.find_element_by_id("fullflow_button")
        flow_button.click()

        flow_image = self.browser.find_element_by_id("image")
        self.assertEqual(
            flow_image.get_attribute('id'),
            'image'
        )
        time.sleep(20)

    def test_home(self):
        # เมื่อเขากดเข้าไปที่หน้า signup
        self.browser.get('http://localhost:8000/signup')

        username_box = self.browser.find_element_by_id("id_username")

        password_box = self.browser.find_element_by_id("id_password1")

        password_box2 = self.browser.find_element_by_id("id_password2")

        # เขาทำการสมัคร username jesselingard
        # password lingard123456789
        # password2 lingard123456789
        username_box.send_keys('jesselingard')
        password_box.send_keys('lingard123456789')
        password_box2.send_keys('lingard123456789')
        # เขาทำการกดปุ่ม signup
        signup_button = self.browser.find_element_by_tag_name("button")
        signup_button.click()
        time.sleep(2)
        # เขาเข้าไปที่หน้า login
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Log in', header_text)

        username_login_box = self.browser.find_element_by_id("id_username")

        password_login_box = self.browser.find_element_by_id("id_password")
        # เขาใส่ id password
        username_login_box.send_keys('jesselingard')
        password_login_box.send_keys('lingard123456789')
        # เขากดปุ่ม login
        login_button = self.browser.find_element_by_tag_name("button")
        login_button.click()
        time.sleep(2)
        # เขาเข้าไปที่หน้า homepage
        self.browser.get('http://127.0.0.1:8000/home')
        id_user = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('jesselingard', id_user)
        # เขาใส่ unit
        unit_text = self.browser.find_element_by_id('subject1Unitid')
        unit_text.send_keys('Unit: 1')
        # เขาใส่ Grade
        unit_text = self.browser.find_element_by_id('subject1Gradeid')
        unit_text.send_keys('Grade: 2.5&nbsp; (C+)')
        time.sleep(3)
        # เขาเห็นเกรดแสดงขึ้นมา
        submit_button = self.browser.find_element_by_id("submit")
        submit_button.click()
        time.sleep(3)
        submit_text = self.browser.find_element_by_id('gradeshow').text
        self.assertIn('2.5', submit_text)
        time.sleep(6)
        # เขาเห็นสาถานะนักศึกษาของเขา
        self.assertIn('Normal State', submit_text)

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
