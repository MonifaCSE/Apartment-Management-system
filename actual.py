from flask import Flask, render_template, request, redirect, flash, session
from werkzeug.utils import secure_filename

import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'static/upload/'

conn = mysql.connector.connect(host="localhost", user="root", password="", database="apartment management system")
cursor = conn.cursor()


@app.route('/')
def login():
    if 'user_id' in session:
        return redirect('/home')
    elif 'password' in session:
        return redirect('/ghome')
    else:
        return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')


@app.route('/apartment')
def apartment():
    if 'user_id' in session:
        s=session['user_id']
        cursor.execute("SELECT* FROM `apartment_details` WHERE Number_of_room = '" + str(s) + "'")
        myapartment = cursor.fetchall()
        return render_template('apartment.html', apartments=myapartment)
    else:
        return redirect('/')


@app.route('/tenant')
def tenant():
    if 'user_id' in session:
        cursor.execute("SELECT* FROM `tenant_details`")
        mytenant = cursor.fetchall()
        return render_template('tenant.html', tenant=mytenant)
    else:
        return redirect('/')


@app.route('/rent')
def rent():
    if 'user_id' in session:
        cursor.execute("SELECT* FROM `rent_info`")
        myrent = cursor.fetchall()
        return render_template('rent.html', rent=myrent)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


# ..................user route.................................


@app.route('/ghome')
def ghome():
    if 'password' in session:
        return render_template('ghome.html')
    else:
        return redirect('/')


@app.route('/gapartment')
def gapartment():
    if 'password' in session:
        cursor.execute("SELECT* FROM apartment_details")
        myapartment = cursor.fetchall()
        return render_template('gapartment.html', gapartments=myapartment)
    else:
        return redirect('/')


@app.route('/glogout')
def glogout():
    session.pop('password')
    return redirect('/')


# ..................................admin................................................


@app.route('/login_validation', methods=['POST'])
def login_validation():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute(
        """SELECT * FROM `user` WHERE `username` LIKE '{}' AND `password` LIKE '{}' AND `user_type`='Admin'"""
        .format(username, password))
    admin = cursor.fetchall()
    cursor.execute("""SELECT * FROM `user` WHERE `username` LIKE '{}' AND `password` LIKE '{}' AND `user_type`='User'"""
                   .format(username, password))
    user = cursor.fetchall()

    if (admin):
        if len(admin) > 0:
            session['user_id'] = admin[0][0]
            return redirect('/home')

    if (user):
        if len(user) > 0:
            session['password'] = user[0][5]
            return redirect('/ghome')

    return redirect('/')


