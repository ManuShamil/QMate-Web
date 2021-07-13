from flask import Flask,render_template,request,session, redirect, jsonify
from dbconnection import Db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import random
import datetime

app = Flask(__name__)
app.secret_key="hai"
staticpath="C:\\Users\\ACM\\PycharmProjects\\Qmate\\static\\"
@app.route('/vv')
def login():
    return render_template('login.html')

@app.route('/login_post',methods=['POST'])
def login_post():
    Username = request.form['username']
    Password = request.form['pass']
    db=Db()
    qry="SELECT * FROM `login` WHERE `user_name`='"+Username+"' AND `password`='"+Password+"'"
    res=db.selectone(qry)
    if res is not None:
        if res['user_type']=="admin":
            session['id']=res['login_id']
            return adminpage()
        elif res['user_type']=="store":

            session['stid'] = res['login_id']
            q="SELECT `status` FROM `store` WHERE `login_id`='"+str(res['login_id'])+"'"
            d=db.selectone(q)
            if d is not None:
                if d["status"] == "approved":
                    print(session['stid'])
                    return storepage()
                elif d["status"] == "rejected":
                    return '''<script>alert('you are rejected');window.location="/"</script>'''
                else:
                    return '''<script>alert('Pending');window.location="/"'''
            else:
                return '''<script>alert('Invalid username or password');window.location="/"</script>'''




        elif res['user_type']=="security":
            session['secid'] = res['login_id']
            print(session['secid'])
            return render_template('admin/security_hom.html')

    else:
        return '''<script>alert("invalid username or password");window.location="/"</script>'''


@app.route('/store_hom')
def store_hom():
    return render_template('store/store_hom.html')




@app.route('/adminstoreappr')
def adminstoreappr1():
    c = Db()
    qry = "SELECT * FROM store where status='pending';"
    res = c.selectall(qry)
    print(res)
    return render_template('admin/admin_store_approvel.html', data = res)



@app.route('/process_store_status', methods=['GET'])
def process_store_status_post():
    id = request.args.get('id')
    action = request.args.get('action')

    if (action == 'accept'):
        qry = "UPDATE store SET status = 'approved' WHERE store_id = " + str(id)
    else:
        qry = "UPDATE store SET status = 'rejected' WHERE store_id = " + str(id)
    print(qry)
    db = Db()
    a=db.update(qry)
    return redirect('/adminstoreappr')



@app.route('/adminusrvisithis')
def adminusrvisithis():
    c = Db()
    qry = "SELECT `visiting_history`.*,`space_slot`.*,`store`.`store_name`,`store`.`store_id`,`user`.* FROM `visiting_history`,`space_slot`,`store`,`user` WHERE `space_slot`.`store_id`=`store`.`store_id` AND `visiting_history`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `visiting_history`.`user_id`=`user`.`login_id`"
    print(qry)
    res = c.selectall(qry)
    return render_template('admin/admin_uservisitinghistory.html',data=res)

@app.route('/adminusrvisithispost',methods=['post'])
def adminusrvisithispost():


    frm=request.form['from']
    to=request.form['to']

    c = Db()
    qry = "SELECT `visiting_history`.*,`space_slot`.*,`store`.`store_name`,`store`.`store_id`,`user`.* FROM `visiting_history`,`space_slot`,`store`,`user` WHERE `space_slot`.`store_id`=`store`.`store_id` AND `visiting_history`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `visiting_history`.`user_id`=`user`.`login_id` and `visiting_history`.`date` between '"+frm+"' and '"+to+"'"
    print(qry)
    res = c.selectall(qry)
    return render_template('admin/admin_uservisitinghistory.html',data=res)



@app.route('/vehlocparkappr')
def vehlocparkappr1():
    # render_template('admin/admin_vehiclelocationparkingapproval.html')
    c=Db()
    qry="SELECT * FROM  parking WHERE `status`='pending'"
    print(qry)
    res=c.selectall(qry)
    print(res)
    return render_template('admin/admin_vehiclelocationparkingapproval.html',data=res)

@app.route('/vehlocparkapproved')
def vehlocparkapproved():
    # render_template('admin/admin_vehiclelocationparkingapproval.html')
    c=Db()
    qry="SELECT * FROM  parking WHERE `status`='approved'"
    print(qry)
    res=c.selectall(qry)
    print(res)
    return render_template('admin/approvedparking.html',data=res)


@app.route('/vehlocparkapprovedpost',methods=['post'])
def vehlocparkapprovedpost():
    s=request.form["search"]
    # render_template('admin/admin_vehiclelocationparkingapproval.html')
    c=Db()
    qry="SELECT * FROM  parking WHERE `status`='approved' and name like '%"+s+"%'"
    print(qry)
    res=c.selectall(qry)
    print(res)
    return render_template('admin/approvedparking.html',data=res)




@app.route('/process_parking_status', methods=['GET'])
def process_parking_status_post():
    id = request.args.get('id')
    action = request.args.get('action')
    if (action == 'accept'):
        qry = "UPDATE parking SET status = 'approved' WHERE parking_slot_id = " + str(id)
    else:
        qry = "UPDATE parking SET status = 'rejected' WHERE parking_slot_id= " + str(id)
    print(qry)
    db = Db()
    a=db.update(qry)
    return redirect('/vehlocparkappr')




