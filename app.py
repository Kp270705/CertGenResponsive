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
def ProcessData(eventname, orgname, certificate_choice, oprchoice, csvPath, logo1Path, logo2Path, hodPath, ccPath):  # which get data from operated csv files:
    
    # global csvData
    global csvData
    csvData = processFile(f"{csvPath}")
    # CertificateEssestials = f"./static/Images/CertificateEssentials"
    from getPath import get_Choice_data

    from redesignTemplate import templatedesign
    match oprchoice:

        case "Generate":
            if certificate_choice == "Choice1":
                pathkey = get_Choice_data(certificate_choice)
                print(f"{pathkey}")
                finalTemplatePath = templatedesign(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], ccPath, hodPath)

            if certificate_choice == "Choice2":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], ccPath, hodPath)

            if certificate_choice == "Choice3":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], ccPath, hodPath)

            i=0
            for CSV in csvData:
                    i+=1
                    getData(CSV.name, CSV.sId, CSV.duration, CSV.pulse, CSV.maxpulse, CSV.calories, CSV.course, CSV.semester, i, eventname, orgname, certificate_choice, oprchoice, finalTemplatePath)


        case "Preview":

            if certificate_choice == "Choice1":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], ccPath, hodPath)
                
            if certificate_choice == "Choice2":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], ccPath, hodPath)

            if certificate_choice == "Choice3":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], ccPath, hodPath)

            i=0
            for CSV in csvData:
                    i+=1
                    getData(CSV.name, CSV.sId, CSV.duration, CSV.pulse, CSV.maxpulse, CSV.calories, CSV.course, CSV.semester, i, eventname, orgname, certificate_choice, oprchoice, finalTemplatePath)
                    if i == 1:
                        break

    zip_folder(f"./static/PDFFolder", f"./static/{oprchoice}edCertificate{i}.zip")
    # return render_template(f"Register.html")        
    print(f"\tLogoFileName is:{logo1Path}")
    print(f"\n\tThere are {i} rows of data in given csv file.\n")


# check file exist or not, if exist then process task:
@app.route('/csv', methods=['GET', 'POST'])
def upload_file():
    userFiles = f"./Uploads"
    if request.method == 'POST':
        
        oprchoice = request.form.get("action")
        
        certificate_choice_id = f" "
        certificate_choice = request.form.get('certificate_choice') # it didn't use in our code, yet

        if request.form.get('certificate_choice') == 'Choice1':
            certificate_choice_id = request.form.get('certificate_choice')

        elif request.form.get('certificate_choice') == 'Choice2':
            certificate_choice_id = request.form.get('certificate_choice')

        elif request.form.get('certificate_choice') == 'Choice3':
            certificate_choice_id = request.form.get('certificate_choice')
            
        eventName = request.form.get("eventName")
        
        orgName = request.form.get("OrgName")
        
        print(f"Certificate choice id name: {certificate_choice_id}")
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        print(f"{request.files}")
        CsvFile = request.files['file']
        Logo1File = request.files["logo"] # to get name of logo file

        Logo2File = request.files["logo2"] # to get name of logo file

        HodFile = request.files["hod"] # to get name of logo file

        CcFile = request.files["cc"] # to get name of logo file

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
            Logo1File.save(os.path.join(app.config['UPLOAD_FOLDER'], logo1_filename))

        if (Logo2File and allowed_file(Logo2File.filename)) or (Logo2File.filename) :
            logo2_filename = secure_filename(Logo2File.filename)
            Logo2File.save(os.path.join(app.config['UPLOAD_FOLDER'], logo2_filename))

        if (HodFile and allowed_file(HodFile.filename)) or (HodFile.filename) :
            hod_filename = secure_filename(HodFile.filename)
            HodFile.save(os.path.join(app.config['UPLOAD_FOLDER'], hod_filename))

        if (CcFile and allowed_file(CcFile.filename)) or (CcFile.filename) :
            cc_filename = secure_filename(CcFile.filename)
            CcFile.save(os.path.join(app.config['UPLOAD_FOLDER'], cc_filename))
            
        if oprchoice == "Generate":
            ProcessData(eventName, orgName, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", f"{userFiles}/{logo2_filename}", f"{userFiles}/{hod_filename}", f"{userFiles}/{cc_filename}")
            return render_template("ack.html")
        if oprchoice == "Preview":
            ProcessData(eventName, orgName, certificate_choice_id, oprchoice, f"{userFiles}/{csv_filename}", f"{userFiles}/{logo1_filename}", f"{userFiles}/{logo2_filename}", f"{userFiles}/{hod_filename}", f"{userFiles}/{cc_filename}")
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
        
    return render_template("Register.html")


# landing page:
@app.route("/landing")
def landingPage():
    return render_template("landing.html")

#loggin page
@app.route('/', methods=['GET', 'POST'])
def Loggin():
    if request.method == "POST":
        
        email = request.form['email']
        name = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(email=email).first() # you can choose any of these filter_by()
        # user = User.query.filter_by(name=name).first()
        # user = (User.query.filter_by(name=name).first()) and (User.query.filter_by(email=email).first())
        
        if user and user.check_password(password):
            session['name'] = user.name # after selecting filter_by() on wish, select right session.
            session['email'] = user.email
            return redirect('/landing')
        else:
            return render_template('Loggin.html', error="Invalid user")

    return render_template("Loggin.html")

# home page: 
@app.route("/home")
def home():
    
    # if session['email']: # then give here right session acc. to mentioned seesion in loggin route. 
    # # if session['name']:
    # # if (session['name']) and (session['email']):
    #     return render_template("home.html")
    
    return render_template("home.html")
    

# driver code: 
if __name__  ==  "__main__":
    app.run(debug=1, port=5000) 