@app.route('/add_admin', methods=['POST'])
def add_admin():
    fullname = request.form.get('afullname')

    username = request.form.get('ausername')
    cursor.execute("SELECT username FROM user")
    u = cursor.fetchall()
    for i in u:
        for j in i:
            if username == j:
                flash("Usrname already exists")
                return redirect('/register')
            else:
                username = request.form.get('ausername')

    email = request.form.get('aemail')
    cursor.execute("SELECT email FROM user")
    e = cursor.fetchall()
    for k in e:
        for l in k:
            if email == l:
                flash("Email already exists")
                return redirect('/register')
            else:
                email = request.form.get('aemail')

    address = request.form.get('aaddress')
    password = request.form.get('apassword')
    usertype = request.form.get('usertype')
    cursor.execute(
        """INSERT INTO `user`(`user_id`, `fullname`, `username`, `email`,`address`, `password`,`user_type`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(
            fullname, username, email, address, password, usertype))
    conn.commit()
    cursor.execute(
        """SELECT * FROM `user` WHERE `username` LIKE '{}' and `user_type`='Admin'""".format(username, usertype))
    myadmin = cursor.fetchall()
    cursor.execute(
        """SELECT * FROM `user` WHERE `username` LIKE '{}' and `user_type`='User'""".format(username, usertype))
    myuser = cursor.fetchall()

    if (myadmin):
        session['user_id'] = myadmin[0][0]
        return redirect('/home')
    elif (myuser):
        session['password'] = myuser[0][5]
        return redirect('/ghome')


# .....................................admin profile............

@app.route('/aprofile')
def aprofile():
    if 'user_id' in session:
        s = session['user_id']
        cursor.execute("SELECT * FROM user WHERE user_id = '" + str(s) + "'")
        p = cursor.fetchone()

        return render_template('aprofile.html', p=p)

    else:
        return redirect('/')


# ...................................................Apartment....................................................

@app.route('/view_image', methods=['GET', 'POST'])
def view_image():
    return redirect('/apartment')


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        apartmentname = request.form['Apartment_name']

        location = request.form['Location']
        numberofroom = request.form['Number_of_room']
        floor = request.form['Floor']
        type = request.form['Type']
        details = request.form['Details']
        description = request.form['Description']
        cost = request.form['Cost']
        file1 = request.files['file1']
        filename1 = secure_filename(file1.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

        file2 = request.files['file2']
        filename2 = secure_filename(file2.filename)
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

        file3 = request.files['file3']
        filename3 = secure_filename(file3.filename)
        file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename3))

        available = request.form['available']
        cursor.execute(
            "INSERT INTO apartment_details (Apartment_name,Location,Number_of_room,Floor,Type,Details,Description,Cost,image1,image2,image3,Available) VALUES (%s,%s,%s,%s, %s, %s, %s ,%s, %s, %s, %s,%s)",
            (apartmentname, location, numberofroom, floor, type, details, description, cost, filename1, filename2,
             filename3, available))
        conn.commit()
        return redirect('/apartment')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":

        apartmentno = request.form['Apartment_no']
        apartmentname = request.form['Apartment_name']

        location = request.form['Location']
        numberofroom = request.form['Number_of_room']
        floor = request.form['Floor']
        type = request.form['Type']
        details = request.form['Details']
        description = request.form['Description']
        cost = request.form['Cost']

        file1 = request.files['file1']
        filename1 = secure_filename(file1.filename)
        if filename1 == '':
            filename1 = request.form['file11']
        else:
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

        file2 = request.files['file2']
        filename2 = secure_filename(file2.filename)
        if filename2 == '':
            filename2 = request.form['file22']
        else:
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

        file3 = request.files['file3']
        filename3 = secure_filename(file3.filename)
        if filename3 == '':
            filename3 = request.form['file33']
        else:
            file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename3))

        available = request.form['available']
        if available == 'Available':
            available = request.form['avail']
        else:
            available = request.form['available']

        cursor.execute("""UPDATE apartment_details 
        SET  Apartment_name=%s, Location=%s ,Number_of_room=%s ,Floor=%s ,Type=%s ,Details=%s ,Description=%s, Cost=%s,image1=%s,image2=%s,image3=%s, Available=%s   
        WHERE Apartment_no=%s

        """, (
        apartmentname, location, numberofroom, floor, type, details, description, cost, filename1, filename2, filename3,
        available, apartmentno))
        flash("Data Updated Successfully")
        conn.commit()

        return redirect('/apartment')


@app.route('/deletee/<string:apartmentno>', methods=['POST', 'GET'])
def delete(apartmentno):
    flash("Record has been deleted successfully")

    cursor.execute("DELETE FROM apartment_details WHERE Apartment_no=%s", (apartmentno,))
    conn.commit()
    return redirect('/apartment')


# ...................................request......................................

@app.route('/request')
def requ():
    if 'user_id' in session:
        cursor.execute("SELECT* FROM `request_details`")
        myrequest = cursor.fetchall()
        return render_template('request.html', request=myrequest)
    else:
        return redirect('/')


@app.route('/insert_re', methods=['POST'])
def insert_re():
    if request.method == "POST":
        flash("Apartment Request Accepted and tenant has been added to the Tenant details")
        requestid = request.form['Request_id']
        tenantname = request.form['Name']
        apartmentno = request.form['Apartment_no']

        address = request.form['Address']
        email = request.form['Email']
        phonenumber = request.form['Phone_number']

        cursor.execute(
            "INSERT INTO tenant_details (Tenant_name,Apartment_no,Address,Email,Phone_number) VALUES (%s, %s ,%s, %s, %s)",
            (tenantname, apartmentno, address, email, phonenumber))
        conn.commit()
        cursor.execute("DELETE FROM request_details WHERE Request_ID=%s", (requestid,))
        conn.commit()
        return redirect('/request')


@app.route('/delete_re/<string:requestid>', methods=['POST', 'GET'])
def delete_re(requestid):
    flash("Request has been Rejected")

    cursor.execute("DELETE FROM request_details WHERE Request_ID=%s", (requestid,))
    conn.commit()
    return redirect('/request')


# ................................Tenant.........................................


@app.route('/insert_tenant', methods=['POST'])
def insert_tenant():
    if request.method == "POST":
        flash("Data Inserted Successfully")

        tenantname = request.form['Tenant_name']
        apartmentno = request.form['Apartment_no']

        address = request.form['Address']
        email = request.form['Email']
        phonenumber = request.form['Phone_number']

        cursor.execute(
            "INSERT INTO tenant_details (Tenant_name,Apartment_no,Address,Email,Phone_number) VALUES (%s, %s ,%s, %s, %s)",
            (tenantname, apartmentno, address, email, phonenumber))
        conn.commit()
        return redirect('/tenant')


@app.route('/update_tenant', methods=['GET', 'POST'])
def update_tenant():
    if request.method == "POST":
        tenantid = request.form['Tenant_id']
        tenantname = request.form['Tenant_name']
        apartmentno = request.form['Apartment_no']

        address = request.form['Address']
        email = request.form['Email']
        phonenumber = request.form['Phone_number']
        cursor.execute("""UPDATE tenant_details 
        SET   Tenant_name=%s,Apartment_no=%s,Address=%s,Email=%s  ,Phone_number=%s 
        WHERE Tenant_ID=%s

        """, (tenantname, apartmentno, address, email, phonenumber, tenantid))
        flash("Data Updated Successfully")
        conn.commit()

        return redirect('/tenant')


@app.route('/delete_tenant/<string:tenantid>', methods=['POST', 'GET'])
def delete_tenant(tenantid):
    flash("Record has been deleted successfully")

    cursor.execute("DELETE FROM tenant_details WHERE Tenant_ID=%s", (tenantid,))
    conn.commit()
    return redirect('/tenant')


# .............................................Rent Request........................................

@app.route('/rent_request')
def rerequ():
    if 'user_id' in session:
        cursor.execute("SELECT* FROM `rent_request`")
        myrrequest = cursor.fetchall()
        return render_template('rent_request.html', rrequest=myrrequest)
    else:
        return redirect('/')


@app.route('/insert_rere', methods=['POST'])
def insert_rere():
    if request.method == "POST":
        flash("Rent Collected Successfully")
        reid = request.form['Request_id']
        tenantid = request.form['Tenant_ID']
        tenantname = request.form['Tenant_name']
        apartmentno = request.form['Apartment_no']

        paiddate = request.form['Paid_Date']
        paidamount = request.form['Paid_amount']
        tran = request.form['Transection_no']

        month = request.form['Month']

        cursor.execute(
            "INSERT INTO rent_info (Tenant_ID,Tenant_name,Apartment_no,Paid_Date,Paid_amount,Transection_no,Month) VALUES (%s, %s,%s,%s,%s,%s,%s)",
            (tenantid, tenantname, apartmentno, paiddate, paidamount, tran, month))
        conn.commit()

        cursor.execute("DELETE FROM rent_request WHERE Request_id=%s", (reid,))
        conn.commit()

        return redirect('/rent_request')


@app.route('/delete_rere/<string:reid>', methods=['POST', 'GET'])
def delete_rere(reid):
    flash("Rent has been rejected successfully")

    cursor.execute("DELETE FROM rent_request WHERE Request_id=%s", (reid,))
    conn.commit()
    return redirect('/rent_request')


# ..................................................Rent..........................................


@app.route('/insert_rent', methods=['POST'])
def insert_rent():
    if request.method == "POST":
        flash("Data has Inserted Successfully")

        tenantid = request.form['Tenant_ID']
        tenantname = request.form['Tenant_name']
        apartmentno = request.form['Apartment_no']

        paiddate = request.form['Paid_Date']
        paidamount = request.form['Paid_amount']
        tran = request.form['Transection_no']

        month = request.form['Month']

        cursor.execute(
            "INSERT INTO rent_info (Tenant_ID,Tenant_name,Apartment_no,Paid_Date,Paid_amount,Transection_no,Month) VALUES (%s, %s,%s,%s,%s,%s,%s)",
            (tenantid, tenantname, apartmentno, paiddate, paidamount, tran, month))
        conn.commit()
        return redirect('/rent')


@app.route('/update_rent', methods=['GET', 'POST'])
def update_rent():
    if request.method == "POST":
        rentid = request.form['Rent_id']
        tenantid = request.form['Tenant_ID']
        tenantname = request.form['Tenant_name']
        apartmentno = request.form['Apartment_no']

        paiddate = request.form['Paid_Date']
        paidamount = request.form['Paid_amount']
        tran = request.form['Transection_no']
        month = request.form['Month']

        cursor.execute("""UPDATE rent_info 
        SET   Tenant_ID=%s,Tenant_name=%s,Apartment_no=%s,Paid_date=%s,Paid_amount=%s,Transection_no=%s,Month=%s 
        WHERE Rent_id=%s

        """, (tenantid, tenantname, apartmentno, paiddate, paidamount, tran, month, rentid))
        flash("Data Updated Successfully")
        conn.commit()

        return redirect('/rent')


@app.route('/delete_rent/<string:rentid>', methods=['POST', 'GET'])
def delete_rent(rentid):
    flash("Record has been deleted successfully")

    cursor.execute("DELETE FROM rent_info WHERE Rent_id=%s", (rentid,))
    conn.commit()
    return redirect('/rent')


# ..............................User Apartment...............................................

@app.route('/send_request', methods=['POST'])
def send_request():
    if request.method == "POST":
        flash("monifa Request for Apartment has been send from User")

        name = request.form['Tenant_name']
        apartmentno = request.form['Apartment_no']

        address = request.form['Address']
        email = request.form['Email']

        phonenumber = request.form['Phone_number']
        cursor.execute(
            "INSERT INTO request_details (Name,Apartment_no,Address,Email,Phone_number) VALUES (%s, %s ,%s, %s, %s)",
            (name, apartmentno, address, email, phonenumber))
        conn.commit()
        return redirect('/gapartment')


@app.route('/search', methods=['GET', 'POST'])
def search():


    if request.method == "POST":
     if 'password' in session:
        s = session['password']
        apartment = request.form['Apartment']
        cursor.execute(
            "SELECT * FROM apartment_details WHERE Location LIKE %s OR Floor LIKE %s OR Number_of_room LIKE %s OR Cost LIKE %s ",
            (apartment, apartment, apartment, apartment))
        mygapartment = cursor.fetchall()

        if (len(mygapartment) == 0 and apartment == 'all') or len(apartment) == 0:

            cursor.execute("SELECT * FROM apartment_details WHERE Floor='" + s + "'")

            mygapartment = cursor.fetchall()
        return render_template('gapartment.html', gapartments=mygapartment)
    return redirect('/gapartment')


# .................................user profile...................................

@app.route('/profile')
def profile():
    if 'password' in session:
        s = session['password']
        cursor.execute("SELECT * FROM user WHERE password ='" + s + "'")
        p = cursor.fetchone()

        cursor.execute("SELECT * FROM tenant_details where email=(SELECT email FROM user WHERE password ='" + s + "')")
        t = cursor.fetchone()

        if t:
            return render_template('tprofile.html', t=t)
        elif p:
            return render_template('profile.html', p=p)

    else:
        return redirect('/')


# ..............................Payrent...............................

@app.route('/payrent')
def payrent():
    if 'password' in session:
        return render_template('payrent.html')
    else:
        return redirect('/')


@app.route('/i_payrent', methods=['POST'])
def i_payrent():
    if request.method == "POST":
        flash("Tenant Just Paid.Please collect the Rent")

        tenantid = request.form['Tenant_ID']
        tenantname = request.form['Tenant_name']
        apartmentno = request.form['Apartment_no']

        paiddate = request.form['Paid_Date']
        paidamount = request.form['Paid_amount']
        tran = request.form['Transection_no']
        month = request.form['Month']

        cursor.execute(
            "INSERT INTO rent_request (Tenant_ID,Tenant_name,Apartment_no,Paid_Date,Paid_amount,Transection_no,Month) VALUES (%s, %s, %s,%s,%s,%s,%s)",
            (tenantid, tenantname, apartmentno, paiddate, paidamount, tran, month))
        conn.commit()
        return redirect('/payrent')


if __name__ == "__main__":
    app.run(debug=True)