@app.route('/viewcomp')
def viewcomp1():
    c=Db()
    qry="SELECT `user`.* ,`complaint`.* FROM `complaint` , `user` WHERE `complaint`.`customer_id`=`user`.`login_id` AND `complaint`.`reply`='pending'"
    print(qry)
    res=c.selectall(qry)
    print(res)
    return render_template('admin/admin_viewcomplaint.html',data=res)

@app.route('/viewcomppost',methods=['post'])
def viewcomppost():
    fro= request.form["from"]
    to= request.form["to"]
    c=Db()
    qry="SELECT `user`.* ,`complaint`.* FROM `complaint` , `user` WHERE `complaint`.`customer_id`=`user`.`login_id`  and date between '"+fro+"' and '"+to+"' AND `complaint`.`reply`='pending'"
    print(qry)
    res=c.selectall(qry)
    print(res)
    return render_template('admin/admin_viewcomplaint.html',data=res)



@app.route('/adminsndrply/<cid>')
def adminsndrply1(cid):
    session['cid']=cid
    # db=Db()
    # qry="UPDATE FROM complaint WHERE reply ='"++"'"
    # print(qry)
    # res=c.selectall(qry)
    # print(res)
    return render_template('admin/admin_sendreply.html')

@app.route('/adminsndrply_post',methods=['POST'])
def adminsndrply1_post():
    print("mm")
    db=Db()
    print("kkkkkkkkkkk")
    y=session['cid']
    reply=request.form['txt1']
    qry="UPDATE `complaint` SET `reply`= '"+reply+"' WHERE `complaint_id`='"+str(y)+"'"
    print(qry)
    res=db.update(qry)
    return viewcomp1()




@app.route('/viewregstr')
def viewregstr1():
    c=Db()
    qry="SELECT * FROM  store WHERE status = 'approved'"
    print(qry)
    res=c.selectall(qry)
    print(res)
    return render_template('admin/admin_viewregisteredstore.html',data=res)

@app.route('/viewregstrpost',methods=['post'])
def viewregstrpost():

    s=request.form["search"]
    c=Db()
    qry="SELECT * FROM  store WHERE status = 'approved' and store_name like '%"+s+"%'"
    print(qry)
    res=c.selectall(qry)
    print(res)
    return render_template('admin/admin_viewregisteredstore.html',data=res)



@app.route('/viewusr')
def viewussr1():
    c=Db()
    qry="SELECT * FROM user"
    res=c.selectall(qry)
    return render_template('admin/admin_viewuser.html',data=res)

@app.route('/viewusrstatus/<kk>')
def viewusrstatus(kk):
    c=Db()
    qry="SELECT * FROM `covid_status` WHERE `user_id`='"+kk+"'"
    res=c.selectone(qry)
    qry2="SELECT `visiting_history`.*,`space_slot`.*,`store`.`store_name`,`store`.`store_id`,`user`.* FROM `visiting_history`,`space_slot`,`store`,`user` WHERE `space_slot`.`store_id`=`store`.`store_id` AND `visiting_history`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `visiting_history`.`user_id`=`user`.`login_id` AND `user`.`login_id`='"+kk+"'"
    res3=c.selectall(qry2)
    return render_template('admin/admin_view_user_covid_status.html',data=res,data3=res3)


@app.route('/viewusrpost',methods=['post'])
def viewusrpost():


    s=request.form["search"]

    c=Db()
    qry="SELECT * FROM user where user_name like '%"+s+"%'"
    res=c.selectall(qry)
    return render_template('admin/admin_viewuser.html',data=res)




@app.route('/store_adds_ecurity')
def store_adds_ecurity1():
    return render_template('store/store_addsecurity.html')

@app.route('/store_adds_ecurity_post',methods=['POST'])
def store_adds_ecurity_post():
    Name=request.form['textfield']
    print(Name)
    DOB=request.form['textfield1']
    print(DOB)
    Gender=request.form['RadioGroup1']
    print(Gender)
    Place=request.form['textfield2']
    print(Place)
    Pin=request.form['textfield3']
    print(Pin)
    Post=request.form['textfield4']
    print(Post)
    City=request.form['textfield5']
    print(City)
    State=request.form['textfield6']
    print(State)
    Photo=request.files['imgage']
    Photo.save(staticpath + "store_security\\" + Photo.filename)
    path = "/static/store_security/" + Photo.filename

    print(Photo)
    Phone=request.form['textfield9']
    print(Phone)
    Email=request.form['textfield10']
    print(Email)
    import random
    psw=random.randint(0000,9999)



    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("myprojectquemate@gmail.com","2021@myqmate")
    msg = MIMEMultipart()  # create a message.........."
    message = "Messege from Qmate"
    msg['From'] = "myprojectqmate@gmail.com"
    msg['To'] = Email
    msg['Subject'] = "Your Password  Q Mate"
    body = "Your Account has been added to Q Mate Project. You Can Now login using your password - " + str(psw)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)



    db=Db()
    qry1="INSERT INTO `login`(`user_name`,`PASSWORD`,`user_type`)VALUES('"+Email+"','"+str(psw)+"','security')"
    res1=db.insert(qry1)
    qry2="INSERT INTO `security`(`security_name`,`age`,`gender`,`pin`,`photo`,`store_id`,`login_id`,`phone`,`email`,`post`,`place`,`city`,`state`)values('"+Name+"','"+DOB+"','"+Gender+"','"+Pin+"','"+path+"','"+str(session['stid'])+"','"+str(res1)+"','"+Phone+"','"+Email+"','"+Post+"','"+Place+"','"+City+"','"+State+"')"
    res2=db.insert(qry2)
    return '<script>alert("successfully Inserted");window.location="/store_adds_ecurity"</script>'


