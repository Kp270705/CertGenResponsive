from flask import Flask, render_template, jsonify, request, flash, redirect, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from flask_uploads import UploadSet, IMAGES, configure_uploads
import os, uuid, bcrypt
from csvFunc import processFile
from generate_pdf import getData
from genZip import zip_folder

UPLOAD_FOLDER = 'Uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}

csvData = []
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = uuid.uuid4().hex
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# defining db class: 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    name = db.Column(db.String(150), nullable=0)
    password = db.Column(db.String(150), nullable=0, unique=1)
    confirm_password = db.Column(db.String(150), nullable=0, unique=1)
    email = db.Column(db.String(150), nullable=0)
    # fav_color = db.Column(db.String(30), nullable=1)
    
    print(f" confirm pass{confirm_password}")
    
    # used to initialise the db's data:
    def __init__(self, name, email, password, confirm_password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
        self.confirm_password = confirm_password
        # self.fav_color = fav_color

    # used to check password:
    def check_password(self, pasword):
        return bcrypt.checkpw(pasword.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()


# check file extension:
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/ack")
def ProcessData(eventname, orgname, certType, certificate_choice, oprchoice, csvPath, logo1Path, logo2Path, organizer1_designation, organizer1Path, organizer2_designation, organizer2Path):  # which get data from operated csv files:
    
    # global csvData
    global csvData
    csvData = processFile(f"{csvPath}")

    from getPath import get_Choice_data

    from redesignTemplate import templatedesign1_2_3, templatedesign4, templatedesign5
    match oprchoice:

        case "Generate":
            if certificate_choice == "Choice1":
                pathkey = get_Choice_data(certificate_choice)
                print(f"{pathkey}")
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice2":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice3":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice4":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign4(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)
            
            if certificate_choice == "Choice5":
                print(f"\n\tin {certificate_choice} ")
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign5(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)


            i=0
            for CSV in csvData:
                    i+=1
                    getData(CSV.name, CSV.sId, CSV.emailId, CSV.course, CSV.semester, CSV.date, i, eventname, orgname, certType, certificate_choice, oprchoice, organizer1_designation, organizer2_designation, finalTemplatePath)


        case "Preview":

            if certificate_choice == "Choice1":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)
                
            if certificate_choice == "Choice2":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice3":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice4":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign4(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice5":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign5(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)
            
            
            i=0
            for CSV in csvData:
                    i+=1
                    getData(CSV.name, CSV.sId, CSV.emailId, CSV.course, CSV.semester, CSV.date, i, eventname, orgname, certType, certificate_choice, oprchoice, organizer1_designation, organizer2_designation, finalTemplatePath)
                    if i == 1:
                        break

    zip_folder(f"./static/PDFFolder", f"./static/{oprchoice}Certificate.zip")
    # return render_template(f"Register.html")        
    print(f"\tLogoFileName is:{logo1Path}")
    print(f"\n\tThere are {i} rows of data in given csv file.\n")



# check file exist or not, if exist then process task:
@app.route('/csv', methods=['GET', 'POST'])
def upload_file():
    userFiles = f"./Uploads"
    if request.method == 'POST':
        
        oprchoice = request.form.get("action")
        
        print("\n\nIn uploadfiles....")
        certificate_choice_id = request.form.get('certificate_choice')
        print(f"Certificate choice id name: {certificate_choice_id}")
        eventName = request.form.get("eventName")
        orgName = request.form.get("OrgName")
        certType = request.form.get("certificateType")
        print(f"certificate type: {certType} ")
        organizer1 = request.form.get("Organizer1Desig")
        organizer2 = request.form.get("Organizer2Desig")
        print(f"orgnzr1 desig:{organizer1}")
        print(f"orgnzr2 desig:{organizer2}")

        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        print(f"{request.files}")
        CsvFile = request.files['file']
        Logo1File = request.files["logo"] # to get name of logo file
        Logo2File = request.files["logo2"]

        organizer1File = request.files["organizer1"] 
        organizer2File = request.files["organizer2"] 

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        
        if CsvFile.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if (CsvFile and allowed_file(CsvFile.filename)) or (CsvFile.filename) :
            csv_filename = secure_filename(CsvFile.filename)
            CsvFile.save(os.path.join(app.config['UPLOAD_FOLDER'], csv_filename))
            
        if (Logo1File and allowed_file(Logo1File.filename)) or (Logo1File.filename) :
            logo1_filename = secure_filename(Logo1File.filename)
            print(f"\n\n\tlogo1_filename:{logo1_filename}")   
            Logo1File.save(os.path.join(app.config['UPLOAD_FOLDER'], logo1_filename))

        if (Logo2File and allowed_file(Logo2File.filename)) or (Logo2File.filename) :
            logo2_filename = secure_filename(Logo2File.filename)
            print(f"\n\n\tlogo2_filename:{logo2_filename}")   
            Logo2File.save(os.path.join(app.config['UPLOAD_FOLDER'], logo2_filename))

        if (organizer1File and allowed_file(organizer1File.filename)) or (organizer1File.filename) :
            organizer1_filename = secure_filename(organizer1File.filename)
            organizer1File.save(os.path.join(app.config['UPLOAD_FOLDER'], organizer1_filename))

        if (organizer2File and allowed_file(organizer2File.filename)) or (organizer2File.filename) :
            organizer2_filename = secure_filename(organizer2File.filename)
            organizer2File.save(os.path.join(app.config['UPLOAD_FOLDER'], organizer2_filename))

        print(f"logo2 file: {Logo2File}")

        if oprchoice == "Generate":
            # if Logo2File == "<'' ('application/octet-stream')>":
            if Logo2File.filename == '':
                print(f'\n\n\tIn if condition')
                ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", None, organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}")
            else:
                print(f'\n\n\tIn else condition...')
                ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", f"{userFiles}/{logo2_filename}", organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}")

            return render_template("ack.html")
        
        if oprchoice == "Preview":
            # if Logo2File == "<FileStorage: '' ('application/octet-stream')>":
            if Logo2File.filename == '':
                print(f'\n\n\tIn if condition')
                ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", None, organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}")
            else:
                print(f'\n\n\tIn else condition...')
                ProcessData(eventName, orgName, certType, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", f"{userFiles}/{logo2_filename}", organizer1, f"{userFiles}/{organizer1_filename}", organizer2, f"{userFiles}/{organizer2_filename}")

            return render_template("preview.html")
        

        print("After ProcessData()...")

    return render_template("home.html")

#use to show user given data in new page:
@app.route("/csvFile")
def showcsv():
    return render_template("yourData.html", data=csvData)

# use to navigate to registration page:
@app.route("/Register", methods=["GET", "POST"])
def Register():
    if request.method == "POST":
        username = request.form['username']
        # fav_color = request.form["fav_color"]
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        
        newUser = User(username, email, password, confirm_password)
        if password == confirm_password:
            db.session.add(newUser)
            db.session.commit()
            return redirect("/")
        
    return render_template("RegisterT.html")


# landing page:
@app.route("/landing", methods=['GET', 'POST'])
def landingPage():
    if request.method == "POST":
        return render_template("landingT.html")
    return render_template("landingT.html")

#loggin page
@app.route('/', methods=['GET', 'POST'])
def Loggin():
    print(f"\n\n\nMethod is: {request.method} ")
    if request.method == "POST":
        email = request.form['email']
        name = request.form['username']
        password = request.form['password']
        print(f"\npassword is: {password} ")

        # user = User.query.filter_by(email=email).first() # you can choose any of these filter_by()
        user = User.query.filter_by(name=name).first()

        # user = (User.query.filter_by(name=name).first()) and (User.query.filter_by(email=email).first())

        print(f"\n\tuser is: {user} ")
        print(f"\n\tuser password is: {user.check_password(password)} ")
        
        if user and user.check_password(password):
            print(f"\n\npassword: {password}")
            print(f"\n\n\tPassword matched...")

            # session['email'] = user.email
            session['name'] = user.name # after selecting filter_by() on wish, select right session.

            print(f"going to home")
            return render_template("landingT.html")
        
        else:
            print("\n\n\tpassword not match...")
            return render_template('LogginT.html', error="Invalid user")
    if request.method == "GET":
        return render_template ("LogginT.html")

    return render_template("LogginT.html")

# home page: 
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return render_template("home.html")
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")    

# driver code: 
if __name__  ==  "__main__":
    app.run(debug=1, host='0.0.0.0', port=5000) 