@app.route('/storeviwe_secty')
def storeviwe_secty():
    d = Db()
    qry="SELECT * FROM SECURITY where store_id='"+str(session['stid'])+"'"
    res = d.selectall(qry)
    print(res)
    return render_template('store/store_securityview.html', data=res)



@app.route('/storeviwe_sectypost',methods=['post'])
def storeviwe_sectypost():
    s=request.form["search"]
    d = Db()
    qry="SELECT * FROM SECURITY where store_id='"+str(session['stid'])+"' and  security_name like '%"+s+"%'"
    res = d.selectall(qry)
    print(res)
    return render_template('store/store_securityview.html', data=res)


@app.route('/storeseqdelete/<id>')
def storeviwde1(id):
    s="delete from `security` WHERE `security_id`='"+id+"'"
    d=Db()
    r=d.delete(s)
    return '<script>alert("deleted");window.location="/storeviw"</script>'

@app.route('/storeseqedit/<id>')
def storeviwed1(id):
     s="select *  from `security` where security_id='"+id+"'"
     d=Db()
     session['eid']=id
     r=d.selectone(s)
     return render_template('store/store_securityupdate.html', data=r)

@app.route('/storeseqeditt')
def storeviwedt1():
      d = Db()
      qry = "update FROM SECURITY "
      res = d.selectall(qry)
      print(res)
      return "ok"



# @app.route('/storeupdtprof')
# def storeupdtprof12():
#     data = []
#
#     d = Db()
#     qry = "SELECT "
#     res = d.selectall(qry)

    # return render_template('store/store_securityupdate.html')

@app.route('/storeupdtsecty',methods=['POST'])
def storeupdtprof5_post():
    print("hiiiiii")
    db=Db()

    name=request.form['textfield']
    age=request.form['textfield1']
    gender=request.form['RadioGroup1']
    place=request.form['textfield2']
    Pin=request.form['textfield3']
    post=request.form['textfield4']
    City=request.form['textfield5']
    state=request.form['textfield6']
    phone=request.form['textfield9']
    email=request.form['textfield10']
    print("jk")



    img = request.files["fff"]

    print("image=")

    if img.filename == '':
        print("kkkkkkkkk")
        qry = "UPDATE `security` SET `security_name`='" + name + "',`age`='" + age + "',`gender`='" + gender + "',`pin`='" + Pin + "',`phone`='" + phone + "',`email`='" + email + "',`post`='" + post + "',`place`='" + place + "',`city`='" + City + "',`state`='" + state + "' WHERE `security_id`='" + str(
            session['eid']) + "'"
        print(qry)
        res2 = db.update(qry)

    else:
        print("mmmmmmmmmmm")
        img.save(staticpath + "store_security\\" + img.filename)
        path = "/static/store_security/" + img.filename
        qry = "UPDATE `security` SET `security_name`='" + name + "',`age`='" + age + "',`gender`='" + gender + "',`pin`='" + Pin + "',`photo`='" + path + "',`phone`='" + phone + "',`email`='" + email + "',`post`='" + post + "',`place`='" + place + "',`city`='" + City + "',`state`='" + state + "' WHERE `security_id`='" + str(
            session['eid']) + "'"
        print(qry)
        db = Db()
        ss = db.update(qry)

    return storeviwe_secty()










@app.route('/strviwspslt')
def strviwspslt1():
    qry = "SELECT *   FROM `space_slot`;"
    db = Db()
    res = db.selectall( qry )
    print(res)
    return render_template('store/store_viewspaceslot.html', data=res)

@app.route('/strviwspslt_post',methods=['POST'])
def strviwspslt_post():


    return "ok"

@app.route('/strviwspslt_delete/<id>')
def strviwspslt_delete2(id):
    s="delete from `space_slot` WHERE `spaceslot_id`='"+id+"'"
    d=Db()
    r=d.delete(s)
    return '<script>alert("deleted");window.location="/strviwspslt"</script>'



@app.route('/straddspslt')
def straddspslt1():
    return render_template('store/store_addspaceslot.html')

@app.route('/straddspslt_post',methods=['POST'])
def straddspslt_post():
    Opening_time=request.form['textfield']
    Closing_time = request.form['textfield1']
    stdid = str(session['stid'])
    # print("ZZZZZZZZZZZZz",type(Opening_time))
    # print(Opening_time)
    # from datetime import datetime, timedelta
    # import time
    # # curr = datetime.now()
    # datetime_object = time.strptime(Opening_time, '%H:%M')
    # print(datetime_object)
    # seq1 = []
    # for x in range(10):
    #     datetime_object = datetime_object + timedelta(minutes=15)
    # seq1.append(Opening_time.strftime("%H:%M"))
    # print(seq1)


    ######asw
    time_list1=Opening_time.split(":")
    time_list2=Closing_time.split(":")
    slot_two_hour = time_list1[0]
    slot_two_min = time_list1[1]
    print(slot_two_hour," ",slot_two_min)
    print(time_list2[0], " ", time_list2[1])
    time1 = int(slot_two_hour) * 60 + int(slot_two_min)
    time2 = int(time_list2[0]) * 60 + int(time_list2[1])
    # while (int(slot_two_hour)<int(time_list2[0])) and (int(slot_two_min)<int(time_list2[1])):
    seq=[]
    from datetime import date, datetime, time, timedelta
    dt = datetime.combine(date.today(), time(int(time_list1[0]), int(time_list1[1])))
    print(dt.time())
    seq.append(dt.time())
    print(dt.time())

    print("seq===")
    print(seq)
    print("ovr")
    while (time2>time1):

        dt = datetime.combine(date.today(), time(int(slot_two_hour), int(slot_two_min))) + timedelta(minutes=10)
        print(dt.time())
        ss=str(dt.time()).split(":")
        slot_two_hour=ss[0]
        slot_two_min=ss[1]
        time1=int(slot_two_hour) * 60 + int(slot_two_min)
        seq.append(dt.time())

    print(seq)
    print("ovr2")
    for i in range(0,len(seq)-1):
        qry = "INSERT INTO space_slot(`store_id`,`From_time`, `T0_time`,`Date`,`Status`) VALUES ('"+stdid+"','"+str(seq[i])+"','"+str(seq[i+1])+"',curdate(),'free')"
        db = Db()
        res = db.insert(qry)
    return render_template("store/store_addspaceslot.html")

@app.route('/strcustlimmang')
def strcustlimmang1():
    qry = ""
    db = Db()
    db.selectall( qry )
    return render_template('store/store_customerlimitmanagment.html')

@app.route('/strreg')
def strreg():
    return render_template('store/store_registration.html')

@app.route('/strreg_post',methods=['post'])
def strreg_post():
    try:
        name = request.form['textfield']
        print(name)
        place = request.form['textfield2']
        print(place)
        post = request.form['textfield3']
        print(post)
        pin = request.form['textfield4']
        print(pin)
        phone = request.form['textfield5']
        print(phone)
        email = request.form['textfield6']
        print(email)
        Password = request.form['textfield7']
        print(Password)
        Confirm_password = request.form['textfield8']
        print(Confirm_password)
        if Password==Confirm_password:
            db=Db()
            qry1="INSERT INTO `login`(`user_name`,`PASSWORD`,`user_type`)VALUES('"+email+"','"+Password+"','store')"
            res1=db.insert(qry1)
            qry2="INSERT INTO `store`(`store_name`,`post`,`pin`,`place`,`phone`,`email`,`login_id`,`status`)VALUES('"+name+"','"+post+"','"+pin+"','"+place+"','"+phone+"','"+email+"','"+str(res1)+"','pending')"
            res2=db.insert(qry2)
            return render_template("store/store_registration.html")
    except Exception as e:
        print(str(e))





@app.route('/storeupjdtprof_post',methods=['POST'])
def storeupdtprof_post():
    name=request.form['textfield']
    place=request.form['textfield1']
    post=request.form['textfield2']
    pin=request.form['textfield3']
    phone=request.form['textfield4']
    email=request.form['textfield5']

    return "ok"




@app.route('/strviwprof')
def strviwprof1():
    db=Db()
    qry="SELECT * FROM `store` WHERE login_id='"+str(session['stid'])+"'"
    res=db.selectone(qry)
    return render_template('store/store_viewprofile.html',data=res)



@app.route('/strqststus')
def strqststus1():
    c = Db()
    print(str(session['stid']))
    # qry="SELECT `que_status`.*,`user`.*,`space_slot`.* FROM `que_status` INNER JOIN `user` ON `que_status`.`user_id`=`user`.`login_id` INNER JOIN `space_slot` ON `space_slot`.`spaceslot_id`=`que_status`.`space_id` WHERE `space_slot`.`store_id`='"+str(session['stid'])+"'"
    qry="SELECT `booking_slot`.*,`space_slot`.*,`store`.*,`user`.* FROM `booking_slot`,`space_slot` ,`store`,`user` WHERE `space_slot`.`spaceslot_id`=`booking_slot`.`space_slot_id` AND `store`.`login_id`=`space_slot`.`store_id` AND `user`.`login_id`=`booking_slot`.`customer_id` AND`store`.`login_id`='"+str(session['stid'])+"'"
    res = c.selectall(qry)
    print(res)
    return render_template('store/store_viewqueuestatus.html', data=res)



@app.route('/strvie')
def strvie1():
    c = Db()
    qry="SELECT user.* ,`visiting_history`.*,`space_slot`.* FROM `visiting_history`,`user`,space_slot WHERE  `visiting_history`.`user_id`=`user`.`login_id` AND `visiting_history`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `space_slot`.`store_id`='"+str(session['stid'])+"'"
    res=c.selectall(qry)
    print(res)
    return render_template('store/store_viewvisitor.html',data=res)


@app.route('/strviepost',methods=['post'])
def strviepost():

    frm=request.form["from"]
    to=request.form["to"]

    c = Db()
    qry="SELECT user.* ,`visiting_history`.*,`space_slot`.* FROM `visiting_history`,`user`,space_slot WHERE  `visiting_history`.`user_id`=`user`.`login_id` AND `visiting_history`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `space_slot`.`store_id`='"+str(session['stid'])+"' and visiting_history.date between '"+frm+"' and '"+to+"'"
    res=c.selectall(qry)
    print(res)
    return render_template('store/store_viewvisitor.html',data=res)


@app.route('/view')
def view1():
    qry = "select * from user"
    db = Db()
    a=db.selectall(qry)

@app.route('/')
def loginpage():
    return render_template("login_index.html")

@app.route('/adminpage')
def adminpage():
    return render_template("admin/admin_hom.html")

@app.route('/storepage')
def storepage():
    return render_template("store/store_hom.html")




#########################           ANDROID
# @app.route('/and_login_post')
# def and_login_post():
#     return jsonify(status="ok")




@app.route('/and_login_post',methods=['POST'])
def and_login_post():
    Username = request.form['username']
    Password = request.form['pass']
    db=Db()

    qry="SELECT * FROM `login` WHERE `user_name`='"+Username+"' AND `password`='"+Password+"'"

    print(qry)
    res=db.selectone(qry)

    if res is not None:
        if res['user_type']=="security":
            qry = "SELECT * FROM security WHERE login_id='" + str(res['login_id']) + "'"
            res1 = db.selectone(qry)
            return jsonify(status='ok',lid=res['login_id'],type='security',store_id=res1['store_id'])
        elif res['user_type']=="parking":
            return jsonify(status='ok', lid=res['login_id'], type='parking')
        elif res['user_type']=="user":
            return jsonify(status='ok', lid=res['login_id'], type='user')
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='no')






@app.route('/and_security_viewprofile',methods=['POST'])
def and_security_viewprofile():
    lid=request.form['login_id']
    db=Db()
    qry="SELECT * FROM security WHERE login_id='"+lid+"'"
    print(qry)
    res=db.selectone(qry)
    print(qry)
    if res is not None:
        return jsonify(status='ok',name=res['security_name'],age=res['age'],gender=res['gender'],pin=res['pin'],photo=res['photo'],phone=res['phone'],email=res['email'],place=res['place'],city=res['city'],post=res['post'],state=res['state'])
    else:
        return jsonify(status='no')





@app.route('/and_security_viewavailable_spaceslot',methods=['POST'])
def and_security_viewavailable_spaceslot():
    store_id=request.form['store_id']
    db=Db()
    # qry="SELECT `spaceslot_id`, `counter_no`, `status` FROM space_slot where store_id ='" + store_id + "'"

    qry="SELECT `spaceslot_id`, `From_time`,`T0_time`,`Date`, `status` FROM space_slot WHERE store_id ='"+store_id+"'"
    print(qry)

    res = db.selectall(qry)
    if res is not None:
        return jsonify(status='ok',data=res)
    else:
        return jsonify(status='no')





@app.route('/and_security_view_questatus',methods=['POST'])
def and_security_view_questatus():
    store_id = request.form['store_id']
    db = Db()
    qry = "SELECT `que_status`.`que_status_id`,`user`.user_name,user.`photo`,que_status.`time`,que_status.`date` FROM `que_status`,`user`,`space_slot` WHERE `que_status`.`user_id`=`user`.`login_id` AND `space_slot`.`spaceslot_id`=`que_status`.`space_id` AND `que_status`.`user_id`=`user`.`login_id` AND space_slot.store_id='"+store_id+"'"
    res = db.selectall(qry)
    if res is not None:
        return jsonify(status='ok', data=res)
    else:
        return jsonify(status='no')





@app.route('/and_security_issue_tocken',methods=['POST'])
def and_security_issue_tocken():
    que_status_id = request.form['que_status_id']
    tocken_no=request.form['tocken_no']
    db = Db()
    qry = ""
    res = db.selectall(qry)
    if res is not None:
        return jsonify(status='ok', data=res)
    else:
        return jsonify(status='no')




@app.route('/and_user_registration',methods=['POST'])
def and_user_registration():
    name=request.form['name']
    dob = request.form['dob']
    gender= request.form['gender']
    address= request.form['address']
    phone= request.form['phone']
    email= request.form['email']
    password= request.form['password']
    print("kkk")
    image=request.form['image']
    print("jk")
    import time
    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(image)
    fh = open(staticpath+"user_images\\" + timestr + ".jpg", "wb")
    path = "/static/user_images/" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    db=Db()
    qry1="INSERT INTO `login`(`user_name`,`password`,`user_type`) VALUES ('"+email+"','"+password+"','user') "
    print(qry1)
    id=db.insert(qry1)
    qry2="INSERT INTO `user`(`user_name`,`age`,`gender`,`address`,`photo`,`login_id`,`phone`,`email`) VALUES ('"+name+"','"+dob+"','"+gender+"','"+address+"','"+path+"','"+str(id)+"','"+phone+"','"+email+"')"
    print(qry2)
    db.insert(qry2)
    return jsonify(status='ok')




@app.route('/usersendcomplaint',methods=['POST'])
def and_User_comp_viewreply():
    subject = request.form['edsubject']
    complaint = request.form['edcomplaint']
    customer_id =request.form['customer_id']
    db = Db()
    qry="INSERT INTO `complaint`(`subject`,`complaint`,`reply`,`date`,`customer_id`) VALUES ('"+subject+"','"+complaint+"','pending',NOW(),'"+customer_id+"')"
    id = db.insert(qry)
    return jsonify(status='ok')

@app.route('/viewprofile',methods=['POST'])
def viewprofile():
    login_id = request.form['login_id']
    print(login_id)
    db = Db()
    qry = "SELECT * FROM USER WHERE`login_id`='"+login_id+"'"
    res=db.selectone(qry)
    print(res)
    return jsonify(status='ok',user_name=res['user_name'],phone=res['phone'],age=res['age'],gender=res['gender'],address=res['address'],photo=res['photo'])

@app.route('/Parkinglocation_adminsignup',methods=['POST'])
def Parkinglocation_adminsignup():
    name=request.form['name']
    email = request.form['email']
    address= request.form['address']
    phone= request.form['phone']
    latitude= request.form['latitude']
    longitude= request.form['longitude']
    password= request.form['password']
    db=Db()
    qry1="INSERT INTO `login`(`user_name`,`password`,`user_type`) VALUES ('"+email+"','"+password+"','parking') "
    lid=db.insert(qry1)
    # qry2="INSERT INTO `parking`(`name`,`email`,`address`,`phone`,`latitude`,`longitude`,login_id) VALUES ('"+name+"','"+email+"','"+address+"','"+phone+"','"+latitude+"','"+longitude+"','"+str(lid)+"') "
    # db.insert(qry2)
    qry2="INSERT INTO `parking`(`name`,`email`,`address`,`phone`,`latitude`,`longitude`,login_id,status) VALUES ('"+name+"','"+email+"','"+address+"','"+phone+"','"+latitude+"','"+longitude+"','"+str(lid)+"','pending') "
    db.insert(qry2)
    return jsonify(status='ok')





@app.route('/Vehpark_viewprofile',methods=['POST'])
def Vehpark_viewprofile():
    login_id = request.form['login_id']
    print(login_id)
    db = Db()
    qry = "SELECT * FROM parking WHERE login_id='"+login_id+"'"
    print(qry)
    res=db.selectone(qry)
    print(res)
    if res is not None:
        data = {
            "name": res["name"],
            "email":res["email"],
            "address":res["address"],
            "phone": res["phone"],
            "latitude": res["latitude"],
            "longitude": res["longitude"]
        }
        return jsonify(status='ok', res=data,  name=res["name"],email = res["email"], address=res["address"], phone=res["phone"], latitude=res["latitude"], longitude=res["longitude"] )
    else:
        return  jsonify(status="notok")




@app.route('/vehicle/parking/manage',methods=['POST'])
def manageVehicleParking():
    login_id = request.form['login_id']
    print(login_id)
    db = Db()
    qry = ""
    res=db.selectone(qry)
    print(res)
    if res is not None:
        data = {
            "name": res["name"],
            "email":res["email"],
            "address":res["address"],
            "phone": res["phone"],
            "latitude": res["latitude"],
            "longitude": res["longitude"]
        }

        return jsonify(status='ok', res=data,  name=res["name"],email = res["email"], address=res["address"], phone=res["phone"], latitude=res["latitude"], longitude=res["longitude"] )
    else:
        return  jsonify(status="notok")




@app.route('/add_parkslot',methods=['POST'])
def add_parkslot():
    lid = request.form['lid']
    slot_name = request.form['slot_name']
    db = Db()
    qry="INSERT INTO `parking_slot`(`parking_id`,`slot_name`,status) VALUES('"+lid+"','"+slot_name+"','empty')"
    id = db.insert(qry)
    return jsonify(status='ok')


@app.route('/view_parkslot',methods=['POST'])
def view_parkslot():
    lid = request.form['lid']
    db = Db()
    qry="SELECT * FROM `parking_slot` WHERE `parking_id`='"+lid+"'"
    res = db.selectall(qry)
    return jsonify(status='ok',data=res)

@app.route('/view_compliant',methods=['POST'])
def view_compliant():
    lid = request.form['lid']
    db = Db()
    qry="SELECT * FROM complaint WHERE customer_id='"+lid+"'"
    print(qry)
    res = db.selectall(qry)
    return jsonify(status='ok',data=res)

@app.route('/user_view_parkinglocation',methods=['POST'])
def user_view_parkinglocation():
    db = Db()
    qry="SELECT * FROM `parking`"
    print(qry)
    res = db.selectall(qry)
    return jsonify(status='ok',data=res)







@app.route('/user_view_nearbystore',methods=['POST'])
def user_view_nearbystore():
    db = Db()
    qry="SELECT * FROM `store`"
    print(qry)
    res = db.selectall(qry)
    return jsonify(status='ok',data=res)

@app.route('/user_booking',methods=['POST'])
def user_booking():
    slot_id = request.form['slot_id']
    status ='pending'
    customer_id = request.form['customer_id']

    Account_number= request.form['accountno']
    Bank_name = request.form['bankname']
    password = request.form['password']
    db = Db()
    qry1="SELECT * FROM `bank`WHERE `Bank_name`='"+Bank_name+"'  and `Account_number`='"+Account_number+"' and  `password`='"+password+"'"
    print(qry1)
    res = db.selectone(qry1)
    if res is not None:
        db = Db()
        qry = "INSERT INTO `booking`(`slot_id`,`date`,`time`,`status`,`customer_id`,bankname,accountno) VALUES ('" + slot_id + "',curdate(),curtime(),'" + status + "','" + customer_id + "','"+Bank_name+"','"+Account_number+"')"
        print(qry,"aaaaa")
        res = db.insert(qry)
        return jsonify(status='ok')
    else:
        return jsonify(status='no')




@app.route('/bookhistory',methods=['POST'])
def bookhistory():
    customer_id = request.form['customer_id']
    db = Db()
    qry="SELECT `booking`.*,`parking`.*,`parking_slot`.* FROM `parking_slot`,`parking`,`booking` WHERE `booking`.`slot_id`=`parking_slot`.`parking_slot_id` AND `parking`.`login_id`=`parking_slot`.`parking_id` and `booking`.`customer_id`='"+customer_id+"' "
    print(qry)
    res = db.selectall(qry)
    return jsonify(status='ok',data=res)







@app.route('/booking_slot',methods=['POST'])
def booking_slot():
    user_id = request.form['user_id']
    space_id = request.form['space_id']
    print(space_id)
    db = Db()
    qq="SELECT COUNT(booking_slot_id) as book_count FROM `booking_slot`WHERE `space_slot_id`='"+space_id+"'"
    rr=db.selectone(qq)
    print(type(rr['book_count']))
    if rr['book_count']<5:
        qry="INSERT INTO `booking_slot`(`customer_id`,`time`,`date`,`space_slot_id`,`status`) VALUES('"+user_id+"',curtime(),curdate(),'"+space_id+"','pending')"
        db.insert(qry)
        return jsonify(status='ok')
    else:
        return jsonify(status="full")



@app.route('/view_my_spaceslotbooking', methods=['POST'])
def view_my_spaceslotbooking():
    db=Db()
    customer_id = request.form['customer_id']
    qry="SELECT `space_slot`.*,`store`.*,`booking_slot`.* FROM `booking_slot`,`space_slot`,`store` WHERE `space_slot`.`store_id`=`store`.`store_id` AND `booking_slot`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `booking_slot`.`customer_id`='"+customer_id+"'"
    res=db.selectall(qry)
    print(qry)
    return jsonify(status='ok',data=res)


@app.route('/security_view_tocken', methods=['POST'])
def security_view_tocken():
    db=Db()
    login_id = request.form['login_id']
    qry="SELECT `store_id`,`login_id` FROM`security` WHERE `login_id`='"+login_id+"'"
    print(qry)

    res=db.selectone(qry)

    sid=res['store_id']
    qry2="SELECT `space_slot`.`From_time`,`space_slot`.`T0_time`,`user`.`user_name`,`user`.`age`,`user`.`gender`,`user`.`address`,`user`.`phone`,`user`.`email`,`booking_slot`.`booking_slot_id`,`booking_slot`.`status` FROM space_slot ,`user` , `booking_slot`WHERE `booking_slot`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `booking_slot`.`customer_id`=`user`.`login_id` AND `space_slot`.`store_id`='"+str(sid)+"' and `booking_slot`.`status`!='exit'"
    print(qry)
    data=db.selectall(qry2)
    return jsonify(status='ok',data=data)


@app.route('/user_view_parkingslot',methods=['POST'])
def user_view_parkingslot():
    parking_id = request.form['pid']
    db = Db()
    qry="SELECT * FROM `parking_slot` WHERE `parking_id` in (SELECT `login_id` FROM `parking` WHERE `parking_slot_id`='"+parking_id+"')"
    print(qry)
    print(qry)
    res = db.selectall(qry)
    return jsonify(status='ok',data=res)



@app.route('/modify_slot',methods=['POST'])
def modify_slot():
    sid = request.form['sid']
    status = request.form['status']
    st = ""
    db = Db()
    if status=="empty":
        st = "filled"
    else:
        st = "empty"
    qry="UPDATE `parking_slot` SET `status`='"+st+"' WHERE `parking_slot_id`='"+sid+"'"
    res = db.update(qry)
    return jsonify(status='ok')


@app.route('/change_password',methods=['POST'])
def change_password():
    np = request.form['np']
    cp = request.form['cp']
    lid = request.form['lid']
    db1=Db()
    db=Db()
    qryy=db1.selectone("SELECT * FROM `login` WHERE `login_id`='"+lid+"' AND `password`='"+cp+"'")
    if qryy!=None:
        qry="UPDATE `login` SET `password`='"+np+"' WHERE `login_id`='"+lid+"'"
        res = db.update(qry)
        return jsonify(status='ok')
    else:
        return jsonify(status='2')


@app.route('/view_booking',methods=['POST'])
def view_booking():
    print("-----------------------------------")
    lid = request.form['lid']
    print(lid)
    db = Db()
    qry = "SELECT `booking`.*,`user`.user_name,user.phone,user.email  FROM `booking`,`parking_slot`,`parking` ,`user` WHERE `booking`.`slot_id`=`parking_slot`.`parking_slot_id` AND `parking_slot`.`parking_id`='"+lid+"' AND user.`login_id`=`booking`.`customer_id` AND `parking`.`login_id`=`parking_slot`.`parking_id`"
    print(qry)
    res = db.selectall(qry)
    print(res)
    return jsonify(status='ok', data=res)





@app.route('/view_payment_more',methods=['POST'])
def view_payment_more():
    bid = request.form['bid']
    print(bid)
    db = Db()
    qry = "SELECT * FROM `payment` INNER JOIN `booking` ON `booking`.`booking_id`=`payment`.`bookid` AND `booking`.`booking_id`='"+bid+"'"
    res = db.selectone(qry)
    print(res)
    return jsonify(status='ok', res=res[''])

@app.route("/security_viewbooking",methods=['POST'])
def security_viewbooking():
    store_id=request.form['store_id']
    print(store_id)
    db=Db()
    qry="SELECT * FROM `booking_slot`,space_slot,USER WHERE `booking_slot`.`space_slot_id`=`space_slot`.`spaceslot_id` AND `booking_slot`.`customer_id`=`user`.`login_id` AND `space_slot`.`store_id`='"+store_id+"'"
    print(qry)
    res = db.selectall(qry)
    print(res)
    return jsonify(status='ok', data=res)


@app.route('/View_store_freeslots',methods=['POST'])
def view_store_freeslots():
    store_id=request.form['store_id']
    print(store_id)
    db=Db()
    qry="SELECT spaceslot_id,convert(From_time,char) as From_time,convert(T0_time,char) as T0_time FROM `space_slot` WHERE status='free' and Date=curdate() and `store_id` in (select login_id from store where store_id='"+store_id+"')"
    print(qry)
    res = db.selectall(qry)
    if res is not None:
        return jsonify(status='ok',data=res)
    else:
        return jsonify(status='no')

@app.route('/entry',methods=['POST'])
def entry():
    booking_slot_id = request.form['booking_slot_id']
    status = request.form['status']
    db = Db()
    qry="UPDATE `booking_slot` SET status ='"+status+"' WHERE `booking_slot_id`='"+booking_slot_id+"' "
    res = db.update(qry)

    print(status)

    #_________________________ visiting history---------------------------------

    if status=="entered":

        qry1="SELECT * FROM `booking_slot` WHERE `booking_slot_id`='"+booking_slot_id+"'"
        booking_slot_data=db.selectone(qry1)
        if booking_slot_data is not None:

            user_id=booking_slot_data["customer_id"]
            date=booking_slot_data["date"]
            time=booking_slot_data["time"]
            space_slot_id=booking_slot_data["space_slot_id"]

            qry2="INSERT INTO `visiting_history`(`user_id`,`date`,`time`,`space_slot_id`)VALUES('"+str(user_id)+"','"+date+"','"+time+"','"+str(space_slot_id)+"')"
            db.insert(qry2)
        else:
            return jsonify(status="no")
    # else:
        # qry1 = "SELECT * FROM `booking_slot` WHERE `booking_slot_id`='" + booking_slot_id + "'"
        # booking_slot_data = db.selectone(qry1)
        # qq = "UPDATE `space_slot` SET `Status`='free' WHERE `spaceslot_id`='" + str(booking_slot_data["space_slot_id"]) + "'"
        # print(qq)
        # res = db.update(qq)



    return jsonify(status='ok',data=res)





@app.route('/user_visiting_history',methods=['POST'])
def user_visiting_history():
    login_id = request.form['login_id']
    db = Db()
    qry = "SELECT `booking_slot`.`booking_slot_id`,`booking_slot`.`status`,`space_slot`.`From_time`,`space_slot`.`Date`,`space_slot`.`T0_time`,`store`.`store_name`,`store`.`place`,`store`.`phone`,`store`.`email` FROM  `space_slot`,`store`,`booking_slot` WHERE `booking_slot`.`space_slot_id`=`space_slot`.`spaceslot_id` AND`space_slot`.`store_id`=`store`.`store_id` AND `booking_slot`.status!='pending' AND `booking_slot`.`customer_id`='"+login_id+"'"
    print(qry)
    res=db.selectall(qry)
    return jsonify(status='ok',data=res)

@app.route('/covid_statusinsertion',methods=['POST'])
def covid_statusinsertion():
    login_id = request.form['login_id']
    z=request.form["status"]
    db = Db()
    qry = "SELECT * FROM `covid_status` WHERE `user_id`='" + login_id + "' "
    print(qry)
    res = db.selectone(qry)
    if res is  None:
        qry="INSERT INTO `covid_status`(`user_id`,`date`,`Status`) VALUES ('"+login_id+"',curdate(),'"+z+"')"
        print(qry)
        res=db.insert(qry)
        return jsonify(status='ok')
    else:
        qry = "UPDATE `covid_status` SET `Status`='"+z+"' WHERE `user_id`='"+login_id+"'"
        print(qry)
        res = db.update(qry)
        return jsonify(status='ok')


@app.route('/user_view_covidstatus',methods=['POST'])
def user_view_covidstatus():
    login_id = request.form['login_id']
    db = Db()
    qry="SELECT * FROM `covid_status` WHERE `user_id`='"+login_id+"' "
    print(qry)
    res=db.selectone(qry)
    print(res)
    if res is not  None:
        return jsonify(status='ok',sts=res['Status'])
    else:
        return jsonify(status='no')

@app.route('/sview_sts',methods=['POST'])
def sview_sts():
    sid = request.form['sp_id']
    ty=request.form["ty"]
    db = Db()

    if ty=="exit":
        qq="UPDATE `space_slot` SET `Status`='free' WHERE `spaceslot_id`='"+str(sid)+"'"
        print(qq)
        res=db.update(qq)
    else:
        qry="UPDATE `space_slot` SET `Status`='"+ty+"' WHERE `spaceslot_id`='"+str(sid)+"'"
        print(qry)
        res=db.update(qry)
    return jsonify(status='ok')



if __name__ == '__main__':
    app.run(debug=True,port=3500,host='0.0.0.0')
